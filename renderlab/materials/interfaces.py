# renderlab/materials/interfaces.py

from abc import ABC, abstractmethod
from typing import Optional, Tuple
from renderlab.math.models import Ray, Vector3
from renderlab.geometry.models import HitRecord

class Material(ABC):
    """Base interface for computing ray scattering interactions on surfaces."""
    
    @abstractmethod
    def scatter(self, ray_in: Ray, rec: HitRecord) -> Optional[Tuple[Vector3, Ray]]:
        """
        Computes the ray reflection/refraction path and attenuation.
        Returns a tuple of (attenuation_vector, scattered_ray) if scattered, 
        or None if the ray is absorbed.
        """
        pass