import math
from renderlab.math.models import Ray, Vector3
from renderlab.math.services import MathService
from .interfaces import AbstractCamera
from .models import CameraConfig
from .validators import CameraValidator

class PerspectiveCamera(AbstractCamera):
    """A standard pinhole perspective camera model."""

    def __init__(self, config: CameraConfig):
        CameraValidator.assert_valid_fov(config.vfov)
        CameraValidator.assert_valid_aspect_ratio(config.aspect_ratio)

        self.config = config
        self.origin = config.lookfrom
        self._recalculate_geometry()

    def _recalculate_geometry(self):
        #Calculate viewport dimensions
        theta = math.radians(self.config.vfov)
        h = math.tan(theta / 2.0)
        viewport_height = 2.0 * h
        viewport_width = self.config.aspect_ratio * viewport_height

        #Calculate the orthonormal basis (u, v, w) for camera orientation
        #w points opposite to the viewing direction
        w_data = self.origin.data - self.config.lookat.data
        self.w = Vector3(w_data[0], w_data[1], w_data[2]).normalize()

        self.u = MathService.cross_product(self.config.vup, self.w).normalize()
        self.v = MathService.cross_product(self.w, self.u)

        #Map viewport to 3D space
        self.horizontal = Vector3(viewport_width * self.u.data[0], viewport_width * self.u.data[1], viewport_width * self.u.data[2])
        self.vertical = Vector3(viewport_height * self.v.data[0], viewport_height * self.v.data[1], viewport_height * self.v.data[2])

        #Determine the lower left corner of the virtual viewport
        llc_data = self.origin.data - (self.horizontal.data / 2.0) - (self.vertical.data / 2.0) - self.w.data
        self.lower_left_corner = Vector3(llc_data[0], llc_data[1], llc_data[2])

    def move_forward(self, distance: float):
        move_vec = self.w.data * -distance
        self.origin.data += move_vec
        self.config.lookat.data += move_vec
        self._recalculate_geometry()

    def move_right(self, distance: float):
        move_vec = self.u.data * distance
        self.origin.data += move_vec
        self.config.lookat.data += move_vec
        self._recalculate_geometry()

    def zoom(self, delta: float):
        self.config.vfov = max(10.0, min(120.0, self.config.vfov + delta))
        self._recalculate_geometry()

    def get_ray(self, s: float, t: float) -> Ray:
        """Calculates the ray passing through viewport coordinate (s, t)."""
        direction_data = self.lower_left_corner.data + (s * self.horizontal.data) + (t * self.vertical.data) - self.origin.data
        direction = Vector3(direction_data[0], direction_data[1], direction_data[2]).normalize()
        return Ray(origin = self.origin, direction = direction)

