# renderlab/camera/validators.py

from .exceptions import InvalidFieldOfViewError, InvalidAspectRatioError

class CameraValidator:
    """Validation utility for camera configurations."""
    
    @staticmethod
    def assert_valid_fov(vfov: float) -> None:
        """Ensures the vertical field of view is between 0 and 180 degrees."""
        if vfov <= 0.0 or vfov >= 180.0:
            raise InvalidFieldOfViewError(f"FOV must be between 0 and 180 degrees. Got {vfov}")

    @staticmethod
    def assert_valid_aspect_ratio(aspect_ratio: float) -> None:
        """Ensures the aspect ratio is strictly positive."""
        if aspect_ratio <= 0.0:
            raise InvalidAspectRatioError(f"Aspect ratio must be > 0. Got {aspect_ratio}")