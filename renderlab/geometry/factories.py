# renderlab/geometry/factories.py

from renderlab.core.factories import AbstractFactory
from renderlab.math.models import Vector3
from .services import Sphere
from .interfaces import Intersectable

class GeometryFactory(AbstractFactory):
    """Factory for generating standard geometric primitives."""
    
    def create(self, **kwargs) -> Intersectable:
        shape_type = kwargs.get("type")
        if shape_type == "sphere":
            return self.create_sphere(
                center=kwargs.get("center", Vector3(0.0, 0.0, 0.0)),
                radius=kwargs.get("radius", 1.0)
            )
        raise ValueError(f"Unknown geometry type: {shape_type}")

    @staticmethod
    def create_sphere(center: Vector3, radius: float) -> Sphere:
        return Sphere(center, radius)