# renderlab/renderer/validators.py

from .exceptions import InvalidRenderSettingsError
from .models import RenderSettings

class RendererValidator:
    """Validates rendering configuration to prevent runtime crashes."""
    
    @staticmethod
    def validate_settings(settings: RenderSettings) -> None:
        if settings.image_width <= 0 or settings.image_height <= 0:
            raise InvalidRenderSettingsError("Image dimensions must be strictly positive.")
        if settings.samples_per_pixel <= 0:
            raise InvalidRenderSettingsError("Samples per pixel must be at least 1.")
        if settings.max_depth < 0:
            raise InvalidRenderSettingsError("Maximum ray depth cannot be negative.")