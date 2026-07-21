class RenderLabException(Exception):
    """Base exception for all RenderLab Engine errors."""
    pass

class ConfigurationError(RenderLabException):
    """Raised when there is a configuration or parameter issue."""
    pass

class InitializationError(RenderLabException):
    """Raised when a subsystem fails to initialize correctly."""
    pass

class ValidationFailedError(RenderLabException):
    """Raised when domain entity validation fails."""
    pass
