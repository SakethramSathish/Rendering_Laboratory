# renderlab/visualization/builders.py

from typing import List
from renderlab.core.builders import AbstractBuilder
from renderlab.math.models import Vector3, Ray
from .models import BaseOverlay
from .factories import OverlayFactory

class RayVisualizationBuilder(AbstractBuilder):
    """Fluent API for building a sequence of overlays to visualize a ray path."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._overlays: List[BaseOverlay] = []
        self._factory = OverlayFactory()

    def add_ray_segment(self, start: Vector3, end: Vector3, color: Vector3 = Vector3(1.0, 1.0, 0.0)) -> 'RayVisualizationBuilder':
        """Adds a line segment representing a ray traveling through space."""
        line = self._factory.create(
            type="line",
            start_point=start,
            end_point=end,
            color=color,
            thickness=2.0
        )
        self._overlays.append(line)
        return self

    def add_intersection_label(self, point: Vector3, text: str = "Hit") -> 'RayVisualizationBuilder':
        """Adds a text label at the point of intersection."""
        label = self._factory.create(
            type="text",
            position=point,
            text=text,
            color=Vector3(1.0, 1.0, 1.0)
        )
        self._overlays.append(label)
        return self

    def build(self) -> List[BaseOverlay]:
        """Returns the compiled list of overlays representing the ray path."""
        return self._overlays