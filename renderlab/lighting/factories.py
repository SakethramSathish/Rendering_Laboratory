# renderlab/lighting/factories.py

from renderlab.core.factories import AbstractFactory
from renderlab.math.models import Vector3
from .interfaces import AbstractLight
from .models import LightData, PointLightData, DirectionalLightData
from .services import PointLight, DirectionalLight

class LightFactory(AbstractFactory):
    """Factory for instantiating analytical light sources."""
    
    def create(self, **kwargs) -> AbstractLight:
        light_type = kwargs.get("type", "point")
        color = kwargs.get("color", Vector3(1.0, 1.0, 1.0))
        intensity = kwargs.get("intensity", 1.0)
        
        base_data = LightData(color=color, intensity=intensity)
        
        if light_type == "point":
            position = kwargs.get("position", Vector3(0.0, 0.0, 0.0))
            data = PointLightData(position=position, base_data=base_data)
            return PointLight(data)
            
        elif light_type == "directional":
            direction = kwargs.get("direction", Vector3(0.0, -1.0, 0.0))
            data = DirectionalLightData(direction=direction, base_data=base_data)
            return DirectionalLight(data)
            
        raise ValueError(f"Unknown light type: {light_type}")