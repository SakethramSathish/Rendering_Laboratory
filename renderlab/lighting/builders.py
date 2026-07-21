# renderlab/lighting/builders.py

from renderlab.core.builders import AbstractBuilder
from renderlab.math.models import Vector3
from .interfaces import AbstractLight
from .factories import LightFactory

class LightBuilder(AbstractBuilder):
    """Fluent API for configuring and generating Light sources."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._type = "point"
        self._color = Vector3(1.0, 1.0, 1.0)
        self._intensity = 1.0
        self._position = Vector3(0.0, 0.0, 0.0)
        self._direction = Vector3(0.0, -1.0, 0.0)

    def with_type(self, light_type: str) -> 'LightBuilder':
        self._type = light_type
        return self

    def with_color(self, r: float, g: float, b: float) -> 'LightBuilder':
        self._color = Vector3(r, g, b)
        return self

    def with_intensity(self, intensity: float) -> 'LightBuilder':
        self._intensity = intensity
        return self

    def at_position(self, x: float, y: float, z: float) -> 'LightBuilder':
        self._position = Vector3(x, y, z)
        return self

    def with_direction(self, x: float, y: float, z: float) -> 'LightBuilder':
        self._direction = Vector3(x, y, z)
        return self

    def build(self) -> AbstractLight:
        """Constructs and returns the configured Light object."""
        return LightFactory().create(
            type=self._type,
            color=self._color,
            intensity=self._intensity,
            position=self._position,
            direction=self._direction
        )