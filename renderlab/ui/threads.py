# renderlab/ui/threads.py

from PySide6.QtCore import QThread, Signal
from renderlab.renderer.interfaces import AbstractRenderer
from renderlab.scene.interfaces import AbstractScene
from renderlab.renderer.models import RenderSettings
from renderlab.renderer.exceptions import RenderAbortedError
from PySide6.QtGui import QImage
import numpy as np

class RenderWorker(QThread):
    """Background worker for rendering the scene without freezing the UI."""
    
    # Emits the final QImage when complete
    render_complete = Signal(QImage)
    
    # Emitted if the render was cancelled
    render_aborted = Signal()

    def __init__(self, renderer: AbstractRenderer, scene: AbstractScene, settings: RenderSettings):
        super().__init__()
        self.renderer = renderer
        self.scene = scene
        self.settings = settings

    def run(self):
        try:
            result = self.renderer.render(self.scene, self.settings)
            pixel_data = result.get_image_data()
            
            height, width, channels = pixel_data.shape
            bytes_per_line = channels * width
            
            if pixel_data.dtype != np.uint8:
                pixel_data = pixel_data.astype(np.uint8)
                
            # MUST copy() so the QImage owns the memory before leaving this thread scope
            q_image = QImage(pixel_data.data, width, height, bytes_per_line, QImage.Format_RGB888).copy()
            self.render_complete.emit(q_image)
        except RenderAbortedError:
            self.render_aborted.emit()
        except Exception as e:
            print(f"Renderer failed with an unexpected error: {e}")
