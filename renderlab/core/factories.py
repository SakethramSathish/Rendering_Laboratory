from abc import ABC, abstractmethod
from typing import Any

class AbstractFactory(ABC):
    """Base interface for object creation factories."""
    
    @abstractmethod
    def create(self, **kwargs: Any) -> Any:
        """Instantiate and return a new object based on keyword arguments."""
        pass