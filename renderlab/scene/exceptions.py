# renderlab/scene/exceptions.py

from renderlab.core.exceptions import RenderLabException

class SceneError(RenderLabException):
    """Base exception for all scene-related errors."""
    pass

class InvalidSceneNodeError(SceneError):
    """Raised when a scene node is missing required geometry or materials."""
    pass

class CameraNotSetError(SceneError):
    """Raised when attempting to render a scene without an active camera."""
    pass