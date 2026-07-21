# renderlab/serialization/interfaces.py

from abc import ABC, abstractmethod
from typing import Any, Dict

class AbstractSerializer(ABC):
    """Interface for encoding and decoding domain objects."""
    
    @abstractmethod
    def dump_to_string(self, data: Dict[str, Any]) -> str:
        """Converts a Python dictionary into a formatted string."""
        pass

    @abstractmethod
    def load_from_string(self, payload: str) -> Dict[str, Any]:
        """Parses a formatted string back into a Python dictionary."""
        pass
        
    @abstractmethod
    def get_extension(self) -> str:
        """Returns the file extension associated with this serializer."""
        pass