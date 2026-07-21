# renderlab/performance/validators.py

from .exceptions import ProfilerStateError

class PerformanceValidator:
    """Validates the state transitions of performance trackers."""
    
    @staticmethod
    def assert_profiler_running(is_running: bool) -> None:
        """Ensures the profiler is running before attempting to stop it."""
        if not is_running:
            raise ProfilerStateError("Cannot stop a profiler that is not currently running.")

    @staticmethod
    def assert_profiler_stopped(is_running: bool) -> None:
        """Ensures the profiler is stopped before attempting to start it again."""
        if is_running:
            raise ProfilerStateError("Cannot start a profiler that is already running.")