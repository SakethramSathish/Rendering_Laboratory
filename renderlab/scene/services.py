# renderlab/scene/services.py

from typing import List, Optional
from renderlab.math.models import Ray, Vector3
from renderlab.geometry.models import HitRecord
from renderlab.camera.interfaces import AbstractCamera
from .interfaces import AbstractScene
from .models import SceneNode, SceneState
from .validators import SceneValidator

class Scene(AbstractScene):
    """Concrete implementation of a renderable 3D environment."""
    
    def __init__(self, name: str = "New Scene"):
        self._state = SceneState(name=name)
        self._nodes: List[SceneNode] = []

    def add_node(self, node: SceneNode) -> None:
        SceneValidator.validate_node(node)
        self._nodes.append(node)

    def get_nodes(self) -> List[SceneNode]:
        return self._nodes

    def set_camera(self, camera: AbstractCamera) -> None:
        self._state.camera = camera

    def get_camera(self) -> AbstractCamera:
        SceneValidator.assert_camera_exists(self._state.camera)
        return self._state.camera

    def set_background_color(self, r: float, g: float, b: float) -> None:
        self._state.background_color = (r, g, b)

    def get_background(self, ray: Ray) -> tuple[float, float, float]:
        """Provides a simple gradient skybox based on ray direction."""
        unit_direction = ray.direction.normalize()
        t = 0.5 * (unit_direction.y + 1.0)
        
        # Linear interpolation between white and a sky blue color
        r = (1.0 - t) * 1.0 + t * 0.5
        g = (1.0 - t) * 1.0 + t * 0.7
        b = (1.0 - t) * 1.0 + t * 1.0
        return (r, g, b)

    def intersect(self, ray: Ray, t_min: float, t_max: float) -> Optional[HitRecord]:
        """Iterates over all scene nodes to find the closest geometry intersection."""
        hit_anything = None
        closest_so_far = t_max

        # Custom attribute added dynamically to HitRecord to track which material was hit
        for node in self._nodes:
            hit = node.geometry.intersect(ray, t_min, closest_so_far)
            if hit:
                closest_so_far = hit.t
                hit_anything = hit
                hit_anything.material = node.material  # Attach material for the renderer

        return hit_anything