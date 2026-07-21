# renderlab/serialization/exceptions.py

from renderlab.core.exceptions import RenderLabException

class SerializationError(RenderLabException):
    """Base exception for all serialization and deserialization errors."""
    pass

class UnsupportedFormatError(SerializationError):
    """Raised when attempting to save/load a file format the engine does not support."""
    pass

class CorruptedDataError(SerializationError):
    """Raised when the payload being deserialized is missing required schema keys."""
    pass