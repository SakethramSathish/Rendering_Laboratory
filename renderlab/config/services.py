# renderlab/config/services.py

from typing import Any
from .interfaces import AbstractConfigManager
from .models import AppConfig
from .validators import ConfigValidator
from .exceptions import MissingConfigKeyError

class ConfigManager(AbstractConfigManager):
    """Concrete service for managing the application's configuration state."""
    
    def __init__(self, initial_config: AppConfig = None):
        self._config = initial_config or AppConfig()
        ConfigValidator.validate_app_config(self._config)

    def get_config(self) -> AppConfig:
        return self._config

    def set_config(self, config: AppConfig) -> None:
        ConfigValidator.validate_app_config(config)
        self._config = config

    def get_value(self, key_path: str, default: Any = None) -> Any:
        """
        Retrieves a value using dot notation, e.g., 'ui.theme'.
        Raises MissingConfigKeyError if the path is invalid and no default is provided.
        """
        keys = key_path.split('.')
        current_obj = self._config

        for key in keys:
            if hasattr(current_obj, key):
                current_obj = getattr(current_obj, key)
            elif isinstance(current_obj, dict) and key in current_obj:
                current_obj = current_obj[key]
            else:
                if default is not None:
                    return default
                raise MissingConfigKeyError(f"Configuration key path '{key_path}' not found.")
                
        return current_obj