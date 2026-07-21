# renderlab/logging/exceptions.py

from renderlab.core.exceptions import RenderLabException

class LoggingError(RenderLabException):
    """Base exception for all logging-related errors."""
    pass

class LoggerConfigurationError(LoggingError):
    """Raised when the logger is configured with an invalid file path or level."""
    pass