"""示例模块。

把你的业务逻辑写成这里的函数，然后在 main.py 中调用即可。

也可以直接运行本文件自测：

    .\\.venv\\Scripts\\python.exe src\\example.py
"""

from __future__ import annotations


def greet(name: str = "world") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """返回两数之和。"""
    return a + b


def _self_test() -> None:
    """本文件被直接运行时执行的简单自测。"""
    assert greet() == "Hello, world!"
    assert greet("Python") == "Hello, Python!"
    assert add(1, 2) == 3

    print("自测通过")
    print(greet())
    print(greet("Python"))
    print(f"add(1, 2) = {add(1, 2)}")


if __name__ == "__main__":
    _self_test()
