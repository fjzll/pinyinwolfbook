import pypinyin


def text_to_pinyin(text):
    pinyin_text = ""
    for char in text:
        if '\u4e00' <= char <= '\u9fff':  # Chinese character range
            pinyin_annotation = pypinyin.pinyin(char, style=pypinyin.TONE3, heteronym=False)
            pinyin_text += char + "(" + ''.join(pinyin_annotation[0]) + ")"
        else:
            pinyin_text += char
    return pinyin_text

# Read file from source text.
source_file_path = "/Users/admin/Desktop/pinyinwolfbook/wolfbookshortversion.txt"
with open(source_file_path, "r") as file:
    extracted_text = file.read()

# Convert into pinyin
annotated_text = text_to_pinyin(extracted_text)

# write the formatted text to a file
with open("/Users/admin/Desktop/pinyinwolfbook/pinyinwolfbook.txt", "w") as file:
    file.write(annotated_text)

