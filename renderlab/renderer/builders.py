# renderlab/renderer/builders.py

from renderlab.core.builders import AbstractBuilder
from .models import RenderSettings
from .interfaces import AbstractRenderer
from .factories import RendererFactory

class RendererBuilder(AbstractBuilder):
    """Fluent API for configuring and generating a Renderer."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._settings = RenderSettings()
        self._backend = "cpu"

    def set_resolution(self, width: int, height: int) -> 'RendererBuilder':
        self._settings.image_width = width
        self._settings.image_height = height
        return self

    def set_samples(self, samples: int) -> 'RendererBuilder':
        self._settings.samples_per_pixel = samples
        return self

    def set_max_depth(self, depth: int) -> 'RendererBuilder':
        self._settings.max_depth = depth
        return self
        
    def get_settings(self) -> RenderSettings:
        return self._settings

    def build(self) -> AbstractRenderer:
        """Creates the renderer configured with the specified backend."""
        return RendererFactory().create(backend=self._backend)