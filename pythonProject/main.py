import PyPDF2
import pypinyin


# Read from PDF and return text for pinyin conversion
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'  # Concatenate text from each page
    return text


def text_to_pinyin(text):
    pinyin_text = ""
    for char in text:
        if '\u4e00' <= char <= '\u9fff':  # Chinese character range
            pinyin_annotation = pypinyin.pinyin(char, style=pypinyin.TONE3, heteronym=False)
            pinyin_text += char + "(" + ''.join(pinyin_annotation[0]) + ")"
        else:
            pinyin_text += char
    return pinyin_text


# Specify the path to your PDF
pdf_path = "/Users/admin/Desktop/pinyinwolfbook/testwolfbook.pdf"

# Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# Convert into pinyin
annotated_text = text_to_pinyin(extracted_text)


# write the formatted text to a file
with open("/Users/admin/Desktop/pinyinwolfbook/pinyinwolfbook.txt", "w") as file:
    file.write(annotated_text)

