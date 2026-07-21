# renderlab/scene/builders.py

from renderlab.core.builders import AbstractBuilder
from renderlab.geometry.interfaces import Intersectable
from renderlab.materials.interfaces import Material
from renderlab.camera.interfaces import AbstractCamera
from .services import Scene
from .factories import SceneFactory

class SceneBuilder(AbstractBuilder):
    """Fluent API for constructing a complete Scene."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._scene = SceneFactory().create()

    def with_name(self, name: str) -> 'SceneBuilder':
        self._scene._state.name = name
        return self

    def add_object(self, geometry: Intersectable, material: Material, name: str = "Object") -> 'SceneBuilder':
        node = SceneFactory.create_node(geometry, material, name)
        self._scene.add_node(node)
        return self

    def with_camera(self, camera: AbstractCamera) -> 'SceneBuilder':
        self._scene.set_camera(camera)
        return self

    def with_background(self, r: float, g: float, b: float) -> 'SceneBuilder':
        self._scene.set_background_color(r, g, b)
        return self

    def build(self) -> Scene:
        """Returns the fully constructed and validated Scene."""
        # Will throw if camera is missing, ensuring fail-fast behavior
        self._scene.get_camera() 
        return self._scene