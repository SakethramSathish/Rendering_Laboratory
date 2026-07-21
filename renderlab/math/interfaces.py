# renderlab/math/interfaces.py

from abc import ABC, abstractmethod
import numpy as np

class Transformable(ABC):
    """Interface for objects that can undergo 3D spatial transformations."""
    
    @abstractmethod
    def apply_transform(self, matrix: np.ndarray) -> None:
        """Applies a 4x4 transformation matrix to the object."""
        pass