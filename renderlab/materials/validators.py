from .exceptions import InvalidMaterialParameterError
from renderlab.math.models import Vector3

class MaterialValidator:
    """Validates physical constraints for material properties."""

    @staticmethod
    def assert_valid_roughness(roughness: float) -> None:
        """Ensures roughness stays within standard microfacet boundaries."""
        if not(0.0 <= roughness <= 1.0):
            raise InvalidMaterialParameterError(f"Roughness must fall within [0.0, 1.0]. Got {roughness}")
        
    @staticmethod
    def assert_valid_albedo(albedo: Vector3) -> None:
        """Ensures conservation of energy by checking albedo values."""
        for channel, val in [('R', albedo.x), ('G', albedo.y), ('B', albedo.z)]:
            if not (0.0 <= val <= 1.0):
                raise InvalidMaterialParameterError(f"Albedo channel {channel} must fall within [0.0, 1.0]. Got {val}")