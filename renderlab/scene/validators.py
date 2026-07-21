# renderlab/scene/validators.py

from .exceptions import InvalidSceneNodeError, CameraNotSetError
from .models import SceneNode
from renderlab.camera.interfaces import AbstractCamera

class SceneValidator:
    """Validation utility for scene integrity."""
    
    @staticmethod
    def validate_node(node: SceneNode) -> None:
        """Ensures a node has valid geometry and material attached."""
        if not node.geometry:
            raise InvalidSceneNodeError(f"Node '{node.name}' is missing geometry.")
        if not node.material:
            raise InvalidSceneNodeError(f"Node '{node.name}' is missing a material.")

    @staticmethod
    def assert_camera_exists(camera: AbstractCamera) -> None:
        """Throws an error if the scene lacks a camera during render initialization."""
        if not camera:
            raise CameraNotSetError("The scene requires an active camera to be rendered.")