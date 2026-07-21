# renderlab/lighting/validators.py

from .exceptions import InvalidLightIntensityError
from renderlab.math.models import Vector3
from renderlab.materials.validators import MaterialValidator

class LightValidator:
    """Validation utility for light configurations."""
    
    @staticmethod
    def assert_valid_intensity(intensity: float) -> None:
        """Ensures light intensity is physically plausible (non-negative)."""
        if intensity < 0.0:
            raise InvalidLightIntensityError(f"Light intensity cannot be negative. Got {intensity}")

    @staticmethod
    def assert_valid_color(color: Vector3) -> None:
        """Ensures the light color is valid using the material albedo validator."""
        # Reusing the albedo validator as color constraints are mathematically identical [0.0 - 1.0]
        MaterialValidator.assert_valid_albedo(color)