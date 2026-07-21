# renderlab/math/validators.py

import numpy as np
from .models import Vector3
from .exceptions import DegenerateGeometryError

class MathValidator:
    """Validation utilities for mathematical structures."""
    
    @staticmethod
    def assert_normalized(vector: Vector3, tolerance: float = 1e-5) -> None:
        """Throws an error if a vector is not normalized."""
        mag = vector.magnitude()
        if abs(mag - 1.0) > tolerance:
            raise DegenerateGeometryError(f"Vector is not normalized (magnitude={mag}).")

    @staticmethod
    def assert_no_nans(vector: Vector3) -> None:
        """Throws an error if a vector contains NaN values."""
        if np.isnan(vector.data).any():
            raise DegenerateGeometryError("Vector contains NaN values.")