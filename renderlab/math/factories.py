import numpy as np
from renderlab.core.factories import AbstractFactory

class TransformFactory(AbstractFactory):
    """Creates standard 4x4 transformation matrices"""

    def create(self, **kwargs) -> np.ndarray:
        return np.eye(4, dtype=np.float64)
    
    @staticmethod
    def translation(x: float, y: float, z: float) -> np.ndarray:
        mat = np.eye(4, dtype=np.float64)
        mat[0,3] = x
        mat[1,3] = y
        mat[2,3] = z
        return mat
    
    @staticmethod
    def scale(sx: float, sy: float, sz: float) -> np.ndarray:
        mat = np.eye(4, dtype=np.float64)
        mat[0,0] = sx
        mat[1,1] = sy
        mat[2,2] = sz
        return mat