# renderlab/config/validators.py

from .exceptions import InvalidConfigValueError
from .models import AppConfig

class ConfigValidator:
    """Validates application configuration data."""
    
    @staticmethod
    def validate_app_config(config: AppConfig) -> None:
        if config.max_threads < 1:
            raise InvalidConfigValueError(f"max_threads must be at least 1. Got {config.max_threads}")
        
        if config.ui.viewport_refresh_rate < 1:
            raise InvalidConfigValueError(f"viewport_refresh_rate must be at least 1. Got {config.ui.viewport_refresh_rate}")
            
        allowed_themes = ["dark", "light", "system"]
        if config.ui.theme not in allowed_themes:
            raise InvalidConfigValueError(f"Theme must be one of {allowed_themes}. Got '{config.ui.theme}'")