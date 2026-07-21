# renderlab/lighting/exceptions.py

from renderlab.core.exceptions import RenderLabException

class LightingError(RenderLabException):
    """Base exception for all lighting-related errors."""
    pass

class InvalidLightIntensityError(LightingError):
    """Raised when a light source is given a negative intensity."""
    pass