# renderlab/config/interfaces.py

from abc import ABC, abstractmethod
from typing import Any
from .models import AppConfig

class AbstractConfigManager(ABC):
    """Interface for managing and retrieving application settings."""
    
    @abstractmethod
    def get_config(self) -> AppConfig:
        """Returns the active configuration object."""
        pass

    @abstractmethod
    def set_config(self, config: AppConfig) -> None:
        """Overwrites the active configuration."""
        pass

    @abstractmethod
    def get_value(self, key_path: str, default: Any = None) -> Any:
        """Retrieves a specific value using a dot-notation path (e.g., 'ui.theme')."""
        pass