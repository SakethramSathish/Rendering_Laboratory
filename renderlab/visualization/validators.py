# renderlab/visualization/validators.py

from .exceptions import InvalidOverlayDataError
from .models import BaseOverlay, LineOverlay

class VisualizationValidator:
    """Validates overlay properties before they are processed."""
    
    @staticmethod
    def validate_overlay_base(overlay: BaseOverlay) -> None:
        """Ensures the base properties (like opacity) are valid."""
        if not (0.0 <= overlay.opacity <= 1.0):
            raise InvalidOverlayDataError(f"Opacity must be between 0.0 and 1.0. Got {overlay.opacity}")

    @staticmethod
    def validate_line_overlay(overlay: LineOverlay) -> None:
        """Ensures line-specific properties are valid."""
        VisualizationValidator.validate_overlay_base(overlay)
        if overlay.thickness <= 0.0:
            raise InvalidOverlayDataError(f"Line thickness must be strictly positive. Got {overlay.thickness}")