import re
def validate_script(text):
    if re.fullmatch(r'[A-Za-z\s]+', text):
        print("Text is valid and in English script.")
    else:
        print("Text contains non-English characters.")
file_path = input("Enter file path: ")
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()
    validate_script(file_content)

# OUTPUT EXAMPLES
# Textfile1: "Hello! This text is in English only."
# Output: Text is valid and in English script.
# Textfile2: "This text contains 漢字 characters."
# Output: Text contains non-English characters.
