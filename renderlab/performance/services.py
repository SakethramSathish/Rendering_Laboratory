# renderlab/performance/services.py

import time
from pyinstrument import Profiler
from .interfaces import AbstractProfiler, AbstractPerformanceMonitor
from .models import RenderMetrics
from .validators import PerformanceValidator

class PyInstrumentWrapper(AbstractProfiler):
    """Concrete profiler wrapping the PyInstrument library."""
    
    def __init__(self):
        self._profiler = Profiler()
        self._is_running = False

    def start(self) -> None:
        PerformanceValidator.assert_profiler_stopped(self._is_running)
        self._profiler.start()
        self._is_running = True

    def stop(self) -> None:
        PerformanceValidator.assert_profiler_running(self._is_running)
        self._profiler.stop()
        self._is_running = False

    def get_report(self) -> str:
        if self._is_running:
            return "Profiler is currently running. Stop it to generate a report."
        return self._profiler.output_text(unicode=True, color=False)


class EnginePerformanceMonitor(AbstractPerformanceMonitor):
    """Concrete tracker for engine-specific rendering statistics."""
    
    def __init__(self):
        self._metrics = RenderMetrics()
        self._is_timing = False

    def start_timer(self) -> None:
        self._metrics.start_time = time.perf_counter()
        self._is_timing = True

    def stop_timer(self) -> None:
        if self._is_timing:
            self._metrics.end_time = time.perf_counter()
            self._is_timing = False

    def record_ray(self, count: int = 1) -> None:
        self._metrics.total_rays_cast += count

    def record_intersection_test(self, hit: bool) -> None:
        self._metrics.total_intersections_tested += 1
        if hit:
            self._metrics.total_intersections_hit += 1

    def get_metrics(self) -> RenderMetrics:
        # If requested while running, calculate current duration dynamically
        if self._is_timing:
            current_metrics = RenderMetrics(
                total_rays_cast=self._metrics.total_rays_cast,
                total_intersections_tested=self._metrics.total_intersections_tested,
                total_intersections_hit=self._metrics.total_intersections_hit,
                start_time=self._metrics.start_time,
                end_time=time.perf_counter()
            )
            return current_metrics
        return self._metrics