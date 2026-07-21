# renderlab/animation/builders.py

from typing import TypeVar, Generic
from renderlab.core.builders import AbstractBuilder
from renderlab.math.models import Vector3
from .models import AnimationTrack, Keyframe
from .validators import AnimationValidator
from .factories import AnimationFactory

T = TypeVar('T', float, Vector3)

class TrackBuilder(AbstractBuilder, Generic[T]):
    """Fluent API for constructing animation tracks frame by frame."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._keyframes = []
        self._loop = False

    def set_looping(self, loop: bool) -> 'TrackBuilder':
        self._loop = loop
        return self

    def add_keyframe(self, time: float, value: T) -> 'TrackBuilder':
        """Adds a keyframe. Will be sorted upon building."""
        AnimationValidator.assert_valid_time(time)
        self._keyframes.append(Keyframe(time=time, value=value))
        return self

    def build(self) -> AnimationTrack[T]:
        """Validates, sorts, and returns the constructed animation track."""
        # Ensure keyframes are sorted chronologically before creation
        self._keyframes.sort(key=lambda k: k.time)
        return AnimationFactory.create_track(self._keyframes, loop=self._loop)