# renderlab/scene/interfaces.py

from abc import abstractmethod
from typing import List, Optional
from renderlab.geometry.interfaces import Intersectable
from renderlab.geometry.models import HitRecord
from renderlab.math.models import Ray
from renderlab.camera.interfaces import AbstractCamera
from .models import SceneNode

class AbstractScene(Intersectable):
    """Base interface for a renderable scene."""
    
    @abstractmethod
    def add_node(self, node: SceneNode) -> None:
        pass

    @abstractmethod
    def get_nodes(self) -> List[SceneNode]:
        pass

    @abstractmethod
    def set_camera(self, camera: AbstractCamera) -> None:
        pass
        
    @abstractmethod
    def get_camera(self) -> AbstractCamera:
        pass

    @abstractmethod
    def get_background(self, ray: Ray) -> tuple[float, float, float]:
        """Calculates the background color for a ray that hits nothing."""
        pass