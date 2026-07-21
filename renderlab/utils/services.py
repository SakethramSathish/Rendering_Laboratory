# renderlab/utils/services.py

import os
import random
import numpy as np
from pathlib import Path
from .interfaces import AbstractFileSystem
from .models import FileMetadata
from .validators import FileSystemValidator
from .exceptions import FileOperationError

class OSFileSystem(AbstractFileSystem):
    """Concrete implementation of the file system interface using the OS."""
    
    def read_text(self, file_path: str) -> str:
        FileSystemValidator.assert_file_exists(file_path)
        try:
            return Path(file_path).read_text(encoding="utf-8")
        except IOError as e:
            raise FileOperationError(f"Failed to read file {file_path}: {str(e)}")

    def write_text(self, file_path: str, content: str) -> None:
        path = Path(file_path)
        # Ensure parent directories exist
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            path.write_text(content, encoding="utf-8")
        except IOError as e:
            raise FileOperationError(f"Failed to write file {file_path}: {str(e)}")

    def get_metadata(self, file_path: str) -> FileMetadata:
        path = Path(file_path)
        exists = path.exists()
        size = path.stat().st_size if exists and path.is_file() else 0
        
        return FileMetadata(
            file_path=path,
            exists=exists,
            extension=path.suffix.lower(),
            size_bytes=size
        )

class Randomizer:
    """Utility for controlling random seeds to ensure reproducible renders."""
    
    @staticmethod
    def set_seed(seed: int) -> None:
        """Locks the global random state for both standard Python and NumPy."""
        random.seed(seed)
        np.random.seed(seed)