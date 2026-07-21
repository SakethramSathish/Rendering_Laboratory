# renderlab/lighting/models.py

from dataclasses import dataclass
from renderlab.math.models import Vector3
from renderlab.core.models import Entity

@dataclass
class LightData:
    """Core properties shared by all light sources."""
    color: Vector3
    intensity: float = 1.0

@dataclass
class PointLightData(Entity):
    """Data specifically for a point light source."""
    position: Vector3
    base_data: LightData

@dataclass
class DirectionalLightData(Entity):
    """Data specifically for an infinite directional light."""
    direction: Vector3
    base_data: LightData