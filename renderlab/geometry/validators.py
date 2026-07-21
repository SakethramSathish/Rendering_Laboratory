# renderlab/geometry/validators.py

from .exceptions import InvalidPrimitiveError

class GeometryValidator:
    """Validates parameters for geometric primitives."""
    
    @staticmethod
    def assert_positive_radius(radius: float) -> None:
        """Ensures a radius is strictly positive."""
        if radius <= 0:
            raise InvalidPrimitiveError(f"Radius must be > 0. Got {radius}")