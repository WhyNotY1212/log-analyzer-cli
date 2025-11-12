from log_analyzer.week3.core.model import LogRecord
def parse_one_line(line: str) -> LogRecord | None :
    if not line:
        return None
    line=line.strip()
    if not line:
        return None
    parts=line.split()
    
    if len(parts)<4:
        return None
    timestamp=parts[0]+" "+parts[1]
    level=parts[2]
    message=" ".join(parts[3:])
    valid_levels = {"INFO", "WARN", "ERROR", "DEBUG", "TRACE", "CRITICAL"}
    if level not in valid_levels:
        return None
    return LogRecord(timestamp,level,message)

def parse_lines(lines: list[str]) -> list[LogRecord]:
    record=[]
    bad_lines=[]
    for line in lines:
        r=parse_one_line(line)
        if not r:
            bad_lines.append(line)
        else:
            record.append(r)
    return record,bad_lines
        


