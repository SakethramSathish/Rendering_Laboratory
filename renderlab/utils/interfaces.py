# renderlab/utils/interfaces.py

from abc import ABC, abstractmethod
from typing import Optional
from .models import FileMetadata

class AbstractFileSystem(ABC):
    """Interface for abstracting OS-level file operations."""
    
    @abstractmethod
    def read_text(self, file_path: str) -> str:
        """Reads a file and returns its text content."""
        pass

    @abstractmethod
    def write_text(self, file_path: str, content: str) -> None:
        """Writes text content to a file."""
        pass

    @abstractmethod
    def get_metadata(self, file_path: str) -> FileMetadata:
        """Retrieves metadata about a file."""
        pass