# renderlab/serialization/models.py

from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ExportPayload:
    """Standardized wrapper for all exported engine data."""
    version: str
    entity_type: str
    data: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "__renderlab_version__": self.version,
            "__entity_type__": self.entity_type,
            "data": self.data
        }