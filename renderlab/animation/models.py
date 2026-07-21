# renderlab/animation/models.py

from dataclasses import dataclass, field
from typing import List, TypeVar, Generic, Union
from renderlab.math.models import Vector3
from renderlab.core.models import Entity

# Type variable to allow Keyframes of float or Vector3
T = TypeVar('T', float, Vector3)

@dataclass
class Keyframe(Generic[T]):
    """A specific value at a specific point in time."""
    time: float
    value: T

@dataclass
class AnimationTrack(Entity, Generic[T]):
    """A sequence of keyframes representing property changes over time."""
    keyframes: List[Keyframe[T]] = field(default_factory=list)
    loop: bool = False
    
    def get_duration(self) -> float:
        if not self.keyframes:
            return 0.0
        return self.keyframes[-1].time