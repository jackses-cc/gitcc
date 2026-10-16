"""示例模块。

把你的业务逻辑写成这里的函数，然后在 main.py 中调用即可。
"""

from __future__ import annotations


def greet(name: str = "world") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """返回两数之和。"""
    return a + b
