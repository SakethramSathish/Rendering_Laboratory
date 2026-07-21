import numpy as np
from renderlab.math.models import Vector3, Ray
from renderlab.geometry.services import Sphere
from renderlab.materials.services import Lambertian
from renderlab.scene.models import SceneNode
from renderlab.scene.services import Scene
from renderlab.renderer.services import CPURenderer

def test_ray_color():
    scene = Scene()
    sphere_geo = Sphere(Vector3(0.0, 0.0, -1.0), 0.5)
    sphere_mat = Lambertian(Vector3(0.8, 0.2, 0.2))
    scene.add_node(SceneNode(geometry=sphere_geo, material=sphere_mat))

    renderer = CPURenderer()
    ray = Ray(Vector3(0.0, 0.0, 0.0), Vector3(0.0, 0.0, -1.0).normalize())
    
    colors = []
    for _ in range(5):
        c = renderer._ray_color(ray, scene, depth=3)
        colors.append((c.x, c.y, c.z))
    print(f"Colors hit front center: {colors}")
    
    # Ray missing sphere
    ray_miss = Ray(Vector3(0.0, 0.0, 0.0), Vector3(0.0, 1.0, 0.0).normalize())
    print(f"Color miss: {renderer._ray_color(ray_miss, scene, depth=3)}")

test_ray_color()
