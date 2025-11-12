# Log Analyzer CLI Tool

A simple command-line log analysis tool written in Python.

## 🧩 Features
- Parse `.log` files
- Count log levels (INFO, WARN, ERROR)
- Extract top tokens
- Export CSV reports

## 🚀 Installation
```bash
pip install -e .
🧠 Usage
bash
log-analyze -i log_analyzer/week3/sample/sample.log
📦 Output
bash
=== Summary ===
INFO 2
WARN 1
ERROR 1
CSV files saved → output/levels.csv, output/top_tokens.csv
