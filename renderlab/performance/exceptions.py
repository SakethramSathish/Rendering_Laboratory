# renderlab/performance/exceptions.py

from renderlab.core.exceptions import RenderLabException

class PerformanceError(RenderLabException):
    """Base exception for all performance and profiling errors."""
    pass

class ProfilerStateError(PerformanceError):
    """Raised when attempting to stop a profiler that hasn't started, or vice versa."""
    pass