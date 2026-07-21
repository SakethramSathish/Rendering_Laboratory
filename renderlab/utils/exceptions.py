# renderlab/utils/exceptions.py

from renderlab.core.exceptions import RenderLabException

class UtilityError(RenderLabException):
    """Base exception for all utility-related errors."""
    pass

class FileOperationError(UtilityError):
    """Raised when a file system operation (like reading or writing) fails."""
    pass