# renderlab/camera/factories.py

from renderlab.core.factories import AbstractFactory
from .interfaces import AbstractCamera
from .models import CameraConfig
from .services import PerspectiveCamera

class CameraFactory(AbstractFactory):
    """Factory for instantiating different camera types."""
    
    def create(self, **kwargs) -> AbstractCamera:
        camera_type = kwargs.get("type", "perspective")
        
        if camera_type == "perspective":
            config = kwargs.get("config")
            if not config:
                raise ValueError("CameraConfig is required to create a perspective camera.")
            return self.create_perspective(config)
            
        raise ValueError(f"Unknown camera type: {camera_type}")

    @staticmethod
    def create_perspective(config: CameraConfig) -> PerspectiveCamera:
        return PerspectiveCamera(config)