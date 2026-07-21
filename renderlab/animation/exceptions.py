# renderlab/animation/exceptions.py

from renderlab.core.exceptions import RenderLabException

class AnimationError(RenderLabException):
    """Base exception for all animation-related errors."""
    pass

class InvalidKeyframeError(AnimationError):
    """Raised when a keyframe has an invalid time or value."""
    pass

class TrackEmptyError(AnimationError):
    """Raised when attempting to evaluate an animation track with no keyframes."""
    pass