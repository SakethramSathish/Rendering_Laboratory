# renderlab/visualization/services.py

from typing import List
from .interfaces import AbstractVisualizationManager
from .models import BaseOverlay, LineOverlay, TextOverlay
from .validators import VisualizationValidator

class VisualizationManager(AbstractVisualizationManager):
    """Concrete service for managing active educational overlays."""
    
    def __init__(self):
        self._overlays: List[BaseOverlay] = []

    def add_overlay(self, overlay: BaseOverlay) -> None:
        # Perform specific validation based on the overlay type
        if isinstance(overlay, LineOverlay):
            VisualizationValidator.validate_line_overlay(overlay)
        else:
            VisualizationValidator.validate_overlay_base(overlay)
            
        self._overlays.append(overlay)

    def clear_overlays(self) -> None:
        self._overlays.clear()

    def get_overlays(self) -> List[BaseOverlay]:
        """Returns the list of overlays. The GUI layer will map these 3D coords to 2D screen space."""
        return self._overlays