# renderlab/math/exceptions.py

from renderlab.core.exceptions import RenderLabException

class MathError(RenderLabException):
    """Base exception for all mathematics-related errors."""
    pass

class DegenerateGeometryError(MathError):
    """Raised when geometric properties are invalid (e.g., zero-length vectors)."""
    pass

class MatrixInversionError(MathError):
    """Raised when attempting to invert a singular matrix."""
    pass