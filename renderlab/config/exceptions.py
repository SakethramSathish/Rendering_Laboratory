# renderlab/config/exceptions.py

from renderlab.core.exceptions import RenderLabException

class ConfigError(RenderLabException):
    """Base exception for all configuration-related errors."""
    pass

class MissingConfigKeyError(ConfigError):
    """Raised when attempting to access a configuration key that does not exist."""
    pass

class InvalidConfigValueError(ConfigError):
    """Raised when a configuration value violates expected boundaries or types."""
    pass