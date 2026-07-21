# renderlab/logging/services.py

import logging
import sys
from .interfaces import AbstractLogger
from .models import LogConfig
from .validators import LogValidator

class RenderLabLogger(AbstractLogger):
    """Concrete logging service utilizing Python's built-in logging module."""
    
    def __init__(self, name: str, config: LogConfig):
        LogValidator.validate_config(config)
        
        self._logger = logging.getLogger(name)
        self._logger.setLevel(config.level.value)
        
        # Prevent adding multiple handlers if the logger already exists
        if not self._logger.handlers:
            formatter = logging.Formatter(config.format_string)
            
            if config.log_to_console:
                console_handler = logging.StreamHandler(sys.stdout)
                console_handler.setFormatter(formatter)
                self._logger.addHandler(console_handler)
                
            if config.log_to_file:
                file_handler = logging.FileHandler(config.file_path, mode='a')
                file_handler.setFormatter(formatter)
                self._logger.addHandler(file_handler)

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str) -> None:
        self._logger.error(message)

    def critical(self, message: str) -> None:
        self._logger.critical(message)