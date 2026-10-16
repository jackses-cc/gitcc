# AGENTS.md

本文件为 Codex 及其他 AI 编码助手提供本仓库的上下文与约定。

## 项目概览

- 语言：Python 3.13
- 入口文件：`main.py`
- 业务代码：`src/` 包
- 依赖清单：`requirements.txt`（requests、python-dotenv）

## 环境

- 虚拟环境位于 `.venv/`（已被 `.gitignore` 忽略）
- 运行程序（**cwd 必须是仓库根**）：

  ```powershell
  .\.venv\Scripts\python.exe main.py
  ```

- 激活虚拟环境：`.\.venv\Scripts\Activate.ps1`
- 安装依赖：`.\.venv\Scripts\python.exe -m pip install -r requirements.txt`

> 注意：VS Code 的工作区根是上一级目录 `d:\github`（非仓库），仓库根为 `d:\github\git`。

## 代码约定

- 所有回复、注释和提交信息使用**简体中文**
- 提交信息前缀：`feat:` / `fix:` / `chore:` / `docs:` / `refactor:`
- 新增模块放在 `src/` 下并加类型标注，然后从 `main.py` 调用
- 函数添加简短中文 docstring
- 使用 `from __future__ import annotations`，类型标注采用 PEP 604 写法

## 密钥管理

- 真实密钥写在 `.env`（已被 `.gitignore` 忽略），模板见 `.env.example`
- 通过 `load_dotenv()` 加载，代码中一律使用 `os.environ["XXX"]` 读取
- **严禁**把密钥硬编码进源码或提交到仓库

## 不要提交

`.venv/`、`.env`、`__pycache__/`、`*.pyc`（均已在 `.gitignore` 中配置）
