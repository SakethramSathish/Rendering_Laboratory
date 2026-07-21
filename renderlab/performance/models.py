# renderlab/performance/models.py

from dataclasses import dataclass
import time

@dataclass
class RenderMetrics:
    """Pure data container for statistics gathered during rendering."""
    total_rays_cast: int = 0
    total_intersections_tested: int = 0
    total_intersections_hit: int = 0
    start_time: float = 0.0
    end_time: float = 0.0

    @property
    def duration_seconds(self) -> float:
        return max(0.0, self.end_time - self.start_time)

    @property
    def rays_per_second(self) -> float:
        if self.duration_seconds == 0:
            return 0.0
        return self.total_rays_cast / self.duration_seconds