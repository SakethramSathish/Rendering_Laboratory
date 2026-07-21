# renderlab/geometry/exceptions.py

from renderlab.core.exceptions import RenderLabException

class GeometryError(RenderLabException):
    """Base exception for all geometry-related errors."""
    pass

class InvalidPrimitiveError(GeometryError):
    """Raised when a primitive is defined with invalid parameters (e.g., negative radius)."""
    pass

class MeshConstructionError(GeometryError):
    """Raised when a polygon mesh fails to build (e.g., mismatched vertices and indices)."""
    pass