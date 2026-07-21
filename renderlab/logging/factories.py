# renderlab/logging/factories.py

from renderlab.core.factories import AbstractFactory
from .interfaces import AbstractLogger
from .services import RenderLabLogger
from .models import LogConfig

class LoggerFactory(AbstractFactory):
    """Factory for creating scoped loggers across the engine."""
    
    _global_config = LogConfig()
    
    @classmethod
    def set_global_config(cls, config: LogConfig) -> None:
        """Sets the baseline configuration for all subsequently created loggers."""
        cls._global_config = config

    def create(self, **kwargs) -> AbstractLogger:
        name = kwargs.get("name", "RenderLab")
        config = kwargs.get("config", self._global_config)
        return RenderLabLogger(name, config)