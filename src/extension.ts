import * as vscode from "vscode";
import { execFile } from "child_process";
import * as path from "path";

// Function to call the Python script
function runPythonScript(
  filePath: string,
  context: vscode.ExtensionContext
): void {
  const pythonExecutable = "python"; // Change to "python3" if required
  const scriptPath = path.join(context.extensionPath, "main.py"); // Update with your actual Python script name

  vscode.window.showInformationMessage(`Processing file: ${filePath}`);
  console.log("About to run Python script...");

  execFile(
    pythonExecutable,
    [scriptPath, filePath],
    (error, stdout, stderr) => {
      console.log("Py Run!");
      if (error) {
        vscode.window.showErrorMessage(
          `Error executing Python script: ${error.message}`
        );
        console.error("Error:", error);
        return;
      }

      if (stderr) {
        vscode.window.showWarningMessage(`Python script warning: ${stderr}`);
        console.warn("Python Script Warning:", stderr);
      }

      vscode.window.showInformationMessage(`Python Output: ${stdout}`);
      console.log("Python Output:", stdout);
    }
  );
}

function runFixes(filePath: string, context: vscode.ExtensionContext): void {
  const pythonExecutable = "python"; // Change to "python3" if required
  // const scriptPath = path.join(context.extensionPath, "main.py"); // Update with your actual Python script name
  const fixPath = path.join(context.extensionPath, "fixes.py"); // Update with your actual Python script name

  vscode.window.showInformationMessage(`Processing file: ${filePath}`);
  console.log("About to run Python script...");

  execFile(pythonExecutable, [fixPath, filePath], (error, stdout, stderr) => {
    console.log("Py Run!");
    if (error) {
      vscode.window.showErrorMessage(
        `Error executing Python script: ${error.message}`
      );
      console.error("Error:", error);
      return;
    }

    if (stderr) {
      vscode.window.showWarningMessage(`Python script warning: ${stderr}`);
      console.warn("Python Script Warning:", stderr);
    }

    vscode.window.showInformationMessage(`Python Output: ${stdout}`);
    console.log("Python Output:", stdout);
  });
}

function runGenCode(filePath: string, context: vscode.ExtensionContext): void {
  const pythonExecutable = "python"; // Change to "python3" if required
  // const scriptPath = path.join(context.extensionPath, "main.py"); // Update with your actual Python script name
  const fixPath = path.join(context.extensionPath, "fixes.py"); // Update with your actual Python script name

  vscode.window.showInformationMessage(`Processing file: ${filePath}`);
  console.log("About to run Python script...");

  execFile(pythonExecutable, [fixPath, filePath], (error, stdout, stderr) => {
    console.log("Py Run!");
    if (error) {
      vscode.window.showErrorMessage(
        `Error executing Python script: ${error.message}`
      );
      console.error("Error:", error);
      return;
    }

    if (stderr) {
      vscode.window.showWarningMessage(`Python script warning: ${stderr}`);
      console.warn("Python Script Warning:", stderr);
    }

    vscode.window.showInformationMessage(`Python Output: ${stdout}`);
    console.log("Python Output:", stdout);
  });
}

// Extension activation
export function activate(context: vscode.ExtensionContext) {
  console.log(' Extension "smarty" is now active!');
  vscode.window.showInformationMessage("Smarty Extension Activated!");

  let disposable = vscode.commands.registerCommand(
    "smarty.processPythonFile",
    () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showErrorMessage(
          "No active editor. Open a Python file to process."
        );
        return;
      }
      vscode.window.showInformationMessage("Holaa!");
      const filePath = editor.document.fileName;
      runPythonScript(filePath, context);
    }
  );

  let applyFixesCmd = vscode.commands.registerCommand(
    "smarty.applyFixes",
    () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showErrorMessage(
          "No active editor. Open a Python file to process."
        );
        return;
      }
      const filePath = editor.document.fileName;
      runFixes(filePath, context);
    }
  );

  let genCode = vscode.commands.registerCommand("smarty.genCode", () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage(
        "No active editor. Open a Python file to process."
      );
      return;
    }
    const filePath = editor.document.fileName;
    runGenCode(filePath, context);
  });

  // const disposable = vscode.commands.registerCommand(
  //   "smarty.helloWorld",
  //   () => {
  //     // The code you place here will be executed every time your command is executed
  //     // Display a message box to the user
  //     vscode.window.showInformationMessage("Hello World from smarty!");
  //   }
  // );

  context.subscriptions.push(disposable, applyFixesCmd, genCode);
}

// Deactivate extension
export function deactivate() {
  console.log(" Smarty Extension Deactivated!");
}
