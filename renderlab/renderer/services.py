import random
import numpy as np
from renderlab.math.models import Ray, Vector3
from renderlab.scene.interfaces import AbstractScene
from .interfaces import AbstractRenderer
from .models import RenderSettings, RenderResult
from .validators import RendererValidator
from .exceptions import RenderAbortedError

class CPURenderer(AbstractRenderer):
    """A pure Python/NumPy CPU path-tracing rendering engine."""

    def __init__(self):
        self.abort_flag = False
    
    def abort(self) -> None:
        self._abort_flag = True

    def _ray_color(self, ray: Ray, scene: AbstractScene, depth: int) -> Vector3:
        """Recursively calculates the color of a single ray path."""
        #Base case: Ray bounce limit reached
        if depth <= 0:
            return Vector3(0.0, 0.0, 0.0)

        # 0.001 t_min prevents shadow acne (self-intersection)
        hit = scene.intersect(ray, t_min=0.001, t_max=float('inf'))

        if hit:
            # The material property was attached to the hit record dynamically in the Scene
            material = getattr(hit, 'material', None)
            if material:
                scatter_result = material.scatter(ray, hit)
                if scatter_result:
                    attenuation, scattered_ray = scatter_result
                    # Recursive call
                    color_from_scatter = self._ray_color(scattered_ray, scene, depth - 1)
                    
                    # Multiply attenuation (albedo) by the scattered light
                    r = attenuation.x * color_from_scatter.x
                    g = attenuation.y * color_from_scatter.y
                    b = attenuation.z * color_from_scatter.z
                    return Vector3(r, g, b)
            # If absorbed or no material
            return Vector3(0.0, 0.0, 0.0)
    
        # Background color
        bg_color = scene.get_background(ray)
        return Vector3(bg_color[0], bg_color[1], bg_color[2])
    
    def render(self, scene: AbstractScene, settings: RenderSettings) -> RenderResult:
        """Executes the main rendering loop over all pixels."""
        RendererValidator.validate_settings(settings)
        self._abort_flag = False
        
        camera = scene.get_camera()
        width = settings.image_width
        height = settings.image_height
        samples = settings.samples_per_pixel
        
        # Buffer to hold floating point colors
        pixel_buffer = np.zeros((height, width, 3), dtype=np.float64)

        for j in range(height):
            if self._abort_flag:
                raise RenderAbortedError("Rendering aborted by user.")
                
            for i in range(width):
                pixel_color = Vector3(0.0, 0.0, 0.0)
                
                # Multi-sampling for anti-aliasing
                for _ in range(samples):
                    u = (i + random.random()) / (width - 1)
                    v = (j + random.random()) / (height - 1)
                    
                    # Note: v coordinate is often inverted in image buffers (0 at top)
                    ray = camera.get_ray(u, 1.0 - v)
                    sample_color = self._ray_color(ray, scene, settings.max_depth)
                    
                    pixel_color.data += sample_color.data

                # Average the samples
                pixel_buffer[j, i] = (pixel_color.data / samples)

        return RenderResult(width=width, height=height, pixels=pixel_buffer)