# renderlab/animation/validators.py

from typing import List, Any
from .exceptions import InvalidKeyframeError, TrackEmptyError
from .models import Keyframe

class AnimationValidator:
    """Validation utility for animation tracks and keyframes."""
    
    @staticmethod
    def assert_valid_time(time: float) -> None:
        """Ensures a keyframe's time is not negative."""
        if time < 0.0:
            raise InvalidKeyframeError(f"Keyframe time cannot be negative. Got {time}")

    @staticmethod
    def assert_track_not_empty(keyframes: List[Any]) -> None:
        """Ensures the track has data to evaluate."""
        if not keyframes:
            raise TrackEmptyError("Cannot evaluate an empty animation track.")

    @staticmethod
    def assert_sorted_keyframes(keyframes: List[Keyframe]) -> None:
        """Ensures keyframes are strictly increasing in time."""
        for i in range(1, len(keyframes)):
            if keyframes[i].time <= keyframes[i-1].time:
                raise InvalidKeyframeError("Keyframes must be sorted by strictly increasing time.")