from abc import ABC, abstractmethod
from typing import Any, Dict

class Serializable(ABC):
    """Interface for objects that can be serialized to and from dictionaries"""

    @abstractmethod
    def serialize(self) -> Dict[str, Any]:
        """Convert the object state to a dictionary"""
        pass

    @classmethod
    @abstractmethod
    def deserialize(cls, data: Dict[str, Any]) -> 'Serializable':
        """Reconstruct the object from a dictionary"""
        pass

class Cloneable(ABC):
    """Interface for objects that support deep copying/cloning"""

    @abstractmethod
    def clone(self) -> 'Cloneable':
        """Return a deep copy of the object."""
        pass

class Observer(ABC):
    """Interface for an observer in the Observer pattern."""

    @abstractmethod
    def update(self, event_type: str, event_data: Any) -> None:
        """Called when the subject state changes."""
        pass

class Observable(ABC):
    """Interface for a subject in the Observer pattern."""

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self, event_type: str, event_data: Any) -> None:
        pass