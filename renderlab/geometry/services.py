import math
from typing import Optional
from renderlab.math.models import Ray, Vector3
from renderlab.math.services import MathService
from .interfaces import Intersectable
from .models import HitRecord
from .validators import GeometryValidator

class Sphere(Intersectable):
    """Mathematical sphere implementation for ray intersection."""

    def __init__(self, center: Vector3, radius: float):
        GeometryValidator.assert_positive_radius(radius)
        self.center = center
        self.radius = radius

    def intersect(self, ray: Ray, t_min: float, t_max: float) -> Optional[HitRecord]:
        #Using NumPy arrays fro optimized intersection math
        oc = ray.origin.data - self.center.data
        a = MathService.dot_product(ray.direction, ray.direction)
        half_b = float(oc.dot(ray.direction.data))
        c = float(oc.dot(oc)) - self.radius * self.radius

        discriminant = half_b * half_b - a*c
        if discriminant < 0:
            return None
        
        sqrtd = math.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range.
        root = (-half_b - sqrtd) / a
        if root < t_min or t_max < root:
            root = (-half_b + sqrtd) / a
            if root < t_min or t_max < root:
                return None
            
        point = ray.point_at(root)
        outward_normal_data = (point.data - self.center.data) / self.radius
        outward_normal = Vector3(outward_normal_data[0], outward_normal_data[1], outward_normal_data[2])

        hit = HitRecord(t = root, point = point, normal = outward_normal, front_face = True)
        hit.set_face_normal(ray.direction, outward_normal)

        return hit