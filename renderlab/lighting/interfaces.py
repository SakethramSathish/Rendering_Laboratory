# renderlab/lighting/interfaces.py

from abc import ABC, abstractmethod
from typing import Tuple
from renderlab.math.models import Vector3

class AbstractLight(ABC):
    """Base interface for an analytical light source."""
    
    @abstractmethod
    def get_illumination(self, surface_point: Vector3) -> Tuple[Vector3, Vector3, float]:
        """
        Calculates the illumination provided by this light at a specific point.
        Returns a tuple containing:
        - The direction vector FROM the surface TO the light.
        - The color/intensity (radiance) arriving at the surface.
        - The distance to the light (useful for shadow rays).
        """
        pass