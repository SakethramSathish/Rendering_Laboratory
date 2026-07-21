# renderlab/visualization/interfaces.py

from abc import ABC, abstractmethod
from typing import List
from .models import BaseOverlay

class AbstractVisualizationManager(ABC):
    """Interface for managing and compiling educational overlays."""
    
    @abstractmethod
    def add_overlay(self, overlay: BaseOverlay) -> None:
        """Adds a new visual overlay to the current frame."""
        pass

    @abstractmethod
    def clear_overlays(self) -> None:
        """Removes all overlays."""
        pass

    @abstractmethod
    def get_overlays(self) -> List[BaseOverlay]:
        """Retrieves all active overlays for the GUI to render."""
        pass