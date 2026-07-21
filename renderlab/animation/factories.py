# renderlab/animation/factories.py

from typing import List, TypeVar
from renderlab.core.factories import AbstractFactory
from renderlab.math.models import Vector3
from .models import AnimationTrack, Keyframe
from .validators import AnimationValidator

T = TypeVar('T', float, Vector3)

class AnimationFactory(AbstractFactory):
    """Factory for creating animation tracks."""
    
    def create(self, **kwargs) -> AnimationTrack:
        """Generic creation method."""
        loop = kwargs.get("loop", False)
        return AnimationTrack(loop=loop)

    @staticmethod
    def create_track(keyframes: List[Keyframe[T]], loop: bool = False) -> AnimationTrack[T]:
        """Creates a track from a pre-existing list of keyframes, validating them first."""
        AnimationValidator.assert_sorted_keyframes(keyframes)
        track = AnimationTrack[T](loop=loop)
        track.keyframes = keyframes
        return track