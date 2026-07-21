# renderlab/logging/models.py

from dataclasses import dataclass
from enum import IntEnum

class LogLevel(IntEnum):
    """Domain-specific logging levels mapped to integers."""
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

@dataclass
class LogConfig:
    """Configuration parameters for the logger."""
    level: LogLevel = LogLevel.INFO
    log_to_console: bool = True
    log_to_file: bool = False
    file_path: str = "renderlab.log"
    format_string: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"