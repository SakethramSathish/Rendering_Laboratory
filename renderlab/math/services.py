import numpy as np
from .models import Vector3
from .exceptions import MatrixInversionError

class MathService:
    """Stateless utility for common 3D graphics math operations."""

    @staticmethod
    def dot_product(v1: Vector3, v2: Vector3) -> float:
        return float(np.dot(v1.data, v2.data))
    
    @staticmethod
    def cross_product(v1: Vector3, v2: Vector3) -> Vector3:
        result = np.cross(v1.data, v2.data)
        return Vector3(result[0], result[1], result[2])
    
    @staticmethod
    def reflect(incident: Vector3, normal: Vector3) -> Vector3:
        """Calculates the reflection vector."""
        i = incident.data
        n = normal.data
        r = i - 2.0 * np.dot(i, n) * n
        return Vector3(r[0], r[1], r[2])
    
    @staticmethod
    def invert_matrix(matrix: np.ndarray) -> np.ndarray:
        """Inverts a 4x4 matrix, raising an engine-specific error on failure."""
        try:
            return np.linalg.inv(matrix)
        except:
            raise MatrixInversionError("Cannot invert singular matrix.")