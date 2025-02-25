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

def debug_code(code):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Add inline comments suggesting fixes, but do **NOT** change code itself:\n```python\n{code}\n```"
    response = model.generate_content(prompt)

    if hasattr(response, "text"):
        cleaned_content = re.sub(r"```(?:python)?\n?|```", "", response.text).strip()
        return cleaned_content
    else:
        return ""


def write_file(file_path, lines):
    """Writes modified lines back to the file."""
    with open(file_path, "w") as file:
        file.writelines(lines)

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

    fixed_code = debug_code(code)
    print("\n[ Suggested Fixes]:\n", fixed_code)

    write_file(file_path,fixed_code)
    

if __name__ == "__main__":
    main()