# renderlab/lighting/services.py

from typing import Tuple
from renderlab.math.models import Vector3
from .interfaces import AbstractLight
from .models import PointLightData, DirectionalLightData
from .validators import LightValidator

class PointLight(AbstractLight):
    """An omnidirectional light emitting from a single 3D point."""
    
    def __init__(self, data: PointLightData):
        LightValidator.assert_valid_intensity(data.base_data.intensity)
        LightValidator.assert_valid_color(data.base_data.color)
        self._data = data

    def get_illumination(self, surface_point: Vector3) -> Tuple[Vector3, Vector3, float]:
        # Vector from surface to light
        direction_data = self._data.position.data - surface_point.data
        direction = Vector3(direction_data[0], direction_data[1], direction_data[2])
        
        distance = direction.magnitude()
        
        if distance == 0:
            return Vector3(0.0, 1.0, 0.0), Vector3(0.0, 0.0, 0.0), 0.0
            
        norm_direction = direction.normalize()
        
        # Inverse-square law for light falloff
        attenuation = 1.0 / (distance * distance)
        radiance_data = self._data.base_data.color.data * self._data.base_data.intensity * attenuation
        radiance = Vector3(radiance_data[0], radiance_data[1], radiance_data[2])
        
        return norm_direction, radiance, distance

class DirectionalLight(AbstractLight):
    """An infinitely far light source emitting parallel rays (e.g., the Sun)."""
    
    def __init__(self, data: DirectionalLightData):
        LightValidator.assert_valid_intensity(data.base_data.intensity)
        LightValidator.assert_valid_color(data.base_data.color)
        # Ensure direction is normalized upon creation
        self._data = data
        self._data.direction = self._data.direction.normalize()

    def get_illumination(self, surface_point: Vector3) -> Tuple[Vector3, Vector3, float]:
        # Direction is inverted because we want the vector pointing TOWARDS the light
        inv_dir = Vector3(-self._data.direction.x, -self._data.direction.y, -self._data.direction.z)
        
        # Radiance does not attenuate based on distance for a directional light
        radiance_data = self._data.base_data.color.data * self._data.base_data.intensity
        radiance = Vector3(radiance_data[0], radiance_data[1], radiance_data[2])
        
        # Distance is technically infinite
        return inv_dir, radiance, float('inf')