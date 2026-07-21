# renderlab/serialization/builders.py

from typing import Dict, Any
from renderlab.core.builders import AbstractBuilder
from renderlab.core.interfaces import Serializable
from .models import ExportPayload

class PayloadBuilder(AbstractBuilder):
    """Fluent API for safely constructing versioned export payloads."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._version = "1.0.0"
        self._entity_type = "Unknown"
        self._data: Dict[str, Any] = {}

    def set_version(self, version: str) -> 'PayloadBuilder':
        self._version = version
        return self

    def set_entity_type(self, entity_type: str) -> 'PayloadBuilder':
        self._entity_type = entity_type
        return self

    def extract_from(self, obj: Serializable) -> 'PayloadBuilder':
        """Automatically calls the entity's own serialize() method."""
        self._entity_type = obj.__class__.__name__
        self._data = obj.serialize()
        return self
        
    def set_raw_data(self, data: Dict[str, Any]) -> 'PayloadBuilder':
        self._data = data
        return self

    def build(self) -> ExportPayload:
        """Returns the fully constructed metadata payload wrapper."""
        return ExportPayload(
            version=self._version,
            entity_type=self._entity_type,
            data=self._data
        )