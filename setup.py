from setuptools import setup, find_packages

setup(
    name="log-analyzer",                  # 包名
    version="1.0.0",                      # 版本号
    author="Zhu Wenqiang",                # 作者名
    author_email="2452420@example.com",   # 可以随意写
    description="A simple CLI log analyzer tool built in Python",
    packages=find_packages(),             # 自动找到 week3 及子包
    python_requires=">=3.10",             # Python 最低版本要求
    install_requires=[                    # 项目依赖
        "argparse",                       # 标准库可省略，这里仅示例
    ],
    entry_points={
    "console_scripts": [
        "log-analyze = log_analyzer.week3.main:main"
    ]
    },

)
