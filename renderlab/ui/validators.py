# renderlab/ui/validators.py

from .exceptions import LayoutConfigurationError
from .models import WindowConfig

class UIValidator:
    """Validation utility for UI configurations."""
    
    @staticmethod
    def assert_valid_dimensions(config: WindowConfig) -> None:
        """Ensures window dimensions are strictly positive and reasonable."""
        if config.width < 400 or config.height < 300:
            raise LayoutConfigurationError(
                f"Window dimensions too small (W:{config.width}, H:{config.height}). "
                "Minimum is 400x300."
            )