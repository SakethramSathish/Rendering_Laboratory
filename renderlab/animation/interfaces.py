# renderlab/animation/interfaces.py

from abc import ABC, abstractmethod

class Animatable(ABC):
    """Interface for scene objects or properties that can change over time."""
    
    @abstractmethod
    def update(self, delta_time: float, total_time: float) -> None:
        """
        Advances the object's state based on the engine's timeline.
        delta_time: Time elapsed since the last frame.
        total_time: Total time elapsed since animation started.
        """
        pass