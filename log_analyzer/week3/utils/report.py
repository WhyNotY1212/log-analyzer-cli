from pathlib import Path

def write_summary(levels: dict, tokens: list[tuple[str, int]], bad_count: int, path="output/summary.txt"):
    """
    生成汇总报告 summary.txt

    参数:
        levels:    日志等级统计，例如 {'INFO': 5, 'ERROR': 2}
        tokens:    高频词列表，例如 [('error', 4), ('slow', 2)]
        bad_count: 无法解析的行数
        path:      输出路径，默认为 output/summary.txt
    """

    # 1. 确保输出路径存在
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    # 2. 构造报告内容
    lines = []
    lines.append("=== Log Analysis Summary ===")
    lines.append(f"Total bad lines: {bad_count}")

    # --- Levels 统计 ---
    lines.append("\n--- Levels ---")
    for level, count in levels.items():
        lines.append(f"{level}: {count}")

    # --- Top Tokens 统计 ---
    lines.append("\n--- Top Tokens ---")
    for token, freq in tokens:
        lines.append(f"{token}: {freq}")

    # 3. 写入文件
    text = "\n".join(lines)
    p.write_text(text, encoding="utf-8")


