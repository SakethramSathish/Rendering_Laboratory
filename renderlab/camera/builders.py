from renderlab.core.builders import AbstractBuilder
from renderlab.math.models import Vector3
from .models import CameraConfig
from .services import PerspectiveCamera

class CameraBuilder(AbstractBuilder):
    """Fluent builder for constructing camera configurations easily."""

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._lookfrom = Vector3(0.0, 0.0, 0.0)
        self._lookat = Vector3(0.0, 0.0, -1.0)
        self._vup = Vector3(0.0, 1.0, 0.0)
        self._vfov = 90.0
        self._aspect_ratio = 16.0 / 9.0

    def set_position(self, x: float, y: float, z: float) -> 'CameraBuilder':
        self._lookfrom = Vector3(x, y, z)
        return self

    def look_at(self, x: float, y: float, z: float) -> 'CameraBuilder':
        self._lookat = Vector3(x, y, z)
        return self

    def set_fov(self, fov: float) -> 'CameraBuilder':
        self._vfov = fov
        return self

    def set_aspect_ratio(self, ratio: float) -> 'CameraBuilder':
        self._aspect_ratio = ratio
        return self

    def build(self) -> PerspectiveCamera:
        """Constructs and returns the configured PerspectiveCamera."""
        config = CameraConfig(
            lookfrom=self._lookfrom,
            lookat=self._lookat,
            vup=self._vup,
            vfov=self._vfov,
            aspect_ratio=self._aspect_ratio
        )
        return PerspectiveCamera(config)