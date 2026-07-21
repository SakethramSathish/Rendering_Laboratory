# renderlab/animation/services.py

from typing import TypeVar
from renderlab.math.models import Vector3
from .models import AnimationTrack
from .validators import AnimationValidator

T = TypeVar('T', float, Vector3)

class InterpolationService:
    """Service handling mathematical interpolation between keyframes."""

    @staticmethod
    def _lerp_float(start: float, end: float, t: float) -> float:
        return start + (end - start) * t

    @staticmethod
    def _lerp_vector(start: Vector3, end: Vector3, t: float) -> Vector3:
        x = InterpolationService._lerp_float(start.x, end.x, t)
        y = InterpolationService._lerp_float(start.y, end.y, t)
        z = InterpolationService._lerp_float(start.z, end.z, t)
        return Vector3(x, y, z)

    @classmethod
    def evaluate_track(cls, track: AnimationTrack[T], current_time: float) -> T:
        """Evaluates the track at a specific time, returning the interpolated value."""
        AnimationValidator.assert_track_not_empty(track.keyframes)
        
        keyframes = track.keyframes
        duration = track.get_duration()

        # Handle Looping
        if track.loop and duration > 0:
            current_time = current_time % duration

        # Edge cases: Before first frame or after last frame
        if current_time <= keyframes[0].time:
            return keyframes[0].value
        if current_time >= keyframes[-1].time:
            return keyframes[-1].value

        # Find the surrounding keyframes
        for i in range(len(keyframes) - 1):
            k1 = keyframes[i]
            k2 = keyframes[i + 1]

            if k1.time <= current_time <= k2.time:
                # Calculate interpolation factor (0.0 to 1.0)
                time_range = k2.time - k1.time
                t = (current_time - k1.time) / time_range

                if isinstance(k1.value, Vector3) and isinstance(k2.value, Vector3):
                    return cls._lerp_vector(k1.value, k2.value, t)
                elif isinstance(k1.value, (float, int)) and isinstance(k2.value, (float, int)):
                    return cls._lerp_float(float(k1.value), float(k2.value), t)
                else:
                    raise TypeError("Unsupported interpolation type in keyframes.")
                    
        return keyframes[-1].value