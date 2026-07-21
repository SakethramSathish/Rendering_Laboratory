# renderlab/performance/factories.py

from renderlab.core.factories import AbstractFactory
from .interfaces import AbstractProfiler, AbstractPerformanceMonitor
from .services import PyInstrumentWrapper, EnginePerformanceMonitor

class PerformanceFactory(AbstractFactory):
    """Factory for creating performance monitoring tools."""
    
    def create(self, **kwargs) -> AbstractPerformanceMonitor:
        """Default behavior returns a standard performance monitor."""
        return self.create_monitor()

    @staticmethod
    def create_monitor() -> AbstractPerformanceMonitor:
        return EnginePerformanceMonitor()

    @staticmethod
    def create_profiler(profiler_type: str = "pyinstrument") -> AbstractProfiler:
        if profiler_type == "pyinstrument":
            return PyInstrumentWrapper()
        raise ValueError(f"Unknown profiler type: {profiler_type}")