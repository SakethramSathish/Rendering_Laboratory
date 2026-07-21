# renderlab/renderer/interfaces.py

from abc import ABC, abstractmethod
from renderlab.scene.interfaces import AbstractScene
from .models import RenderSettings, RenderResult

class AbstractRenderer(ABC):
    """Base interface for all rendering engines."""
    
    @abstractmethod
    def render(self, scene: AbstractScene, settings: RenderSettings) -> RenderResult:
        """Executes the rendering pipeline for the given scene."""
        pass

    @abstractmethod
    def abort(self) -> None:
        """Signals the renderer to safely halt the current job."""
        pass