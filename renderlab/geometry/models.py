from dataclasses import dataclass
from renderlab.math.models import Vector3

@dataclass
class HitRecord:
    """Stores information about a ray-geometry intersection."""

    t: float            #Distance along the ray
    point: Vector3      #3D intersection point
    normal: Vector3     #Surface normal at the intersection point
    front_face: bool    #True if the ray hit the outside of the surface

    def set_face_normal(self,  ray_direction: Vector3, outward_normal: Vector3) -> None:
        """Determines if the ray is hitting the front or back face."""
        from renderlab.math.services import MathService
        self.front_face = MathService.dot_product(ray_direction, outward_normal) < 0
        self.normal = outward_normal if self.front_face else Vector3(
            -outward_normal.x, -outward_normal.y, -outward_normal.z
        )