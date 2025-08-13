# Minerva 快速开始指南 (使用uv)

> **当前状态**: Hello World实现
>
> 本指南帮助你设置Minerva开发环境。项目当前处于hello world阶段，为通用记忆系统奠定基础。

## 前置要求

### 安装uv
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 或者使用包管理器
brew install uv  # macOS
pip install uv   # 任何平台
```

### 验证安装
```bash
uv --version
# 应该显示类似: uv 0.4.x
```

## 项目初始化

### 1. 创建项目
```bash
# 创建新的Python项目
uv init minerva
cd minerva

# 查看生成的项目结构
tree .
```

### 2. 配置pyproject.toml
```toml
[project]
name = "minerva"
version = "0.1.0"
description = "A memory-based coding assistant inspired by human memory mechanisms"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
dependencies = [
    "click>=8.0.0",
    "rich>=13.0.0",
    "sqlalchemy>=2.0.0",
    "pydantic>=2.0.0",
]
requires-python = ">=3.9"

[project.scripts]
minerva = "minerva.cli:main"

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]
ai = [
    "torch>=2.0.0",
    "transformers>=4.30.0",
    "sentence-transformers>=2.2.0",
    "numpy>=1.24.0",
]
web = [
    "fastapi>=0.100.0",
    "uvicorn>=0.23.0",
    "jinja2>=3.1.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 88
target-version = "py39"

[tool.black]
line-length = 88
target-version = ['py39']

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
```

### 3. 创建基础项目结构
```bash
# 创建源代码目录
mkdir -p src/minerva
touch src/minerva/__init__.py
touch src/minerva/cli.py
touch src/minerva/memory.py
touch src/minerva/core.py

# 创建测试目录
mkdir tests
touch tests/__init__.py
touch tests/test_memory.py

# 创建其他目录
mkdir docs
mkdir examples
```

## 开发工作流

### 1. 安装依赖
```bash
# 安装基础依赖
uv sync

# 安装开发依赖
uv sync --extra dev

# 安装AI相关依赖（可选）
uv sync --extra ai

# 安装所有依赖
uv sync --all-extras
```

### 2. 运行代码
```bash
# 直接运行Python模块
uv run python -m minerva --help

# 使用项目脚本
uv run minerva --help

# 运行特定文件
uv run python src/minerva/cli.py
```

### 3. 开发和测试
```bash
# 运行测试
uv run pytest

# 运行测试并生成覆盖率报告
uv run pytest --cov=minerva

# 代码格式化
uv run black src/ tests/

# 代码检查
uv run ruff check src/ tests/

# 类型检查
uv run mypy src/
```

### 4. 添加新依赖
```bash
# 添加运行时依赖
uv add requests

# 添加开发依赖
uv add --dev pytest-mock

# 添加可选依赖组
uv add --optional ai torch

# 从requirements.txt添加
uv add -r requirements.txt
```

## 第一个可工作的版本

### 1. 创建基础CLI (src/minerva/cli.py)
```python
import click
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
@click.version_option(version="0.1.0")
def main():
    """Minerva - A memory-based coding assistant"""
    pass

@main.command()
@click.argument("content")
def add_memory(content):
    """Add a new memory"""
    console.print(f"✓ Memory stored: {content}", style="green")

@main.command()
@click.argument("query")
def ask(query):
    """Ask a question"""
    console.print(f"🤔 You asked: {query}", style="blue")
    console.print("I don't have any memories yet!", style="yellow")

@main.command()
def stats():
    """Show memory statistics"""
    table = Table(title="Memory Statistics")
    table.add_column("Type", style="cyan")
    table.add_column("Count", style="magenta")
    
    table.add_row("Total memories", "0")
    table.add_row("Codebase memories", "0")
    table.add_row("Error memories", "0")
    
    console.print(table)

if __name__ == "__main__":
    main()
```

### 2. 测试基础功能
```bash
# 安装项目（开发模式）
uv pip install -e .

# 测试CLI命令
uv run minerva --help
uv run minerva add-memory "Test memory"
uv run minerva ask "What do you remember?"
uv run minerva stats
```

## uv的优势体现

### 1. 快速依赖管理
```bash
# 传统方式
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# uv方式
uv sync  # 一条命令搞定
```

### 2. 环境隔离
```bash
# uv自动管理虚拟环境
uv run python --version  # 使用项目环境的Python
uv run which python      # 显示项目环境的Python路径
```

### 3. 锁文件管理
```bash
# uv.lock自动生成和维护
uv sync                   # 根据pyproject.toml更新uv.lock
uv sync --locked         # 严格按照uv.lock安装
```

### 4. Python版本管理
```bash
# uv可以管理Python版本
uv python install 3.11   # 安装Python 3.11
uv python pin 3.11       # 固定项目使用Python 3.11
```

## 常用命令速查

```bash
# 项目管理
uv init <project>         # 创建新项目
uv sync                   # 同步依赖
uv sync --extra dev       # 同步包含开发依赖

# 依赖管理
uv add <package>          # 添加依赖
uv remove <package>       # 移除依赖
uv tree                   # 显示依赖树

# 运行命令
uv run <command>          # 在项目环境中运行命令
uv run python <script>    # 运行Python脚本
uv run pytest            # 运行测试

# 环境管理
uv venv                   # 创建虚拟环境
uv pip list               # 列出已安装包
uv pip freeze             # 导出依赖列表
```

## 下一步

现在你已经有了一个基础的uv项目结构，可以开始实现Milestone 1的具体任务：

1. 完善CLI界面
2. 实现基础的MemorySegment类
3. 添加简单的内存存储
4. 实现第一个可工作的demo

使用uv让整个开发过程更加流畅和高效！
