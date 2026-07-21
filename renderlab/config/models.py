# renderlab/config/models.py

from dataclasses import dataclass, field
from typing import Dict, Any
from renderlab.core.interfaces import Serializable

@dataclass
class UIConfig(Serializable):
    """Configuration settings specific to the presentation layer."""
    theme: str = "dark"
    show_performance_overlay: bool = True
    viewport_refresh_rate: int = 60

    def serialize(self) -> Dict[str, Any]:
        return {
            "theme": self.theme,
            "show_performance_overlay": self.show_performance_overlay,
            "viewport_refresh_rate": self.viewport_refresh_rate
        }

    @classmethod
    def deserialize(cls, data: Dict[str, Any]) -> 'UIConfig':
        return cls(
            theme=data.get("theme", "dark"),
            show_performance_overlay=data.get("show_performance_overlay", True),
            viewport_refresh_rate=data.get("viewport_refresh_rate", 60)
        )

@dataclass
class AppConfig(Serializable):
    """The root configuration object containing all subsystem settings."""
    ui: UIConfig = field(default_factory=UIConfig)
    default_render_backend: str = "cpu"
    max_threads: int = 4

    def serialize(self) -> Dict[str, Any]:
        return {
            "ui": self.ui.serialize(),
            "default_render_backend": self.default_render_backend,
            "max_threads": self.max_threads
        }

    @classmethod
    def deserialize(cls, data: Dict[str, Any]) -> 'AppConfig':
        return cls(
            ui=UIConfig.deserialize(data.get("ui", {})),
            default_render_backend=data.get("default_render_backend", "cpu"),
            max_threads=data.get("max_threads", 4)
        )