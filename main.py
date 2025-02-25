import google.generativeai as genai
import sys
from watchdog.observers import Observer
import os
import re
from watchdog.events import FileSystemEventHandler

genai.configure(api_key="api key")

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_test_file(file_path, content,file_name):
    cleaned_content = re.sub(r"```(?:python)?\n?|```", "", content).strip()
    file_name_remove_Py=os.path.splitext(file_name)[0]
    with open(file_path, "w") as file:
        import_statement = f"from {file_name_remove_Py} import *\n"
        file.write(import_statement)
        file.write(cleaned_content)


def generate_test_cases(func_code):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Generate compprehensive pytest unit test cases for the following function give code with comments that can be run directly:\n```python\n{func_code}\n```"
    response = model.generate_content(prompt)
    return response.text.strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    parent_dir = os.path.dirname(file_path)
    
    test_dir = os.path.join(parent_dir, "test")
    os.makedirs(test_dir, exist_ok=True)


    file_name = os.path.basename(file_path)
    test_file_name = f"test_{file_name}"
    test_file_path = os.path.join(test_dir, test_file_name)

    print(f"\n[Processing File '{file_name}'...]\n")

    code = read_file(file_path)
    print("[ Code Detected]:\n", code)

    test_cases = generate_test_cases(code)
    write_test_file(test_file_path, test_cases, file_name)

    print(f"\n[ Test Cases Saved to '{test_file_path}']")

if __name__ == "__main__":
    main()