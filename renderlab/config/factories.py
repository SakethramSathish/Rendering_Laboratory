# renderlab/config/factories.py

from renderlab.core.factories import AbstractFactory
from .models import AppConfig, UIConfig

class ConfigFactory(AbstractFactory):
    """Factory for generating default Application Configurations."""
    
    def create(self, **kwargs) -> AppConfig:
        profile = kwargs.get("profile", "default")
        
        if profile == "performance":
            return AppConfig(
                ui=UIConfig(theme="dark", show_performance_overlay=True, viewport_refresh_rate=30),
                default_render_backend="cpu",
                max_threads=8
            )
        elif profile == "educational":
            return AppConfig(
                ui=UIConfig(theme="light", show_performance_overlay=True, viewport_refresh_rate=60),
                default_render_backend="cpu",
                max_threads=2
            )
            
        # Default profile
        return AppConfig()