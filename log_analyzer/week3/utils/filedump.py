from pathlib import Path

def write_text(path: str, lines: list[str]):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    # 原样写入
    content = "".join(lines)  # 每行原本就带换行符
    p.write_text(content, encoding="utf-8")
