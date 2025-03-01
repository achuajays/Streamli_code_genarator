from smolagents import Tool
from pathlib import Path

class CodeFileTool(Tool):
    name = "code_file_tool"
    description = "Creates or appends code to files within a base directory."

    inputs = {
        "filename": {"type": "string", "description": "File name relative to base directory."},
        "code": {"type": "string", "description": "Code to add to the file."},
        "mode": {"type": "string", "description": "'create' or 'append' mode."}
    }
    output_type = "string"

    def __init__(self, base_directory: str, **kwargs):
        super().__init__(**kwargs)
        self.base_directory = Path(base_directory).resolve()

    def forward(self, filename: str, code: str, mode: str):
        file_path = self.base_directory / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)

        mode = mode.lower()
        if mode == "create":
            try:
                with file_path.open("x") as f:
                    f.write(code)
                return f"File '{filename}' created."
            except FileExistsError:
                return f"Error: '{filename}' already exists."
            except Exception as e:
                return f"Error: {str(e)}"
        elif mode == "append":
            try:
                with file_path.open("a") as f:
                    f.write(code)
                return f"Code appended to '{filename}'."
            except Exception as e:
                return f"Error: {str(e)}"
        else:
            return "Error: Mode must be 'create' or 'append'."