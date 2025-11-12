from dataclasses import dataclass

@dataclass
class LogRecord:
    timestamp: str
    level: str
    message: str

Parsed = list[LogRecord]
LevelCount = dict[str, int]
TopTokens = list[tuple[str, int]]