# renderlab/core/builders.py

from abc import ABC, abstractmethod
from typing import Any

class AbstractBuilder(ABC):
    """Base interface for complex object builders."""
    
    @abstractmethod
    def reset(self) -> None:
        """Reset the builder to a blank state."""
        pass

    @abstractmethod
    def build(self) -> Any:
        """Return the fully constructed object."""
        pass