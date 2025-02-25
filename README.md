# AutoCode Extension 

This is the README for your extension "AutoCode-Extension." This extension helps automate code generation, debugging, and test creation within VS Code. This extension integrates with VS Code.

## Features

- Generate code for python using AI
- AI-driven bug detection and fixing.
- Automated test case generation.

## Requirements

Ensure you have the following dependencies installed before using this extension: NodeJS, Python, VSCode, Gemini API Key

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/suprajasesh/AutoCode-Extension.git
   ```
2. Navigate to the project directory:
   ```sh
   cd AutoCode-Extension
   ```
3. Install dependencies:
   ```sh
   npm install
   ```
4. Gnerate a Gemini API Key and use it.
   
## Run Instructions
1. Compile the program:
   ```sh
   npm run compile
   ```
2. Press F5 to open the Extension Developer Mode

## Usage

1. Open a file in VS Code.
2. Use the command palette (`Ctrl+Shift+P`) to access AutoCode commands.
3. Select an action such as `Smarty: Generate Code`, `Smarty: Fix`, or `Smarty: Generate Tests Cases`.

## Known Issues

- Some generated code may require manual adjustments.
- Works for python only as of now
- Debugging suggestions may not cover all edge cases.
