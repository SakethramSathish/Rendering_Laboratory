# renderlab/ui/models.py

from dataclasses import dataclass

@dataclass
class WindowConfig:
    """Configuration parameters for the main application window."""
    title: str = "RenderLab Engine"
    width: int = 1280
    height: int = 720
    is_maximized: bool = False
    stylesheet_path: str = ""

@dataclass
class ViewportState:
    """Holds the transient state of the rendering viewport."""
    is_rendering: bool = False
    current_fps: float = 0.0
    zoom_level: float = 1.0