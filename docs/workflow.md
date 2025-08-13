# Minerva Milestone 1 - Code Workflow & Architecture (Legacy)

> **重要说明**: 这个文档包含了过度工程化的设计，已被更简单的通用记忆机制取代。
>
> **当前方法**: 参考 [design_v2.md](design_v2.md) 了解基于通用记忆机制的新架构。
>
> **项目状态**: 已重构为Hello World实现，准备基于新设计进行开发。

## Overview (Legacy)

This document describes the detailed code workflow and architecture for implementing Milestone 1: Basic Memory Storage. It provides a technical roadmap for completing the remaining tasks and achieving the first working demo.

**Note**: The architecture described here was overly complex and domain-specific. The new approach focuses on universal memory mechanisms.

## Current Status

### ✅ Completed Components
- **Project Structure**: uv-based Python package with proper organization
- **Core Memory Classes**: `MemorySegment` and `MemoryStore` with full functionality
- **CLI Framework**: Rich-formatted command interface with all command stubs
- **Test Suite**: Comprehensive tests for memory system (8/8 passing)
- **Documentation**: Complete design and execution plans

### 🔄 Remaining Tasks for Milestone 1
- **Task 1.4**: Complete CLI functionality with actual memory operations
- **Task 1.5**: Integrate CLI with memory system for working demo

## Architecture Deep Dive

### 1. Memory System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CLI Layer (cli.py)                      │
├─────────────────────────────────────────────────────────────┤
│                 Memory Service Layer                       │
│  ┌─────────────────┐  ┌─────────────────┐                 │
│  │  MemoryManager  │  │ MemoryRetrieval │                 │
│  │   (new class)   │  │   (new class)   │                 │
│  └─────────────────┘  └─────────────────┘                 │
├─────────────────────────────────────────────────────────────┤
│                 Core Memory Layer                          │
│  ┌─────────────────┐  ┌─────────────────┐                 │
│  │  MemorySegment  │  │   MemoryStore   │                 │
│  │   (complete)    │  │   (complete)    │                 │
│  └─────────────────┘  └─────────────────┘                 │
└─────────────────────────────────────────────────────────────┘
```

### 2. Data Flow Architecture

```
User Input → CLI Command → MemoryManager → MemoryStore → Query Results
     ↑                          ↓              ↓              ↓
     └─────── Rich Formatted Output ←─── MemoryRetrieval ←─────┘
```

## Implementation Workflow

### Task 1.4: Complete CLI Functionality

#### 1.4.1 Create MemoryManager Service Class

**File**: `src/minerva/manager.py`

```python
class MemoryManager:
    """High-level service for managing memory operations"""
    
    def __init__(self, store: MemoryStore):
        self.store = store
        self.retrieval = MemoryRetrieval(store)
    
    def add_memory(self, content: str, memory_type: MemoryType = MemoryType.BASIC_INFO) -> str:
        """Add a new memory from user input"""
        # Parse content and create structured memory
        # Return memory ID
    
    def query_memory(self, query: str) -> Dict[str, Any]:
        """Query memories and return relevant results"""
        # Search memories and format response
        # Return structured answer with sources
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get comprehensive memory statistics"""
        # Aggregate stats from store
        # Return formatted statistics
```

**Implementation Steps**:
1. Create the file with basic class structure
2. Implement `add_memory()` method with content parsing
3. Implement `query_memory()` method with search logic
4. Implement `get_statistics()` method with rich formatting
5. Add error handling and validation

#### 1.4.2 Create MemoryRetrieval Service Class

**File**: `src/minerva/retrieval.py`

```python
class MemoryRetrieval:
    """Intelligent memory retrieval and ranking"""
    
    def __init__(self, store: MemoryStore):
        self.store = store
    
    def search_and_rank(self, query: str) -> List[MemorySegment]:
        """Search memories and rank by relevance"""
        # Implement keyword matching
        # Add importance-based ranking
        # Return sorted results
    
    def format_response(self, memories: List[MemorySegment], query: str) -> str:
        """Format search results into human-readable response"""
        # Create natural language response
        # Include memory sources and confidence
        # Handle no-results case
```

**Implementation Steps**:
1. Create basic search functionality
2. Add relevance scoring algorithm
3. Implement response formatting
4. Add query preprocessing (lowercase, tokenization)
5. Handle edge cases (no results, empty query)

#### 1.4.3 Update CLI Commands

**File**: `src/minerva/cli.py`

**Changes needed**:
```python
# Add imports
from .manager import MemoryManager
from .memory import memory_store

# Initialize manager
memory_manager = MemoryManager(memory_store)

@main.command()
@click.argument("content")
def add_memory(content):
    """Add a new memory to the system"""
    try:
        memory_id = memory_manager.add_memory(content)
        console.print(f"✓ Memory stored: [green]{content}[/green]")
        console.print(f"💾 Memory ID: [dim]{memory_id}[/dim]")
    except Exception as e:
        console.print(f"❌ Error: {e}", style="red")

@main.command()
@click.argument("query")
def ask(query):
    """Ask a question and retrieve relevant memories"""
    try:
        response = memory_manager.query_memory(query)
        console.print(f"🤔 You asked: [blue]{query}[/blue]")
        
        if response['memories']:
            console.print("\n📚 Found relevant memories:")
            console.print(response['answer'])
            console.print(f"\n[dim]Sources: {len(response['memories'])} memories[/dim]")
        else:
            console.print("[yellow]No relevant memories found.[/yellow]")
            console.print("[dim]💡 Try adding some memories first![/dim]")
    except Exception as e:
        console.print(f"❌ Error: {e}", style="red")

@main.command()
def stats():
    """Show memory statistics and system status"""
    try:
        stats = memory_manager.get_statistics()
        
        table = Table(title="🧠 Memory Statistics")
        table.add_column("Type", style="cyan", no_wrap=True)
        table.add_column("Count", style="magenta", justify="right")
        table.add_column("Status", style="green")
        
        for stat_type, count in stats['type_counts'].items():
            status = "Active" if count > 0 else "Empty"
            table.add_row(stat_type.replace('_', ' ').title(), str(count), status)
        
        console.print(table)
        
        if stats['total_memories'] > 0:
            console.print(f"\n📊 Most accessed: [bold]{stats['most_accessed']['content']}[/bold]")
            console.print(f"🕒 Most recent: [dim]{stats['most_recent']['timestamp']}[/dim]")
        else:
            console.print("\n[dim]💡 Tip: Start by adding memories with 'minerva add-memory <content>'[/dim]")
            
    except Exception as e:
        console.print(f"❌ Error: {e}", style="red")
```

### Task 1.5: First Working Demo

#### 1.5.1 Integration Testing

**File**: `tests/test_integration.py`

```python
"""Integration tests for the complete memory system"""

def test_complete_workflow():
    """Test the complete add-memory -> ask workflow"""
    manager = MemoryManager(MemoryStore())
    
    # Add some memories
    id1 = manager.add_memory("My GitHub username is laofeizhu")
    id2 = manager.add_memory("I prefer Python for AI projects")
    
    # Query memories
    response1 = manager.query_memory("What is my GitHub username?")
    response2 = manager.query_memory("What language do I prefer?")
    
    # Verify responses
    assert "laofeizhu" in response1['answer']
    assert "Python" in response2['answer']
    assert len(response1['memories']) > 0

def test_cli_commands():
    """Test CLI commands work end-to-end"""
    # Use click.testing.CliRunner to test CLI
    from click.testing import CliRunner
    from minerva.cli import main
    
    runner = CliRunner()
    
    # Test add-memory
    result = runner.invoke(main, ['add-memory', 'Test memory content'])
    assert result.exit_code == 0
    assert "Memory stored" in result.output
    
    # Test ask
    result = runner.invoke(main, ['ask', 'Test'])
    assert result.exit_code == 0
    
    # Test stats
    result = runner.invoke(main, ['stats'])
    assert result.exit_code == 0
    assert "Memory Statistics" in result.output
```

#### 1.5.2 Demo Script

**File**: `examples/demo.py`

```python
"""
Minerva Milestone 1 Demo Script
Demonstrates the basic memory functionality
"""

from minerva.manager import MemoryManager
from minerva.memory import MemoryStore
from rich.console import Console

console = Console()

def run_demo():
    """Run the Milestone 1 demo"""
    console.print("[bold blue]Minerva Milestone 1 Demo[/bold blue]")
    console.print("Demonstrating basic memory storage and retrieval\n")
    
    # Initialize system
    store = MemoryStore()
    manager = MemoryManager(store)
    
    # Demo 1: Add memories
    console.print("[bold]1. Adding memories...[/bold]")
    memories = [
        "My GitHub username is laofeizhu",
        "I prefer Python for AI development",
        "My favorite framework is FastAPI",
        "I use uv for Python package management"
    ]
    
    for memory in memories:
        memory_id = manager.add_memory(memory)
        console.print(f"  ✓ Added: {memory}")
    
    # Demo 2: Ask questions
    console.print("\n[bold]2. Asking questions...[/bold]")
    questions = [
        "What is my GitHub username?",
        "What language do I prefer?",
        "What package manager do I use?",
        "Tell me about my preferences"
    ]
    
    for question in questions:
        console.print(f"\n  🤔 Q: {question}")
        response = manager.query_memory(question)
        console.print(f"  💡 A: {response['answer']}")
    
    # Demo 3: Show statistics
    console.print("\n[bold]3. Memory statistics...[/bold]")
    stats = manager.get_statistics()
    console.print(f"  📊 Total memories: {stats['total_memories']}")
    console.print(f"  🔍 Search capability: Active")
    console.print(f"  💾 Storage: In-memory (temporary)")
    
    console.print("\n[green]✅ Milestone 1 Demo Complete![/green]")
    console.print("[dim]Next: Milestone 2 will add programming-specific memory types[/dim]")

if __name__ == "__main__":
    run_demo()
```

## Implementation Priority

### Phase 1: Core Service Layer (Days 1-2)
1. Create `MemoryManager` class with basic functionality
2. Create `MemoryRetrieval` class with simple search
3. Write unit tests for new classes

### Phase 2: CLI Integration (Days 2-3)
1. Update CLI commands to use `MemoryManager`
2. Add proper error handling and user feedback
3. Test CLI commands manually

### Phase 3: Demo and Polish (Days 3-4)
1. Create integration tests
2. Build demo script
3. Test complete workflow
4. Polish error messages and user experience

### Phase 4: Documentation and Validation (Day 4-5)
1. Update README with working examples
2. Create usage examples
3. Validate against Milestone 1 requirements
4. Prepare for Milestone 2

## Success Criteria

### Functional Requirements
- ✅ User can add memories via CLI
- ✅ User can ask questions and get relevant answers
- ✅ System shows meaningful statistics
- ✅ All commands work without errors
- ✅ Memory persistence during session

### Technical Requirements
- ✅ Clean separation of concerns (CLI → Service → Storage)
- ✅ Comprehensive error handling
- ✅ Rich, user-friendly output formatting
- ✅ Test coverage > 80%
- ✅ Code follows project style guidelines

### User Experience Requirements
- ✅ Commands are intuitive and self-explanatory
- ✅ Error messages are helpful and actionable
- ✅ Output is visually appealing and informative
- ✅ System provides guidance for next steps

## File Structure After Completion

```
src/minerva/
├── __init__.py          # Package exports
├── cli.py              # ✅ Updated CLI with full functionality
├── memory.py           # ✅ Core memory classes (complete)
├── manager.py          # 🆕 High-level memory management
└── retrieval.py        # 🆕 Memory search and retrieval

tests/
├── __init__.py
├── test_memory.py      # ✅ Core memory tests (complete)
├── test_manager.py     # 🆕 Manager service tests
├── test_retrieval.py   # 🆕 Retrieval service tests
└── test_integration.py # 🆕 End-to-end integration tests

examples/
└── demo.py             # 🆕 Milestone 1 demonstration
```

This workflow provides a clear path to complete Milestone 1 with a working, testable, and demonstrable memory system that serves as the foundation for all future milestones.

---

# Milestone 2 - Programming Memory Specialization

## Overview

Milestone 2 builds upon the basic memory system to add specialized memory types and processing logic specifically designed for programming tasks. This milestone transforms Minerva from a general memory system into a coding-focused assistant.

## Architecture Evolution

### Enhanced Memory System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CLI Layer (cli.py)                      │
├─────────────────────────────────────────────────────────────┤
│              Programming Service Layer                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │ CodebaseAnalyzer│  │  ErrorLearner   │  │StyleLearner │ │
│  │   (new class)   │  │   (new class)   │  │ (new class) │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                 Memory Service Layer                       │
│  ┌─────────────────┐  ┌─────────────────┐                 │
│  │  MemoryManager  │  │ MemoryRetrieval │                 │
│  │   (enhanced)    │  │   (enhanced)    │                 │
│  └─────────────────┘  └─────────────────┘                 │
├─────────────────────────────────────────────────────────────┤
│              Specialized Memory Types                      │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐ │
│  │ CodebaseMemory  │  │  ErrorMemory    │  │ StyleMemory │ │
│  │   (new class)   │  │   (new class)   │  │ (new class) │ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                 Core Memory Layer                          │
│  ┌─────────────────┐  ┌─────────────────┐                 │
│  │  MemorySegment  │  │   MemoryStore   │                 │
│  │   (complete)    │  │   (complete)    │                 │
│  └─────────────────┘  └─────────────────┘                 │
└─────────────────────────────────────────────────────────────┘
```

## Implementation Workflow

### Task 2.1: Implement Programming Memory Types

#### 2.1.1 Create Specialized Memory Classes

**File**: `src/minerva/coding_memory.py`

```python
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from .memory import MemorySegment, MemoryType

@dataclass
class CodebaseMemory(MemorySegment):
    """Specialized memory for codebase analysis results"""

    def __init__(self, project_path: str, language: str, framework: str = None):
        super().__init__(memory_type=MemoryType.CODEBASE_ANALYSIS)
        self.content = {
            "type": "codebase_analysis",
            "project_info": {
                "name": self._extract_project_name(project_path),
                "path": project_path,
                "language": language,
                "framework": framework,
                "version": None
            },
            "architecture": {
                "pattern": None,  # MVC, MVP, Clean Architecture, etc.
                "layers": [],     # presentation, business, data, etc.
                "components": {}, # key modules and their responsibilities
                "dependencies": [] # external dependencies
            },
            "code_structure": {
                "entry_points": [],
                "config_files": [],
                "key_directories": {},
                "important_files": []
            },
            "workflows": {},  # key business processes
            "apis": [],       # API endpoints and their purposes
            "database": {     # database schema understanding
                "type": None,
                "models": [],
                "relationships": []
            }
        }
        self.analysis_depth = "shallow"  # shallow, medium, deep
        self.confidence_score = 0.0

    def _extract_project_name(self, path: str) -> str:
        """Extract project name from path"""
        return path.split('/')[-1] if '/' in path else path

@dataclass
class ErrorMemory(MemorySegment):
    """Specialized memory for error experiences and solutions"""

    def __init__(self, command: str, error_message: str, context: Dict[str, Any]):
        super().__init__(memory_type=MemoryType.ERROR_EXPERIENCE)
        self.content = {
            "type": "error_experience",
            "error_info": {
                "category": self._categorize_error(error_message),
                "tool_name": self._extract_tool_name(command),
                "command": command,
                "error_message": error_message,
                "error_code": None
            },
            "context": {
                "task": context.get("task", "unknown"),
                "environment": context.get("environment", "local"),
                "project_type": context.get("project_type", "unknown"),
                "language": context.get("language", "unknown")
            },
            "resolution": {
                "status": "unresolved",  # resolved, unresolved, workaround
                "solution": None,
                "alternative_approaches": [],
                "time_to_resolve": None,
                "confidence": 0.0
            },
            "prevention": {
                "check_command": None,
                "install_command": None,
                "environment_requirement": None
            }
        }
        self.recurrence_count = 1
        self.last_encountered = self.timestamp

    def _categorize_error(self, error_message: str) -> str:
        """Categorize error type based on message"""
        error_message_lower = error_message.lower()
        if "command not found" in error_message_lower:
            return "missing_dependency"
        elif "permission denied" in error_message_lower:
            return "permission_error"
        elif "syntax error" in error_message_lower:
            return "syntax_error"
        elif "import" in error_message_lower and "error" in error_message_lower:
            return "import_error"
        else:
            return "runtime_error"

    def _extract_tool_name(self, command: str) -> str:
        """Extract tool name from command"""
        return command.split()[0] if command else "unknown"

    def add_solution(self, solution: str, confidence: float = 0.8):
        """Add a solution to this error memory"""
        self.content["resolution"]["solution"] = solution
        self.content["resolution"]["status"] = "resolved"
        self.content["resolution"]["confidence"] = confidence
        self.importance_score = min(1.0, self.importance_score + 0.3)

@dataclass
class CodingStyleMemory(MemorySegment):
    """Specialized memory for coding style preferences"""

    def __init__(self, language: str, framework: str = None):
        super().__init__(memory_type=MemoryType.CODING_STYLE)
        self.content = {
            "type": "coding_style_preference",
            "language": language,
            "framework": framework,
            "style_preferences": {
                "naming_convention": {
                    "variables": None,  # camelCase, snake_case, etc.
                    "functions": None,
                    "classes": None,
                    "constants": None
                },
                "code_structure": {
                    "indentation": None,  # spaces, tabs
                    "line_length": None,
                    "blank_lines": {},
                    "import_organization": None
                },
                "documentation": {
                    "docstring_style": None,  # Google, NumPy, Sphinx
                    "comment_style": None,
                    "language": "english",  # English, Chinese, etc.
                    "detail_level": "moderate"  # minimal, moderate, detailed
                },
                "error_handling": {
                    "strategy": None,  # try-catch, return-codes, exceptions
                    "logging_level": None,
                    "user_messages": "user-friendly",
                    "message_language": "english"
                },
                "api_design": {
                    "response_format": {},
                    "status_codes": "semantic",
                    "parameter_validation": "explicit",
                    "authentication_style": None
                }
            },
            "patterns": {
                "preferred_patterns": [],  # design patterns user likes
                "avoided_patterns": [],    # patterns user dislikes
                "custom_patterns": []      # user's unique approaches
            }
        }
        self.confidence_level = 0.0
        self.sample_count = 0
        self.last_reinforced = self.timestamp

    def update_preference(self, category: str, subcategory: str, value: Any):
        """Update a specific style preference"""
        if category in self.content["style_preferences"]:
            if subcategory in self.content["style_preferences"][category]:
                self.content["style_preferences"][category][subcategory] = value
                self.sample_count += 1
                self.confidence_level = min(1.0, self.sample_count * 0.1)
                self.last_reinforced = time.time()
```

#### 2.1.2 Update Memory Types Enum

**File**: `src/minerva/memory.py`

```python
# Add to existing MemoryType enum
class MemoryType(Enum):
    """Types of memories in the Minerva system"""
    BASIC_INFO = "basic_info"
    CODEBASE_ANALYSIS = "codebase_analysis"
    ERROR_EXPERIENCE = "error_experience"
    CODING_STYLE = "coding_style_preference"
    CONVERSATION = "conversation"
    # Add new types for future milestones
    CODE_SNIPPET = "code_snippet"
    DEBUGGING_SESSION = "debugging_session"
```

### Task 2.2: Simple Code Analysis

#### 2.2.1 Create Code Analysis Service

**File**: `src/minerva/analyzers.py`

```python
import os
import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from .coding_memory import CodebaseMemory

class CodebaseAnalyzer:
    """Analyzes codebase structure and creates memory"""

    def __init__(self):
        self.supported_languages = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.java': 'java',
            '.go': 'go',
            '.rs': 'rust',
            '.cpp': 'cpp',
            '.c': 'c'
        }
        self.config_files = {
            'python': ['requirements.txt', 'pyproject.toml', 'setup.py', 'Pipfile'],
            'javascript': ['package.json', 'yarn.lock', 'package-lock.json'],
            'java': ['pom.xml', 'build.gradle', 'gradle.properties'],
            'go': ['go.mod', 'go.sum'],
            'rust': ['Cargo.toml', 'Cargo.lock']
        }

    def analyze_project(self, project_path: str) -> CodebaseMemory:
        """Analyze a project and create codebase memory"""
        project_path = os.path.abspath(project_path)

        # Detect primary language
        language = self._detect_primary_language(project_path)

        # Detect framework
        framework = self._detect_framework(project_path, language)

        # Create memory object
        memory = CodebaseMemory(project_path, language, framework)

        # Analyze structure
        self._analyze_structure(memory, project_path)

        # Analyze dependencies
        self._analyze_dependencies(memory, project_path)

        # Set confidence based on analysis depth
        memory.confidence_score = self._calculate_confidence(memory)

        return memory

    def _detect_primary_language(self, project_path: str) -> str:
        """Detect the primary programming language"""
        file_counts = {}

        for root, dirs, files in os.walk(project_path):
            # Skip hidden directories and common ignore patterns
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'target', 'build']]

            for file in files:
                ext = Path(file).suffix.lower()
                if ext in self.supported_languages:
                    lang = self.supported_languages[ext]
                    file_counts[lang] = file_counts.get(lang, 0) + 1

        if not file_counts:
            return "unknown"

        return max(file_counts, key=file_counts.get)

    def _detect_framework(self, project_path: str, language: str) -> Optional[str]:
        """Detect framework based on files and dependencies"""
        if language == "python":
            return self._detect_python_framework(project_path)
        elif language == "javascript":
            return self._detect_js_framework(project_path)
        return None

    def _detect_python_framework(self, project_path: str) -> Optional[str]:
        """Detect Python framework"""
        # Check for common framework files
        framework_indicators = {
            'flask': ['app.py', 'application.py', 'wsgi.py'],
            'django': ['manage.py', 'settings.py', 'urls.py'],
            'fastapi': ['main.py', 'app.py'],
            'streamlit': ['streamlit_app.py', 'app.py']
        }

        for framework, indicators in framework_indicators.items():
            for indicator in indicators:
                if os.path.exists(os.path.join(project_path, indicator)):
                    return framework

        # Check requirements.txt for framework dependencies
        req_file = os.path.join(project_path, 'requirements.txt')
        if os.path.exists(req_file):
            with open(req_file, 'r') as f:
                content = f.read().lower()
                if 'flask' in content:
                    return 'flask'
                elif 'django' in content:
                    return 'django'
                elif 'fastapi' in content:
                    return 'fastapi'

        return None

    def _detect_js_framework(self, project_path: str) -> Optional[str]:
        """Detect JavaScript framework"""
        package_json = os.path.join(project_path, 'package.json')
        if os.path.exists(package_json):
            try:
                with open(package_json, 'r') as f:
                    data = json.load(f)
                    deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}

                    if 'react' in deps:
                        return 'react'
                    elif 'vue' in deps:
                        return 'vue'
                    elif 'angular' in deps or '@angular/core' in deps:
                        return 'angular'
                    elif 'express' in deps:
                        return 'express'
            except json.JSONDecodeError:
                pass

        return None

    def _analyze_structure(self, memory: CodebaseMemory, project_path: str):
        """Analyze project structure"""
        structure_info = {
            "total_files": 0,
            "directories": [],
            "key_files": []
        }

        for root, dirs, files in os.walk(project_path):
            # Skip hidden and build directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__', 'target', 'build']]

            rel_root = os.path.relpath(root, project_path)
            if rel_root != '.':
                structure_info["directories"].append(rel_root)

            for file in files:
                if not file.startswith('.'):
                    structure_info["total_files"] += 1

                    # Identify key files
                    if file in ['README.md', 'LICENSE', 'Dockerfile', 'docker-compose.yml']:
                        structure_info["key_files"].append(os.path.join(rel_root, file))

        memory.content["code_structure"]["key_directories"] = structure_info["directories"][:10]  # Limit to top 10
        memory.content["code_structure"]["important_files"] = structure_info["key_files"]
        memory.semantic_info["total_files"] = structure_info["total_files"]

    def _analyze_dependencies(self, memory: CodebaseMemory, project_path: str):
        """Analyze project dependencies"""
        language = memory.content["project_info"]["language"]
        config_files = self.config_files.get(language, [])

        dependencies = []
        for config_file in config_files:
            config_path = os.path.join(project_path, config_file)
            if os.path.exists(config_path):
                memory.content["code_structure"]["config_files"].append(config_file)
                deps = self._extract_dependencies(config_path, config_file)
                dependencies.extend(deps)

        memory.content["architecture"]["dependencies"] = dependencies[:20]  # Limit to top 20

    def _extract_dependencies(self, config_path: str, config_file: str) -> List[str]:
        """Extract dependencies from config file"""
        dependencies = []

        try:
            if config_file == 'requirements.txt':
                with open(config_path, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            dep = line.split('==')[0].split('>=')[0].split('<=')[0]
                            dependencies.append(dep)

            elif config_file == 'package.json':
                with open(config_path, 'r') as f:
                    data = json.load(f)
                    deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                    dependencies.extend(list(deps.keys()))

            elif config_file == 'pyproject.toml':
                # Simple TOML parsing for dependencies
                with open(config_path, 'r') as f:
                    content = f.read()
                    if 'dependencies = [' in content:
                        # Extract dependencies from pyproject.toml
                        # This is a simplified parser
                        pass

        except Exception:
            pass  # Ignore parsing errors

        return dependencies

    def _calculate_confidence(self, memory: CodebaseMemory) -> float:
        """Calculate confidence score based on analysis completeness"""
        score = 0.0

        # Language detection
        if memory.content["project_info"]["language"] != "unknown":
            score += 0.3

        # Framework detection
        if memory.content["project_info"]["framework"]:
            score += 0.2

        # Structure analysis
        if memory.content["code_structure"]["key_directories"]:
            score += 0.2

        # Dependencies
        if memory.content["architecture"]["dependencies"]:
            score += 0.2

        # Config files
        if memory.content["code_structure"]["config_files"]:
            score += 0.1

        return min(1.0, score)
```

### Task 2.3: Error Capture Mechanism

#### 2.3.1 Create Error Learning Service

**File**: `src/minerva/error_learner.py`

```python
import subprocess
import time
from typing import Dict, List, Any, Optional, Tuple
from .coding_memory import ErrorMemory
from .memory import MemoryStore

class ErrorLearner:
    """Learns from command execution errors"""

    def __init__(self, memory_store: MemoryStore):
        self.memory_store = memory_store
        self.known_solutions = {
            "pytest: command not found": "python -m pytest",
            "black: command not found": "python -m black",
            "flake8: command not found": "python -m flake8",
            "mypy: command not found": "python -m mypy",
            "pip: command not found": "python -m pip",
        }

    def execute_with_learning(self, command: str, context: Dict[str, Any] = None) -> Tuple[bool, str, Optional[ErrorMemory]]:
        """Execute command and learn from any errors"""
        context = context or {}

        # Check if we've seen this error before
        similar_error = self._find_similar_error(command)
        if similar_error and similar_error.content["resolution"]["status"] == "resolved":
            # Try the known solution first
            solution = similar_error.content["resolution"]["solution"]
            success, output = self._execute_command(solution)
            if success:
                return True, output, None

        # Execute the original command
        success, output = self._execute_command(command)

        if success:
            return True, output, None

        # Command failed, create error memory
        error_memory = ErrorMemory(command, output, context)

        # Try to find a solution
        solution = self._suggest_solution(command, output)
        if solution:
            # Test the solution
            solution_success, solution_output = self._execute_command(solution)
            if solution_success:
                error_memory.add_solution(solution, confidence=0.9)
                self.memory_store.add_memory(error_memory)
                return True, solution_output, error_memory

        # No solution found, store the error for future learning
        self.memory_store.add_memory(error_memory)
        return False, output, error_memory

    def _execute_command(self, command: str) -> Tuple[bool, str]:
        """Execute a shell command and return success status and output"""
        try:
            result = subprocess.run(
                command.split(),
                capture_output=True,
                text=True,
                timeout=30
            )
            return result.returncode == 0, result.stdout if result.returncode == 0 else result.stderr
        except subprocess.TimeoutExpired:
            return False, "Command timed out"
        except FileNotFoundError:
            return False, f"{command.split()[0]}: command not found"
        except Exception as e:
            return False, str(e)

    def _find_similar_error(self, command: str) -> Optional[ErrorMemory]:
        """Find similar error in memory"""
        error_memories = self.memory_store.get_memories_by_type(MemoryType.ERROR_EXPERIENCE)

        for memory in error_memories:
            if isinstance(memory, ErrorMemory):
                stored_command = memory.content["error_info"]["command"]
                if stored_command == command:
                    return memory

                # Check for similar tool
                stored_tool = memory.content["error_info"]["tool_name"]
                current_tool = command.split()[0]
                if stored_tool == current_tool:
                    return memory

        return None

    def _suggest_solution(self, command: str, error_message: str) -> Optional[str]:
        """Suggest a solution based on error patterns"""
        # Check known solutions
        for error_pattern, solution in self.known_solutions.items():
            if error_pattern in error_message:
                return solution

        # Pattern-based suggestions
        if "command not found" in error_message:
            tool = command.split()[0]
            return f"python -m {tool}"

        if "permission denied" in error_message.lower():
            return f"sudo {command}"

        if "module not found" in error_message.lower():
            # Extract module name and suggest installation
            if "No module named" in error_message:
                module = error_message.split("No module named '")[1].split("'")[0]
                return f"pip install {module}"

        return None
```

### Task 2.4: Programming Task CLI

#### 2.4.1 Update CLI with Programming Commands

**File**: `src/minerva/cli.py` (additions)

```python
# Add imports
from .analyzers import CodebaseAnalyzer
from .error_learner import ErrorLearner
from .coding_memory import CodebaseMemory, ErrorMemory

# Initialize programming services
codebase_analyzer = CodebaseAnalyzer()
error_learner = ErrorLearner(memory_store)

@main.command()
@click.argument("path", type=click.Path(exists=True))
def analyze_code(path):
    """Analyze a codebase and store architectural knowledge"""
    try:
        console.print(f"🔍 Analyzing codebase at: [blue]{path}[/blue]")

        with console.status("[bold green]Analyzing project structure..."):
            codebase_memory = codebase_analyzer.analyze_project(path)

        # Store the memory
        memory_id = memory_store.add_memory(codebase_memory)

        # Display results
        project_info = codebase_memory.content["project_info"]
        console.print(f"✅ [green]Analysis complete![/green]")
        console.print(f"📊 Language: [cyan]{project_info['language']}[/cyan]")

        if project_info['framework']:
            console.print(f"🏗️  Framework: [cyan]{project_info['framework']}[/cyan]")

        console.print(f"📁 Files analyzed: [yellow]{codebase_memory.semantic_info.get('total_files', 'N/A')}[/yellow]")
        console.print(f"🎯 Confidence: [green]{codebase_memory.confidence_score:.1%}[/green]")
        console.print(f"💾 Memory ID: [dim]{memory_id}[/dim]")

    except Exception as e:
        console.print(f"❌ Error analyzing codebase: {e}", style="red")

@main.command()
@click.argument("command")
@click.option("--context", help="Additional context for the command")
def run_command(command, context):
    """Run a command and learn from any errors"""
    try:
        console.print(f"🚀 Executing: [blue]{command}[/blue]")

        # Parse context if provided
        context_dict = {}
        if context:
            try:
                context_dict = dict(item.split("=") for item in context.split(","))
            except ValueError:
                console.print("⚠️  Invalid context format. Use key=value,key2=value2", style="yellow")

        # Execute with learning
        success, output, error_memory = error_learner.execute_with_learning(command, context_dict)

        if success:
            console.print("✅ [green]Command executed successfully![/green]")
            if error_memory:
                console.print("🧠 [blue]Learned from previous error and applied solution[/blue]")
            console.print(f"📤 Output:\n{output}")
        else:
            console.print("❌ [red]Command failed[/red]")
            console.print(f"📤 Error:\n{output}")

            if error_memory:
                if error_memory.content["resolution"]["status"] == "resolved":
                    console.print("🧠 [green]Found and applied solution![/green]")
                else:
                    console.print("🧠 [yellow]Error recorded for future learning[/yellow]")
                    console.print(f"💾 Error memory ID: [dim]{error_memory.id}[/dim]")

    except Exception as e:
        console.print(f"❌ Execution error: {e}", style="red")

@main.command()
def list_errors():
    """List all learned errors and their solutions"""
    try:
        error_memories = memory_store.get_memories_by_type(MemoryType.ERROR_EXPERIENCE)

        if not error_memories:
            console.print("[yellow]No errors learned yet.[/yellow]")
            console.print("[dim]💡 Try running commands with 'minerva run-command <command>'[/dim]")
            return

        table = Table(title="🐛 Learned Errors")
        table.add_column("Tool", style="cyan", no_wrap=True)
        table.add_column("Error Type", style="yellow")
        table.add_column("Status", style="green")
        table.add_column("Solution", style="blue")

        for memory in error_memories:
            if isinstance(memory, ErrorMemory):
                error_info = memory.content["error_info"]
                resolution = memory.content["resolution"]

                solution = resolution.get("solution", "None")
                if len(solution) > 30:
                    solution = solution[:27] + "..."

                table.add_row(
                    error_info["tool_name"],
                    error_info["category"],
                    resolution["status"],
                    solution
                )

        console.print(table)

    except Exception as e:
        console.print(f"❌ Error listing errors: {e}", style="red")
```

## Implementation Priority for Milestone 2

### Phase 1: Specialized Memory Types (Days 6-7)
1. Create `coding_memory.py` with specialized classes
2. Update `MemoryType` enum
3. Write unit tests for new memory types
4. Test memory creation and serialization

### Phase 2: Code Analysis (Days 7-8)
1. Create `analyzers.py` with `CodebaseAnalyzer`
2. Implement language and framework detection
3. Add structure and dependency analysis
4. Test with various project types

### Phase 3: Error Learning (Days 8-9)
1. Create `error_learner.py` with `ErrorLearner`
2. Implement command execution with error capture
3. Add solution suggestion logic
4. Test error learning and solution application

### Phase 4: CLI Integration (Days 9-10)
1. Update CLI with new commands
2. Integrate analyzers and error learner
3. Add rich formatting for programming outputs
4. Test complete programming workflow

## Success Criteria for Milestone 2

### Functional Requirements
- ✅ Analyze codebase and store architectural knowledge
- ✅ Execute commands and learn from errors
- ✅ Apply learned solutions to prevent repeat errors
- ✅ Display programming-specific statistics
- ✅ Support multiple programming languages

### Technical Requirements
- ✅ Specialized memory types for programming tasks
- ✅ Intelligent error categorization and solution matching
- ✅ Codebase analysis with confidence scoring
- ✅ Integration with existing memory system
- ✅ Comprehensive test coverage

### User Experience Requirements
- ✅ Clear feedback on analysis progress and results
- ✅ Helpful error messages and solution suggestions
- ✅ Visual indicators for learning and solution application
- ✅ Easy-to-understand programming statistics

## File Structure After Milestone 2

```
src/minerva/
├── __init__.py              # Updated exports
├── cli.py                  # ✅ Enhanced with programming commands
├── memory.py               # ✅ Updated MemoryType enum
├── manager.py              # ✅ From Milestone 1
├── retrieval.py            # ✅ From Milestone 1
├── coding_memory.py        # 🆕 Specialized memory classes
├── analyzers.py            # 🆕 Codebase analysis service
└── error_learner.py        # 🆕 Error learning service

tests/
├── test_memory.py          # ✅ From Milestone 1
├── test_manager.py         # ✅ From Milestone 1
├── test_integration.py     # ✅ From Milestone 1
├── test_coding_memory.py   # 🆕 Specialized memory tests
├── test_analyzers.py       # 🆕 Code analysis tests
└── test_error_learner.py   # 🆕 Error learning tests

examples/
├── demo.py                 # ✅ From Milestone 1
└── programming_demo.py     # 🆕 Programming features demo
```

This completes the detailed workflow for Milestone 2, transforming Minerva into a specialized programming assistant with codebase understanding and error learning capabilities.
```
