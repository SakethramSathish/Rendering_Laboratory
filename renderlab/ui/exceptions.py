# renderlab/ui/exceptions.py

from renderlab.core.exceptions import RenderLabException

class UIError(RenderLabException):
    """Base exception for all graphical user interface errors."""
    pass

class WidgetInitializationError(UIError):
    """Raised when a PySide6 widget fails to initialize or map to the domain."""
    pass

class LayoutConfigurationError(UIError):
    """Raised when the UI layout parameters are invalid."""
    pass