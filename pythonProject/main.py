import pypinyin
from pypinyin import Style
import os


def text_to_pinyin(text, chunk_size=8):
    # First pass: find the maximum pinyin length
    max_length = 0
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        for char in chunk:
            if '\u4e00' <= char <= '\u9fff':  # Chinese character range
                pinyin_annotation = pypinyin.pinyin(char, style=Style.TONE, heteronym=False)
                pinyin_length = len(''.join(pinyin_annotation[0]))
                max_length = max(max_length, pinyin_length)
    # print(max_length)

    # Second pass: format the text with padding
    formatted_text = ""  # Initialize the formatted text string

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        pinyin_line = ""
        chinese_line = ""

        for char in chunk:
            if '\u4e00' <= char <= '\u9fff':  # Chinese character range
                # Get pinyin with tone marks
                pinyin_annotation = pypinyin.pinyin(char, style=Style.TONE, heteronym=False)
                pinyin = ''.join(pinyin_annotation[0])
                # Pad the pinyin to the max length
                pinyin_line += pinyin.ljust(max_length+1)
                chinese_line += char.ljust(max_length)
            else:
                # Non-Chinese characters, add spaces in pinyin line for alignment
                pinyin_line += char.ljust(1)
                chinese_line += char.ljust(1)

        # Combine the pinyin and Chinese characters
        formatted_text += pinyin_line.rstrip() + '\n' + chinese_line.rstrip() + "\n\n"

    return formatted_text.strip()


# Specify the source directory where your files are located
source_directory = '/Users/admin/Desktop/pinyinwolfbook'
# Specify the destination directory where you want the new files to be saved
destination_directory = '/Users/admin/Desktop/pinyinwolfbook'
# Ensure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)
# Process files from Chapter 1 to 36
for chapter_number in range(10, 37):  # 1 to 36 inclusive
    # Construct file name based on chapter number
    filename = f'Simplified_Chapter{chapter_number}_Mandarin.txt'
    source_file_path = os.path.join(source_directory, filename)

    # Ensure the source file exists before attempting to process it
    if os.path.exists(source_file_path):
        output_filename = f'pinyinwolfbook_chapter{chapter_number}.txt'
        destination_file_path = os.path.join(destination_directory, output_filename)

    # Read the content of the source file
        with open(source_file_path, 'r', encoding='utf-8') as file:
            extracted_text = file.read()

# Read file from source text.
# source_file_path = "/Users/admin/Desktop/pinyinwolfbook/Simplified_Chapter9_Mandarin.txt"
# with open(source_file_path, "r", encoding='utf-8') as file:
#    extracted_text = file.read()

# Convert into pinyin
        annotated_text = text_to_pinyin(extracted_text)

# Write the formatted text to a file
# output_file_path = "/Users/admin/Desktop/pinyinwolfbook/pinyinwolfbook_chapter9.txt"
        with open(destination_file_path, "w", encoding='utf-8') as file:
            file.write(annotated_text)
