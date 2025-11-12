import csv
from pathlib import Path

def write_csv(path: str, rows: list[tuple]):
    p = Path(path)

    # 自动建目录
    p.parent.mkdir(parents=True, exist_ok=True)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["key", "value"])
        writer.writerows(rows)
