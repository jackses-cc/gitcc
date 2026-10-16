"""项目入口文件。

运行方式（在仓库根 D:\\github\\git 下执行）：

    .\\.venv\\Scripts\\python.exe main.py

或在 VS Code 中直接按 F5 / 点右上角运行按钮（会自动使用 .venv 解释器）。
"""

from __future__ import annotations

from dotenv import load_dotenv

from src.example import greet

# 读取仓库根目录的 .env（该文件已被 .gitignore 忽略，适合存放密钥）
load_dotenv()


def main() -> None:
    """程序主逻辑，从这里开始写你的代码。"""
    print(greet())
    print(greet("Python"))


if __name__ == "__main__":
    main()
