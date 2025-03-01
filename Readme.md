# Code Management and Streamlit Generator Application

Welcome to the **Code Management and Streamlit Generator Application**! This Python-based toolset automates file creation, Streamlit application generation, GitHub version control, and file reading within a specified directory. Built with flexibility and modularity in mind, it empowers developers to streamline coding workflows and deploy Streamlit apps efficiently.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [CodeFileTool](#codefiletool)
  - [GitPushCodeTool](#gitpushcodetool)
  - [StreamlitCodeGenerator](#streamlitcodegenerator)
  - [FileReaderTool](#file_readertool)
- [Configuration](#configuration)
- [Examples](#examples)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features
- **File Creation**: Create or append to files programmatically with `CodeFileTool`.
- **GitHub Integration**: Push files to a GitHub repository with `GitPushCodeTool`.
- **Streamlit Code Generation**: Generate Python code for Streamlit applications using the Groq API with `StreamlitCodeGenerator`.
- **File Reading**: Read file contents from a specified directory with `FileReaderTool`.
- **Modular Design**: Tools are built as classes inheriting from `smolagents.Tool`, making them easy to integrate into larger workflows.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   See [Dependencies](#dependencies) for a list of required packages.

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add:
   ```plaintext
   GROQ_API_KEY=your_groq_api_key
   GITHUB_USERNAME=your_github_username
   GITHUB_TOKEN=your_github_token
   ```
   Replace placeholders with your actual credentials.

## Usage

Each tool is designed to be instantiated and used independently or as part of a larger agent-based system (e.g., using `smolagents.CodeAgent`).

### CodeFileTool
**Purpose**: Creates or appends code to files in the local filesystem.
- **Initialization**:
  ```python
  from tools import CodeFileTool
  tool = CodeFileTool()
  ```
- **Example**:
  ```python
  result = tool.forward(filename="script.py", code="print('Hello')", mode="create")
  print(result)  # "File 'script.py' created successfully with the provided code."
  ```

### GitPushCodeTool
**Purpose**: Commits and pushes existing files from a local directory to a GitHub repository.
- **Initialization**:
  ```python
  from tools import GitPushCodeTool
  tool = GitPushCodeTool()
  ```
- **Example**:
  ```python
  result = tool.forward(commit_message="Add new script")
  print(result)  # "Files successfully pushed to GitHub repository 'automated_coading_4'..."
  ```
- **Note**: Assumes files are already created in `/content/Repo/automated_coading_4`.

### StreamlitCodeGenerator
**Purpose**: Generates Python code for Streamlit apps using the Groq API.
- **Initialization**:
  ```python
  from tools import StreamlitCodeGenerator
  tool = StreamlitCodeGenerator(api_key="your_groq_api_key")
  ```
- **Example**:
  ```python
  code = tool.forward(prompt="Create a Streamlit app with a button")
  print(code)
  # Expected output:
  # import streamlit as st
  # if st.button("Click Me"):
  #     st.write("Button clicked!")
  ```

### FileReaderTool
**Purpose**: Reads the content of a file in a specified base directory.
- **Initialization**:
  ```python
  from tools import FileReaderTool
  tool = FileReaderTool(base_directory="/path/to/directory")
  ```
- **Example**:
  ```python
  content = tool.forward(file_name="script.py")
  print(content)  # Prints the content of script.py
  ```

## Configuration

- **Base Directory**: Set the `base_directory` for `FileReaderTool` to the root folder containing your files (e.g., `/path/to/your/project`).
- **GitHub Credentials**: Update `GITHUB_USERNAME` and `GITHUB_TOKEN` in `GitPushCodeTool` or use environment variables:
  ```python
  import os
  GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
  GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
  ```
- **Groq API Key**: Provide your Groq API key to `StreamlitCodeGenerator` either directly or via an environment variable.

## Examples

### End-to-End Workflow
1. **Create a File**:
   ```python
   code_tool = CodeFileTool()
   code_tool.forward(filename="app.py", code="import streamlit as st\nst.write('Hello')", mode="create")
   ```

2. **Read the File**:
   ```python
   reader_tool = FileReaderTool(base_directory="/content/Repo/automated_coading_4")
   content = reader_tool.forward(file_name="app.py")
   print(content)
   ```

3. **Push to GitHub**:
   ```python
   git_tool = GitPushCodeTool()
   git_tool.forward(commit_message="Add Streamlit app")
   ```

4. **Generate a New Streamlit App**:
   ```python
   streamlit_tool = StreamlitCodeGenerator(api_key="your_groq_api_key")
   new_code = streamlit_tool.forward(prompt="Create a Streamlit app with a chart")
   print(new_code)
   ```

## Dependencies

- **Python**: 3.8+
- **Required Packages**:
  ```plaintext
  smolagents
  gitpython
  requests
  groq
  pathlib
  ```
  Install with:
  ```bash
  pip install smolagents gitpython requests groq
  ```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-tool`).
3. Commit your changes (`git commit -m "Add new tool"`).
4. Push to the branch (`git push origin feature/new-tool`).
5. Open a pull request.

Please ensure your code follows PEP 8 style guidelines and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Notes
- **Placeholders**: Replace `your-username`, `your-repo-name`, and `your_groq_api_key` with actual values when deploying this README.
- **File Structure**: The README assumes tools are in a `tools` module (e.g., `tools.py`). Adjust import statements if your structure differs.
- **Spelling**: I corrected "Rwadme.md" to "README.md" and "forr thr filefor" to "for the entire application" in the title for clarity.
