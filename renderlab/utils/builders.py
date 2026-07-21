# renderlab/utils/builders.py

from pathlib import Path
from renderlab.core.builders import AbstractBuilder

class PathBuilder(AbstractBuilder):
    """Fluent API for constructing safe, cross-platform file paths."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._components = []
        self._extension = ""

    def add_directory(self, dir_name: str) -> 'PathBuilder':
        """Appends a directory to the path."""
        self._components.append(dir_name)
        return self

    def set_filename(self, filename: str) -> 'PathBuilder':
        """Sets the base filename."""
        self._components.append(filename)
        return self

    def set_extension(self, extension: str) -> 'PathBuilder':
        """Sets the file extension (e.g., '.json'). Automatically adds the dot if missing."""
        if not extension.startswith('.'):
            extension = f".{extension}"
        self._extension = extension
        return self

    def build(self) -> str:
        """Constructs and returns the final path string."""
        if not self._components:
            return ""
            
        base_path = Path(*self._components)
        if self._extension:
            # If the filename already had an extension, replace it. Otherwise, add it.
            base_path = base_path.with_suffix(self._extension)
            
        return str(base_path)