# renderlab/geometry/interfaces.py

from abc import ABC, abstractmethod
from typing import Optional
from renderlab.math.models import Ray
from .models import HitRecord

class Intersectable(ABC):
    """Contract for any geometric object that a ray can intersect."""
    
    @abstractmethod
    def intersect(self, ray: Ray, t_min: float, t_max: float) -> Optional[HitRecord]:
        """
        Tests if a ray intersects the geometry.
        Returns a HitRecord if successful, or None if it misses.
        """
        pass