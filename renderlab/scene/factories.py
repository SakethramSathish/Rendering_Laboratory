# renderlab/scene/factories.py

from renderlab.core.factories import AbstractFactory
from renderlab.geometry.interfaces import Intersectable
from renderlab.materials.interfaces import Material
from .models import SceneNode
from .services import Scene

class SceneFactory(AbstractFactory):
    """Factory for creating scenes and scene elements."""
    
    def create(self, **kwargs) -> Scene:
        name = kwargs.get("name", "Generated Scene")
        return Scene(name=name)

    @staticmethod
    def create_node(geometry: Intersectable, material: Material, name: str = "Node") -> SceneNode:
        return SceneNode(name=name, geometry=geometry, material=material)