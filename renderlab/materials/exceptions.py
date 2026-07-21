# renderlab/materials/exceptions.py

from renderlab.core.exceptions import RenderLabException

class MaterialError(RenderLabException):
    """Base exception for all material and BRDF-related errors."""
    pass

class InvalidMaterialParameterError(MaterialError):
    """Raised when material coefficients (e.g., negative roughness) are invalid."""
    pass