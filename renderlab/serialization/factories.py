# renderlab/serialization/factories.py

from renderlab.core.factories import AbstractFactory
from .interfaces import AbstractSerializer
from .services import JSONSerializer, YAMLSerializer
from .exceptions import UnsupportedFormatError

class SerializerFactory(AbstractFactory):
    """Instantiates the appropriate serializer based on the desired format."""
    
    def create(self, **kwargs) -> AbstractSerializer:
        format_type = kwargs.get("format", "json").lower()
        
        if format_type in ("json", ".json"):
            return JSONSerializer()
        elif format_type in ("yaml", "yml", ".yaml", ".yml"):
            return YAMLSerializer()
            
        raise UnsupportedFormatError(f"Format '{format_type}' is not supported by the engine.")