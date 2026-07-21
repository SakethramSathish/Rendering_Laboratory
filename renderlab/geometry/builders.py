# renderlab/geometry/builders.py

from typing import List
from renderlab.core.builders import AbstractBuilder
from .interfaces import Intersectable
from renderlab.math.models import Ray
from .models import HitRecord
from typing import Optional

class GeometryList(Intersectable):
    """An aggregate geometry container that tests intersections against multiple objects."""
    
    def __init__(self):
        self.objects: List[Intersectable] = []

    def add(self, obj: Intersectable) -> None:
        self.objects.append(obj)
        
    def clear(self) -> None:
        self.objects.clear()

    def intersect(self, ray: Ray, t_min: float, t_max: float) -> Optional[HitRecord]:
        hit_anything = None
        closest_so_far = t_max

        for obj in self.objects:
            hit = obj.intersect(ray, t_min, closest_so_far)
            if hit:
                closest_so_far = hit.t
                hit_anything = hit

        return hit_anything

class SceneGeometryBuilder(AbstractBuilder):
    """Builder for constructing the aggregate geometric representation of a scene."""
    
    def __init__(self):
        self._geometry_list = GeometryList()

    def reset(self) -> None:
        self._geometry_list = GeometryList()

    def add_shape(self, shape: Intersectable) -> 'SceneGeometryBuilder':
        self._geometry_list.add(shape)
        return self

    def build(self) -> GeometryList:
        """Returns the fully aggregated list of scene geometry."""
        return self._geometry_list