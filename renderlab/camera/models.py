from dataclasses import dataclass
from renderlab.math.models import Vector3

@dataclass
class CameraConfig:
    """Data object holding all configuration parameters for a camera."""

    lookfrom: Vector3
    lookat: Vector3
    vup: Vector3
    vfov: float         # Vertical Field of View in degrees
    aspect_ratio: float # Width / Height
    aperture: float = 0.0
    focus_dist: float = 1.0