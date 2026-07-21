# renderlab/logging/validators.py

import os
from .exceptions import LoggerConfigurationError
from .models import LogConfig

class LogValidator:
    """Validates logger configurations."""
    
    @staticmethod
    def validate_config(config: LogConfig) -> None:
        """Ensures that file paths are valid if file logging is enabled."""
        if config.log_to_file:
            if not config.file_path or config.file_path.isspace():
                raise LoggerConfigurationError("File logging is enabled but no file path was provided.")
            
            # Check if the directory exists or can be created
            directory = os.path.dirname(config.file_path)
            if directory and not os.path.exists(directory):
                raise LoggerConfigurationError(f"Log directory '{directory}' does not exist.")