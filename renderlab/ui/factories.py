# renderlab/ui/factories.py

import sys
from PySide6.QtWidgets import QApplication
from renderlab.core.factories import AbstractFactory
from .interfaces import AbstractMainWindow
from .services import RenderLabMainWindow
from .models import WindowConfig

class UIFactory(AbstractFactory):
    """Factory for spinning up the Qt Application and its main components."""
    
    _app_instance = None
    
    @classmethod
    def get_qapplication(cls) -> QApplication:
        """Ensures only one QApplication instance exists."""
        if cls._app_instance is None:
            cls._app_instance = QApplication.instance()
            if cls._app_instance is None:
                cls._app_instance = QApplication(sys.argv)
        return cls._app_instance

    def create(self, **kwargs) -> AbstractMainWindow:
        """Creates the main window."""
        config = kwargs.get("config", WindowConfig())
        return RenderLabMainWindow(config)