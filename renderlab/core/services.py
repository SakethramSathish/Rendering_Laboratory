from typing import List, Any
from .interfaces import Observable, Observer

class EventBus(Observable):
    """Centralized event dispatcher for decoupled subsystem communication."""

    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def register_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observer(self, event_type: str, event_data: Any = None) -> None:
        """Dispatches an event to all registered observers."""
        for observer in self._observers:
            observer.update(event_type, event_data)
