# renderlab/materials/factories.py

from renderlab.core.factories import AbstractFactory
from renderlab.math.models import Vector3
from .interfaces import Material
from .services import Lambertian, Metal

class MaterialFactory(AbstractFactory):
    """Factory for spinning up standard rendering engine materials."""
    
    def create(self, **kwargs) -> Material:
        mat_type = kwargs.get("type", "lambertian")
        albedo = kwargs.get("albedo", Vector3(0.5, 0.5, 0.5))
        
        if mat_type == "lambertian":
            return Lambertian(albedo)
        elif mat_type == "metal":
            roughness = kwargs.get("roughness", 0.0)
            return Metal(albedo, roughness)
            
        raise ValueError(f"Unknown or unsupported material type: {mat_type}")