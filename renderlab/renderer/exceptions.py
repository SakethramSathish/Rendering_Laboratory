# renderlab/renderer/exceptions.py

from renderlab.core.exceptions import RenderLabException

class RendererError(RenderLabException):
    """Base exception for all rendering-related errors."""
    pass

class RenderAbortedError(RendererError):
    """Raised when a rendering process is manually stopped by the user."""
    pass

class InvalidRenderSettingsError(RendererError):
    """Raised when rendering parameters (e.g., negative resolution) are invalid."""
    pass