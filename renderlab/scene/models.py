# renderlab/scene/models.py

from dataclasses import dataclass
from typing import Optional
from renderlab.core.models import Entity
from renderlab.geometry.interfaces import Intersectable
from renderlab.materials.interfaces import Material
from renderlab.camera.interfaces import AbstractCamera

@dataclass(kw_only=True)
class SceneNode(Entity):
    """A single object in the scene combining geometry and material."""
    geometry: Intersectable
    material: Material

@dataclass
class SceneState:
    """Pure data container holding the current state of a scene."""
    name: str = "Default Scene"
    camera: Optional[AbstractCamera] = None
    background_color: tuple[float, float, float] = (0.0, 0.0, 0.0)