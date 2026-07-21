import numpy as np
from typing import Optional, Tuple
from renderlab.math.models import Ray, Vector3
from renderlab.math.services import MathService
from renderlab.geometry.models import HitRecord
from .interfaces import Material
from .validators import MaterialValidator

def generate_random_unit_vector() -> Vector3:
    """Generates a random 3D unit vector via spherical rejection sampling."""
    while True:
        p = np.random.uniform(-1.0, 1.0, 3)
        if np.dot(p, p) < 1.0:
            mag = np.linalg.norm(p)
            norm_p = p / mag if mag > 0 else p
            return Vector3(norm_p[0], norm_p[1], norm_p[2])
        
class Lambertian(Material):
    """Ideal diffuse material executing cosine-weighted hemispherical scattering."""

    def __init__(self, albedo: Vector3):
        MaterialValidator.assert_valid_albedo(albedo)
        self.albedo = albedo

    def scatter(self, ray_in: Ray, rec: HitRecord) -> Optional[Tuple[Vector3, Ray]]:
        scatter_direction_data = rec.normal.data + generate_random_unit_vector().data

        # Guard against degenerate vectors matching inverse normal
        if np.allclose(scatter_direction_data, 0.0, atol=1e-8):
            scatter_direction_data = rec.normal.data
            
        scattered = Ray(rec.point, Vector3(scatter_direction_data[0], scatter_direction_data[1], scatter_direction_data[2]).normalize())
        return self.albedo, scattered

class Metal(Material):
    """Specular reflection material supporting fuzzy microfacet roughness."""
    
    def __init__(self, albedo: Vector3, roughness: float):
        MaterialValidator.assert_valid_albedo(albedo)
        MaterialValidator.assert_valid_roughness(roughness)
        self.albedo = albedo
        self.roughness = roughness

    def scatter(self, ray_in: Ray, rec: HitRecord) -> Optional[Tuple[Vector3, Ray]]:
        reflected = MathService.reflect(ray_in.direction, rec.normal)
        fuzz_vector = generate_random_unit_vector().data * self.roughness
        scattered_dir_data = reflected.data + fuzz_vector
        
        scattered = Ray(rec.point, Vector3(scattered_dir_data[0], scattered_dir_data[1], scattered_dir_data[2]).normalize())
        
        # Verify scattered ray reflects outward from the surface hemisphere
        if MathService.dot_product(scattered.direction, rec.normal) > 0:
            return self.albedo, scattered
        return None