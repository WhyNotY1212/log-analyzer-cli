import argparse
from log_analyzer.week3.utils.io import read_lines
from log_analyzer.week3.core.model import LogRecord
from log_analyzer.week3.core.parse import parse_lines
from log_analyzer.week3.core.stats import count_level, top_tokens
from log_analyzer.week3.utils.writer import write_csv
from log_analyzer.week3.utils.filedump import write_text
from log_analyzer.week3.utils.report import write_summary

import logging
from pathlib import Path

# === 初始化日志系统 ===
log_path = Path("output/system.log")
log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=log_path,
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    filemode="a"
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input",help="Input file", required=True)
    args = parser.parse_args()
    lines = read_lines(args.input)


    if lines is not None:
        logging.info(f"Read {len(lines)} lines from {args.input}")
    else:
        logging.error(f"未读取到任何内容: {args.input}")
        print("No lines were read.")
        return

    records, bad_lines = parse_lines(lines)
    if records is not None:
        logging.info(f"Parsed {len(records)} log records，bad lines: {len(bad_lines)}")
    else:
        print("No log records were parsed.")
    
    if records:
        levels = count_level(records)
        tops = top_tokens(records, n=3)
    else:
        levels = {}
        tops = []

    print("=== Summary ===")
    logging.info("=== Summary ===")
    for k, v in levels.items():
        print(k, v)
    for token, cnt in tops:
        print(token, cnt)
    level_rows = [(k, v) for k, v in levels.items()]
    write_csv("output/levels.csv", level_rows)

    write_csv("output/top_tokens.csv", tops)
    logging.info("Saved CSV -> output/levels.csv, output/top_tokens.csv")
    print("CSV files saved → output/levels.csv, output/top_tokens.csv")
    
    # === bad lines output ===
    if bad_lines:
        write_text("output/bad.log", bad_lines)
        logging.warning(f"Saved {len(bad_lines)} bad lines to output/bad.log")
    else:
        logging.info("No bad lines to save.")


    # === summary report ===
    write_summary(levels, tops, len(bad_lines), path="output/summary.txt")








if __name__ == "__main__":
    main()