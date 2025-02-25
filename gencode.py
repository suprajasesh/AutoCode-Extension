import google.generativeai as genai
import sys
import os
import re

genai.configure(api_key="api key")

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()  
    
def generate_code(prompt):
    """Generates code using Gemini based on a given prompt."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Generate Python code for: {prompt}")
    
    if hasattr(response, "text"):
        return response.text.strip()
    return ""

def process_code(lines):
    """Processes code and replaces comment-based placeholders with generated code."""
    new_lines = []
    for line in lines:
        match = re.search(r"#\s*generate:\s*(.*)", line, re.IGNORECASE)
        write= re.search(r"#\s*write:\s*(.*)", line, re.IGNORECASE)
        if match:
            prompt = match.group(1)
            print(f"Generating code for: {prompt}")
            generated_code = generate_code(prompt)
            new_lines.append(generated_code + "\n")  
        elif write:
            prompt = write.group(1)
            print(f"Generating code for: {prompt}")
            generated_code = generate_code(prompt)
            generated_code = re.sub(r"^#", "", generated_code).strip()  
            generated_code = re.sub(r"```python\s*", "", generated_code) 
            generated_code = re.sub(r"```", "", generated_code)  
            
            new_lines.append(generated_code + "\n")
            new_lines.append(generated_code + "\n")
        else:
            new_lines.append(line)
    return new_lines

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

    lines = read_file(file_path)
    print("[ Code Detected]:\n", "".join(lines))

    modified_lines = process_code(lines)

    write_file(file_path, modified_lines)

    print("\n[ Code Updated with Generated Sections ]")

if __name__ == "__main__":
    main()
