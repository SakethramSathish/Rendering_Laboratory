# renderlab/visualization/models.py

from dataclasses import dataclass
from renderlab.math.models import Vector3
from renderlab.core.models import Entity

@dataclass
class BaseOverlay(Entity):
    """Base data container for a visualization overlay."""
    color: Vector3 = Vector3(1.0, 0.0, 0.0)  # Default red for visibility
    opacity: float = 1.0

@dataclass
class LineOverlay(BaseOverlay):
    """Represents a 3D line, useful for drawing rays or normals."""
    start_point: Vector3 = Vector3(0.0, 0.0, 0.0)
    end_point: Vector3 = Vector3(1.0, 1.0, 1.0)
    thickness: float = 1.0

@dataclass
class TextOverlay(BaseOverlay):
    """Represents text rendered in 3D space, useful for labeling intersections."""
    position: Vector3 = Vector3(0.0, 0.0, 0.0)
    text: str = "Label"
    font_size: int = 12