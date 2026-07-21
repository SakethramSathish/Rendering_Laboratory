# renderlab/visualization/exceptions.py

from renderlab.core.exceptions import RenderLabException

class VisualizationError(RenderLabException):
    """Base exception for visualization and overlay errors."""
    pass

class InvalidOverlayDataError(VisualizationError):
    """Raised when overlay data (e.g., coordinates, colors) is malformed."""
    pass