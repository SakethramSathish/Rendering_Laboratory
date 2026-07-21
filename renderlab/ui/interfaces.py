# renderlab/ui/interfaces.py

from abc import ABC, abstractmethod
import numpy as np
from renderlab.core.interfaces import Observer

class AbstractViewport(Observer):
    """Interface for the rendering output display."""
    
    @abstractmethod
    def update_image(self, pixel_data: np.ndarray) -> None:
        """Receives a new image buffer from the engine and displays it."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clears the current viewport image."""
        pass

class AbstractMainWindow(ABC):
    """Interface for the primary application shell."""
    
    @abstractmethod
    def show(self) -> None:
        """Displays the window to the user."""
        pass

    @abstractmethod
    def close(self) -> None:
        """Safely terminates the window and underlying processes."""
        pass