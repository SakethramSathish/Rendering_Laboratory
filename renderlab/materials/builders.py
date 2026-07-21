# renderlab/materials/builders.py

from renderlab.core.builders import AbstractBuilder
from renderlab.math.models import Vector3
from .interfaces import Material
from .services import Lambertian, Metal

class MaterialBuilder(AbstractBuilder):
    """Fluent builder for creating parameterized surface materials."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._type = "lambertian"
        self._albedo = Vector3(0.5, 0.5, 0.5)
        self._roughness = 0.0

    def with_type(self, mat_type: str) -> 'MaterialBuilder':
        self._type = mat_type
        return self

    def with_albedo(self, r: float, g: float, b: float) -> 'MaterialBuilder':
        self._albedo = Vector3(r, g, b)
        return self

    def with_roughness(self, roughness: float) -> 'MaterialBuilder':
        self._roughness = roughness
        return self

    def build(self) -> Material:
        if self._type == "lambertian":
            return Lambertian(self._albedo)
        elif self._type == "metal":
            return Metal(self._albedo, self._roughness)
        raise ValueError(f"Invalid construction parameters for material type: {self._type}")