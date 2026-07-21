# renderlab/math/builders.py

import numpy as np
from renderlab.core.builders import AbstractBuilder
from .factories import TransformFactory

class TransformBuilder(AbstractBuilder):
    """Builds complex 4x4 transformation matrices via method chaining."""
    
    def __init__(self):
        self._matrix = np.eye(4, dtype=np.float64)

    def reset(self) -> None:
        self._matrix = np.eye(4, dtype=np.float64)

    def translate(self, x: float, y: float, z: float) -> 'TransformBuilder':
        trans_mat = TransformFactory.translation(x, y, z)
        self._matrix = self._matrix @ trans_mat
        return self

    def scale(self, sx: float, sy: float, sz: float) -> 'TransformBuilder':
        scale_mat = TransformFactory.scale(sx, sy, sz)
        self._matrix = self._matrix @ scale_mat
        return self

    def build(self) -> np.ndarray:
        return self._matrix