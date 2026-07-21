# renderlab/config/builders.py

from renderlab.core.builders import AbstractBuilder
from .models import AppConfig, UIConfig

class ConfigBuilder(AbstractBuilder):
    """Fluent API for building custom application configurations."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._config = AppConfig()

    def with_theme(self, theme: str) -> 'ConfigBuilder':
        self._config.ui.theme = theme
        return self

    def toggle_performance_overlay(self, show: bool) -> 'ConfigBuilder':
        self._config.ui.show_performance_overlay = show
        return self

    def with_refresh_rate(self, hz: int) -> 'ConfigBuilder':
        self._config.ui.viewport_refresh_rate = hz
        return self

    def with_max_threads(self, threads: int) -> 'ConfigBuilder':
        self._config.max_threads = threads
        return self

    def build(self) -> AppConfig:
        """Returns the constructed AppConfig."""
        from .validators import ConfigValidator
        ConfigValidator.validate_app_config(self._config)
        return self._config