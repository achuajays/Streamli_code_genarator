from smolagents import Tool
from pathlib import Path

class FileReaderTool(Tool):
    name = "file_reader"
    description = "Reads the content of a file in the specified base directory."

    inputs = {
        "file_name": {
            "type": "string",
            "description": "File name to read, relative to the base directory."
        }
    }
    output_type = "string"

    def __init__(self, base_directory: str, **kwargs):
        super().__init__(**kwargs)
        self.base_directory = Path(base_directory).resolve()

    def forward(self, file_name: str):
        if Path(file_name).is_absolute():
            return "Error: file_name must be relative."

        file_path = (self.base_directory / file_name).resolve()
        if self.base_directory not in file_path.parents:
            return f"Error: '{file_name}' is outside base directory."

        try:
            return file_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            return f"Error: '{file_name}' not found in '{self.base_directory}'."
        except Exception as e:
            return f"Error reading '{file_name}': {str(e)}"