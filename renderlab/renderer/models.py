import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class RenderSettings:
    """Configuration parameters for the CPU rendering engine."""
    image_width: int = 800
    image_height: int = 600
    samples_per_pixel: int = 10
    max_depth: int = 10
    multthreading_enabled: bool = True

@dataclass
class RenderResult:
    """Stores the final pixel data after a render completes."""
    width: int
    height: int
    pixels: np.ndarray

    def get_image_data(self) -> np.ndarray:
        """Returns the image data scaled to 8-bit RGB (0-255)."""
        #Apply simple gamma correction (gamma=2.0)
        gamma_corrected = np.sqrt(np.clip(self.pixels, 0.0, 1.0))
        return (gamma_corrected * 255).astype(np.uint8)