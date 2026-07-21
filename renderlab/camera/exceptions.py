# renderlab/camera/exceptions.py

from renderlab.core.exceptions import RenderLabException

class CameraError(RenderLabException):
    """Base exception for all camera-related errors."""
    pass

class InvalidFieldOfViewError(CameraError):
    """Raised when the field of view is outside physically plausible bounds."""
    pass

class InvalidAspectRatioError(CameraError):
    """Raised when the aspect ratio is zero or negative."""
    pass