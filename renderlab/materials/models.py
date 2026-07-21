# renderlab/materials/models.py

from dataclasses import dataclass
from renderlab.math.models import Vector3

@dataclass
class MaterialProperties:
    """Pure data container storing raw optical coefficients."""
    albedo: Vector3
    roughness: float = 0.0
    ior: float = 1.0  # Index of refraction