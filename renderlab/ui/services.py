# renderlab/ui/services.py

import sys
import numpy as np
from typing import Any
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Qt, QObject
from abc import ABCMeta
from .interfaces import AbstractMainWindow, AbstractViewport
from .models import WindowConfig, ViewportState
from .validators import UIValidator
from renderlab.scene.interfaces import AbstractScene
from renderlab.renderer.interfaces import AbstractRenderer
from renderlab.renderer.models import RenderSettings
from .threads import RenderWorker
import copy

class QABCMeta(type(QObject), ABCMeta):
    pass

class ViewportWidget(QWidget, AbstractViewport, metaclass=QABCMeta):
    """Concrete PySide6 widget for displaying the rendered image."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.state = ViewportState()
        
        # Setup Layout
        self.layout = QVBoxLayout(self)
        self.image_label = QLabel("Viewport Initializing...")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

    def update(self, event_type: str, event_data: Any) -> None:
        if event_type == "RENDER_COMPLETE" and isinstance(event_data, QImage):
            self.update_image(event_data)

    def update_image(self, q_image: QImage) -> None:
        """Updates the label with a pre-constructed QImage."""
        self.image_label.setPixmap(QPixmap.fromImage(q_image))
        self.image_label.setScaledContents(True)

    def clear(self) -> None:
        self.image_label.clear()
        self.image_label.setText("No Image")


class RenderLabMainWindow(QMainWindow, AbstractMainWindow, metaclass=QABCMeta):
    """Concrete PySide6 Main Window implementation."""
    
    def __init__(self, config: WindowConfig):
        super().__init__()
        UIValidator.assert_valid_dimensions(config)
        
        self.setWindowTitle(config.title)
        self.resize(config.width, config.height)
        
        if config.is_maximized:
            self.showMaximized()
            
        # Initialize central widget
        self.viewport = ViewportWidget(self)
        self.setCentralWidget(self.viewport)

        self.worker = None
        self.scene = None
        self.renderer = None
        self.settings = None
        self._is_aborting = False
        self._next_preview_state = False

    def start_engine(self, scene: AbstractScene, renderer: AbstractRenderer, settings: RenderSettings):
        self.scene = scene
        self.renderer = renderer
        self.settings = settings
        self.trigger_render(preview=False)

    def trigger_render(self, preview=False):
        self._next_preview_state = preview
        if self.worker and self.worker.isRunning():
            if not self._is_aborting:
                self._is_aborting = True
                self.renderer.abort()
            return # Wait for the worker to naturally abort and signal us

        self._start_worker(preview)

    def _start_worker(self, preview):
        self._is_aborting = False
        run_settings = copy.deepcopy(self.settings)
        if preview:
            run_settings.samples_per_pixel = 1
            run_settings.max_depth = 1 # very fast

        self.worker = RenderWorker(self.renderer, self.scene, run_settings)
        self.worker.render_complete.connect(self._on_render_complete)
        self.worker.render_aborted.connect(self._on_render_aborted)
        self.worker.start()

    def _on_render_aborted(self):
        # Safely start the next queued render once the old worker has died
        self._start_worker(self._next_preview_state)

    def _on_render_complete(self, q_image: QImage):
        self.viewport.update_image(q_image)

    def keyPressEvent(self, event):
        if not self.scene: return
        camera = self.scene.get_camera()
        moved = False
        speed = 0.5

        if event.key() == Qt.Key_W:
            camera.move_forward(speed)
            moved = True
        elif event.key() == Qt.Key_S:
            camera.move_forward(-speed)
            moved = True
        elif event.key() == Qt.Key_D:
            camera.move_right(speed)
            moved = True
        elif event.key() == Qt.Key_A:
            camera.move_right(-speed)
            moved = True

        if moved:
            self.trigger_render(preview=True)

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return
        if event.key() in (Qt.Key_W, Qt.Key_A, Qt.Key_S, Qt.Key_D):
            self.trigger_render(preview=False)

    def wheelEvent(self, event):
        if not self.scene: return
        camera = self.scene.get_camera()
        delta = event.angleDelta().y() / 120.0
        camera.zoom(-delta * 5.0)
        self.trigger_render(preview=False)