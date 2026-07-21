# renderlab/utils/models.py

from dataclasses import dataclass
from pathlib import Path

@dataclass
class FileMetadata:
    """Contains information about a file used by the engine."""
    file_path: Path
    exists: bool
    extension: str
    size_bytes: int = 0