import pypinyin
from pypinyin import Style

def text_to_pinyin(text):
    pinyin_lines = []  # For storing pinyin annotations
    chinese_lines = []  # For storing corresponding Chinese characters

    for char in text:
        if '\u4e00' <= char <= '\u9fff':  # Chinese character range
            # Use Style.TONE to get pinyin with tone marks
            pinyin_annotation = pypinyin.pinyin(char, style=Style.TONE, heteronym=False)
            pinyin_lines.append(''.join(pinyin_annotation[0]))  # Add pinyin to the list
            chinese_lines.append(char)  # Add Chinese character to the list
        else:
            # For non-Chinese characters, add them directly, keeping the alignment
            pinyin_lines.append(' ')
            chinese_lines.append(char)

    # Combine the lists into strings, with each element followed by a space for alignment
    pinyin_text = ' '.join(pinyin_lines)
    chinese_text = ' '.join(chinese_lines)

    # Format the final text with pinyin above the Chinese characters
    formatted_text = pinyin_text + '\n' + chinese_text

    return formatted_text

# Read file from source text.
source_file_path = "/Users/admin/Desktop/pinyinwolfbook/wolfbookshortversion.txt"
with open(source_file_path, "r") as file:
    extracted_text = file.read()

# Convert into pinyin
annotated_text = text_to_pinyin(extracted_text)

# Write the formatted text to a file
with open("/Users/admin/Desktop/pinyinwolfbook/pinyinwolfbook.txt", "w") as file:
    file.write(annotated_text)
