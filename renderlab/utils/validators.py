# renderlab/utils/validators.py

from pathlib import Path
from .exceptions import FileOperationError

class FileSystemValidator:
    """Validates file and directory paths."""
    
    @staticmethod
    def assert_file_exists(file_path: str) -> None:
        """Throws an error if the specified file does not exist."""
        path = Path(file_path)
        if not path.exists():
            raise FileOperationError(f"File not found: {file_path}")
        if not path.is_file():
            raise FileOperationError(f"Path exists but is not a file: {file_path}")

    @staticmethod
    def assert_valid_extension(file_path: str, expected_extension: str) -> None:
        """Ensures the file has the correct extension."""
        path = Path(file_path)
        if path.suffix.lower() != expected_extension.lower():
            raise FileOperationError(f"Expected extension '{expected_extension}', got '{path.suffix}'")