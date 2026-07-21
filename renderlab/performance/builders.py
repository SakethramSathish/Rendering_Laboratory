# renderlab/performance/builders.py

from renderlab.core.builders import AbstractBuilder
from .models import RenderMetrics

class PerformanceReportBuilder(AbstractBuilder):
    """Fluent API for building formatted performance reports."""
    
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._metrics = RenderMetrics()
        self._title = "Render Performance Report"

    def with_metrics(self, metrics: RenderMetrics) -> 'PerformanceReportBuilder':
        self._metrics = metrics
        return self

    def with_title(self, title: str) -> 'PerformanceReportBuilder':
        self._title = title
        return self

    def build(self) -> str:
        """Returns the formatted performance report as a string."""
        hit_ratio = 0.0
        if self._metrics.total_intersections_tested > 0:
            hit_ratio = (self._metrics.total_intersections_hit / self._metrics.total_intersections_tested) * 100

        report = [
            f"=== {self._title} ===",
            f"Time Elapsed:         {self._metrics.duration_seconds:.4f} seconds",
            f"Total Rays Cast:      {self._metrics.total_rays_cast:,}",
            f"Rays Per Second:      {self._metrics.rays_per_second:,.2f} rays/sec",
            f"Intersections Tested: {self._metrics.total_intersections_tested:,}",
            f"Intersections Hit:    {self._metrics.total_intersections_hit:,} ({hit_ratio:.2f}%)",
            "================================="
        ]
        return "\n".join(report)