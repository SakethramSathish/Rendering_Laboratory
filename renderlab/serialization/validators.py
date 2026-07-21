# renderlab/serialization/validators.py

from typing import Dict, Any
from .exceptions import CorruptedDataError

class SchemaValidator:
    """Validates the structure of deserialized data."""
    
    @staticmethod
    def validate_payload_wrapper(payload: Dict[str, Any]) -> None:
        """Ensures the loaded dictionary contains the required RenderLab metadata."""
        if "__renderlab_version__" not in payload:
            raise CorruptedDataError("Payload is missing version metadata.")
        if "__entity_type__" not in payload:
            raise CorruptedDataError("Payload is missing entity type metadata.")
        if "data" not in payload:
            raise CorruptedDataError("Payload is missing the core data block.")