# renderlab/renderer/factories.py

from renderlab.core.factories import AbstractFactory
from .interfaces import AbstractRenderer
from .services import CPURenderer

class RendererFactory(AbstractFactory):
    """Instantiates the required rendering engine."""
    
    def create(self, **kwargs) -> AbstractRenderer:
        backend = kwargs.get("backend", "cpu")
        
        if backend == "cpu":
            return CPURenderer()
            
        raise ValueError(f"Rendering backend '{backend}' is not supported.")