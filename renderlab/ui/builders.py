# renderlab/ui/builders.py

from renderlab.core.builders import AbstractBuilder
from .models import WindowConfig
from .interfaces import AbstractMainWindow
from .factories import UIFactory

class MainWindowBuilder(AbstractBuilder):
    """Fluent API for constructing the desktop application window."""
    
    def __init__(self):
        self.reset()
        
    def reset(self) -> None:
        self._config = WindowConfig()
        self._factory = UIFactory()
        # Ensure Qt app is initialized before building widgets
        self._factory.get_qapplication()

    def set_title(self, title: str) -> 'MainWindowBuilder':
        self._config.title = title
        return self

    def set_resolution(self, width: int, height: int) -> 'MainWindowBuilder':
        self._config.width = width
        self._config.height = height
        return self

    def set_maximized(self, maximized: bool = True) -> 'MainWindowBuilder':
        self._config.is_maximized = maximized
        return self

    def build(self) -> AbstractMainWindow:
        """Constructs and returns the configured QMainWindow."""
        return self._factory.create(config=self._config)