# 🧠 Log Analyzer CLI

一个用 **Python** 构建的轻量级命令行工具，用于快速分析日志文件（Log 文件）中的信息。  
它可以自动统计日志等级（INFO/WARN/ERROR）与高频关键词，并输出 CSV 与 TXT 报告。

---

## 🚀 功能概览
- 解析日志文件（按行读取，跳过坏行）
- 统计日志等级分布（INFO、WARN、ERROR）
- 提取最常出现的关键词
- 输出多种结果格式：
  - `output/levels.csv`：日志等级统计
  - `output/top_tokens.csv`：高频关键词统计
  - `output/summary.txt`：汇总报告
  - `output/bad.log`：无法解析的行  

---

## 🧩 安装与环境

### 方式一：开发者模式（推荐）
```bash
git clone https://github.com/WhyNotY1212/log-analyzer-cli.git
cd log-analyzer-cli
pip install -e .
方式二：使用 requirements.txt 安装依赖
bash
<<<<<<< HEAD
log-analyze -i log_analyzer/week3/sample/sample.log
📦 Output
bash
=== Summary ===
INFO 2
WARN 1
ERROR 1
CSV files saved → output/levels.csv, output/top_tokens.csv
=======
复制代码
pip install -r requirements.txt
要求环境：

Python ≥ 3.10

依赖：argparse

⚙️ 使用方法
1️⃣ 分析示例日志文件
bash
复制代码
log-analyze -i week3/sample/sample.log
2️⃣ 自定义输入文件路径
bash
复制代码
log-analyze -i your_folder/your_log.log
执行后会在 output/ 文件夹中自动生成：

lua
复制代码
output/
├── levels.csv
├── top_tokens.csv
├── summary.txt
└── bad.log
📊 输出示例
text
复制代码
=== Log Analysis Summary ===
Total bad lines: 2

--- Levels ---
INFO: 2
ERROR: 1
WARN: 1

--- Top Tokens ---
message: 1
something: 1
line1: 1
🏗️ 项目结构
perl
复制代码
log-analyzer-cli/
│
├── week3/
│   ├── core/              # 核心逻辑模块
│   │   ├── model.py
│   │   ├── parse.py
│   │   └── stats.py
│   │
│   ├── utils/             # 工具模块（IO、输出、报告）
│   │   ├── io.py
│   │   ├── writer.py
│   │   ├── report.py
│   │   └── filedump.py
│   │
│   ├── sample/            # 示例日志文件
│   │   └── sample.log
│   │
│   ├── output/            # 输出结果文件夹（自动生成）
│   └── main.py            # 主入口（已注册为 log-analyze 命令）
│
├── setup.py               # 包安装配置
├── requirements.txt       # 依赖清单
└── README.md              # 项目说明
🧩 开发与调试
在本地调试时可以直接运行：

bash
复制代码
python -m week3.main -i week3/sample/sample.log
🧑‍💻 作者
Zhu Wenqiang (WhyNotY)
邮箱：1785560449@qq.com
>>>>>>> a6976b9 (更新本地 README.md)
