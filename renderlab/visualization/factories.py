# renderlab/visualization/factories.py

from renderlab.core.factories import AbstractFactory
from renderlab.math.models import Vector3
from .models import BaseOverlay, LineOverlay, TextOverlay

class OverlayFactory(AbstractFactory):
    """Factory for spinning up different visualization overlays."""
    
    def create(self, **kwargs) -> BaseOverlay:
        overlay_type = kwargs.get("type", "line")
        color = kwargs.get("color", Vector3(1.0, 0.0, 0.0))
        opacity = kwargs.get("opacity", 1.0)
        
        if overlay_type == "line":
            return LineOverlay(
                color=color,
                opacity=opacity,
                start_point=kwargs.get("start_point", Vector3(0.0, 0.0, 0.0)),
                end_point=kwargs.get("end_point", Vector3(1.0, 1.0, 1.0)),
                thickness=kwargs.get("thickness", 1.0)
            )
        elif overlay_type == "text":
            return TextOverlay(
                color=color,
                opacity=opacity,
                position=kwargs.get("position", Vector3(0.0, 0.0, 0.0)),
                text=kwargs.get("text", "Label"),
                font_size=kwargs.get("font_size", 12)
            )
            
        raise ValueError(f"Unknown overlay type: {overlay_type}")