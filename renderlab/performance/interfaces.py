# renderlab/performance/interfaces.py

from abc import ABC, abstractmethod
from .models import RenderMetrics

class AbstractProfiler(ABC):
    """Interface for code execution profilers."""
    
    @abstractmethod
    def start(self) -> None:
        """Begins tracking execution time and call stacks."""
        pass

    @abstractmethod
    def stop(self) -> None:
        """Stops tracking."""
        pass

    @abstractmethod
    def get_report(self) -> str:
        """Returns a formatted profiling report."""
        pass

class AbstractPerformanceMonitor(ABC):
    """Interface for tracking rendering statistics."""
    
    @abstractmethod
    def start_timer(self) -> None:
        pass

    @abstractmethod
    def stop_timer(self) -> None:
        pass

    @abstractmethod
    def record_ray(self, count: int = 1) -> None:
        pass
        
    @abstractmethod
    def record_intersection_test(self, hit: bool) -> None:
        pass

    @abstractmethod
    def get_metrics(self) -> RenderMetrics:
        pass