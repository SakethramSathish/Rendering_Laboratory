# renderlab/camera/interfaces.py

from abc import ABC, abstractmethod
from renderlab.math.models import Ray

class AbstractCamera(ABC):
    """Base interface for all camera implementations."""
    
    @abstractmethod
    def get_ray(self, u: float, v: float) -> Ray:
        """
        Generates a 3D ray from the camera given 2D normalized viewport coordinates.
        u: Horizontal coordinate (0.0 to 1.0)
        v: Vertical coordinate (0.0 to 1.0)
        """
        pass