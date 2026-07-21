# renderlab/logging/builders.py

from renderlab.core.builders import AbstractBuilder
from .models import LogConfig, LogLevel
from .interfaces import AbstractLogger
from .factories import LoggerFactory

class LoggerBuilder(AbstractBuilder):
    """Fluent API for configuring engine loggers."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._name = "RenderLab"
        self._config = LogConfig()

    def with_name(self, name: str) -> 'LoggerBuilder':
        self._name = name
        return self

    def set_level(self, level: LogLevel) -> 'LoggerBuilder':
        self._config.level = level
        return self

    def enable_console(self, enabled: bool) -> 'LoggerBuilder':
        self._config.log_to_console = enabled
        return self

    def enable_file(self, file_path: str) -> 'LoggerBuilder':
        self._config.log_to_file = True
        self._config.file_path = file_path
        return self

    def build(self) -> AbstractLogger:
        """Constructs and returns the configured logger."""
        factory = LoggerFactory()
        return factory.create(name=self._name, config=self._config)