# renderlab/serialization/services.py

import json
import yaml
from typing import Dict, Any
from .interfaces import AbstractSerializer
from .exceptions import SerializationError

class JSONSerializer(AbstractSerializer):
    """Concrete serializer for the JSON format."""
    
    def dump_to_string(self, data: Dict[str, Any]) -> str:
        try:
            return json.dumps(data, indent=4)
        except TypeError as e:
            raise SerializationError(f"Failed to serialize to JSON: {str(e)}")

    def load_from_string(self, payload: str) -> Dict[str, Any]:
        try:
            return json.loads(payload)
        except json.JSONDecodeError as e:
            raise SerializationError(f"Failed to decode JSON: {str(e)}")

    def get_extension(self) -> str:
        return ".json"

class YAMLSerializer(AbstractSerializer):
    """Concrete serializer for the YAML format."""
    
    def dump_to_string(self, data: Dict[str, Any]) -> str:
        try:
            return yaml.dump(data, default_flow_style=False, sort_keys=False)
        except yaml.YAMLError as e:
            raise SerializationError(f"Failed to serialize to YAML: {str(e)}")

    def load_from_string(self, payload: str) -> Dict[str, Any]:
        try:
            return yaml.safe_load(payload) or {}
        except yaml.YAMLError as e:
            raise SerializationError(f"Failed to decode YAML: {str(e)}")

    def get_extension(self) -> str:
        return ".yaml"