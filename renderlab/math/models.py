import numpy as np
from dataclasses import dataclass
from renderlab.core.interfaces import Cloneable

@dataclass
class Vector3(Cloneable):
    """3D Vector representation wrapping a NumPy array for fast computation."""

    data: np.ndarray

    def __init__(self, x: float, y: float, z: float):
        self.data = np.array([x, y, z], dtype=np.float64)

    @property
    def x(self) -> float: return float(self.data[0])

    @property
    def y(self) -> float: return float(self.data[1])

    @property
    def z(self) -> float: return float(self.data[2])

    def magnitude(self) -> float:
        return float(np.linalg.norm(self.data))

    def normalize(self) -> 'Vector3':
        mag = self.magnitude()
        if mag == 0:
            return Vector3(0.0, 0.0, 0.0)
        norm_data = self.data / mag
        return Vector3(norm_data[0], norm_data[1], norm_data[2])
    
    def clone(self) -> 'Vector3':
        return Vector3(self.x, self.y, self.z)
    
@dataclass
class Ray:
    """Represents a mathematical ray with an origin and a normalized direction."""

    origin: Vector3
    direction: Vector3
    t_min: float = 0.001
    t_max: float = float('inf')

    def point_at(self, t: float) -> Vector3:
        """Calculates the 3D point along the ray at distance t."""
        p_data = self.origin.data + (self.direction.data * t)
        return Vector3(p_data[0], p_data[1], p_data[2])