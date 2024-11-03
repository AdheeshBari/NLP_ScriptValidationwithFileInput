# NLP_ScriptValidationwithFileInput
This Python script checks if the text in a specified file contains only English letters and spaces, printing a validation message accordingly.

This Python script validates if the text in a specified file contains only English alphabetic characters and whitespace. It reads the file content and checks for non-English characters, printing a message accordingly.
How it works:
1. Function Definition:
      The validate_script function uses a regular expression to check if the input text contains only English letters (both uppercase and lowercase) and spaces.
      If the text matches this pattern, the script prints "Text is valid and in English script." Otherwise, it prints "Text contains non-English characters."
2. File Reading:
      The script prompts the user to enter a file path, then opens the file in read mode ('r') with UTF-8 encoding.
      It reads the entire file content and passes it to the validate_script function for validation.
3. Examples:
      File Content: "Hello! This text is in English only."
      Output: "Text is valid and in English script."
      File Content: "This text contains 漢字 characters."
      Output: "Text contains non-English characters."
This script is useful for quickly validating English-only text content within a file.
