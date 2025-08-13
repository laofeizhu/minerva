# Minerva Agent 编程记忆系统设计 (Legacy)

> **注意**: 这是针对编程任务的专门化设计，已被更通用的方案取代。
>
> **当前方法**: 使用通用记忆机制处理所有类型的经验，包括编程。参考 [design_v2.md](design_v2.md)。
>
> 本文档保留作为参考，展示了领域特定设计的详细思路。

## 概述

本文档详细描述了Minerva Agent针对编程任务优化的记忆系统设计，重点关注代码理解、错误学习和编程风格适应等核心功能。

**设计反思**: 这种专门化的方法违背了人类记忆的通用性原则。人类大脑不会为编程和生活创建不同的记忆系统。

## 编程记忆的特殊类型

### 1. 代码库记忆 (Codebase Memory)

```python
class CodebaseMemory(MemorySegment):
    def __init__(self):
        super().__init__()
        self.content = {
            "type": "codebase_analysis",
            "project_info": {
                "name": str,
                "path": str,
                "language": str,
                "framework": str,
                "version": str
            },
            "architecture": {
                "pattern": str,  # MVC, MVP, Clean Architecture, etc.
                "layers": [],    # presentation, business, data, etc.
                "components": {},  # key modules and their responsibilities
                "dependencies": []  # external dependencies
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
                "type": str,
                "models": [],
                "relationships": []
            }
        }
        self.analysis_depth = "deep"  # shallow, medium, deep
        self.last_updated = None
        self.confidence_score = 0.0
```

### 2. 错误记忆 (Error Memory)

```python
class ErrorMemory(MemorySegment):
    def __init__(self):
        super().__init__()
        self.content = {
            "type": "error_experience",
            "error_info": {
                "category": str,  # syntax, runtime, environment, logic
                "tool_name": str,
                "command": str,
                "error_message": str,
                "error_code": int
            },
            "context": {
                "task": str,
                "environment": str,  # local, docker, cloud, etc.
                "project_type": str,
                "language": str
            },
            "resolution": {
                "status": str,  # resolved, unresolved, workaround
                "solution": str,
                "alternative_approaches": [],
                "time_to_resolve": int,  # minutes
                "confidence": float
            },
            "prevention": {
                "check_command": str,  # command to check if issue exists
                "install_command": str,  # command to fix the issue
                "environment_requirement": str
            }
        }
        self.recurrence_count = 0
        self.last_encountered = None
```

### 3. 编程风格记忆 (Coding Style Memory)

```python
class CodingStyleMemory(MemorySegment):
    def __init__(self):
        super().__init__()
        self.content = {
            "type": "coding_style_preference",
            "language": str,
            "framework": str,
            "style_preferences": {
                "naming_convention": {
                    "variables": str,  # camelCase, snake_case, etc.
                    "functions": str,
                    "classes": str,
                    "constants": str
                },
                "code_structure": {
                    "indentation": str,  # spaces, tabs
                    "line_length": int,
                    "blank_lines": dict,
                    "import_organization": str
                },
                "documentation": {
                    "docstring_style": str,  # Google, NumPy, Sphinx
                    "comment_style": str,
                    "language": str,  # English, Chinese, etc.
                    "detail_level": str  # minimal, moderate, detailed
                },
                "error_handling": {
                    "strategy": str,  # try-catch, return-codes, exceptions
                    "logging_level": str,
                    "user_messages": str,  # technical, user-friendly
                    "message_language": str
                },
                "api_design": {
                    "response_format": dict,
                    "status_codes": str,  # semantic, numeric
                    "parameter_validation": str,
                    "authentication_style": str
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
        self.last_reinforced = None
```

## 专门的记忆处理器

### 1. 代码分析处理器 (Code Analysis Processor)

```python
class CodeAnalysisProcessor:
    def __init__(self):
        self.supported_languages = ['python', 'javascript', 'java', 'go', 'rust']
        self.analysis_tools = {
            'python': ['ast', 'pylint', 'mypy'],
            'javascript': ['esprima', 'eslint'],
            'java': ['javaparser'],
            'go': ['go/ast'],
            'rust': ['syn']
        }
    
    def analyze_codebase(self, project_path):
        """深度分析代码库结构"""
        analysis_result = {
            "structure": self._analyze_structure(project_path),
            "dependencies": self._analyze_dependencies(project_path),
            "patterns": self._identify_patterns(project_path),
            "complexity": self._calculate_complexity(project_path),
            "quality_metrics": self._assess_quality(project_path)
        }
        
        return self._create_codebase_memory(analysis_result)
    
    def _analyze_structure(self, project_path):
        """分析项目结构"""
        # 实现目录结构分析
        pass
    
    def _identify_patterns(self, project_path):
        """识别设计模式和架构模式"""
        # 实现模式识别逻辑
        pass
```

### 2. 错误学习处理器 (Error Learning Processor)

```python
class ErrorLearningProcessor:
    def __init__(self):
        self.error_patterns = {}
        self.solution_database = {}
        self.environment_checks = {}
    
    def process_error(self, error_info, context):
        """处理错误信息，创建错误记忆"""
        error_memory = ErrorMemory()
        error_memory.content["error_info"] = error_info
        error_memory.content["context"] = context
        
        # 尝试找到已知解决方案
        similar_errors = self._find_similar_errors(error_info)
        if similar_errors:
            error_memory.content["resolution"]["suggested_solutions"] = similar_errors
        
        return error_memory
    
    def suggest_solution(self, error_memory):
        """基于历史错误记忆建议解决方案"""
        error_signature = self._create_error_signature(error_memory)
        
        # 查找相似的已解决错误
        similar_resolved = self._query_resolved_errors(error_signature)
        
        if similar_resolved:
            return similar_resolved[0].content["resolution"]["solution"]
        
        return None
    
    def _create_error_signature(self, error_memory):
        """创建错误特征签名用于匹配"""
        return {
            "tool": error_memory.content["error_info"]["tool_name"],
            "error_type": error_memory.content["error_info"]["category"],
            "environment": error_memory.content["context"]["environment"]
        }
```

### 3. 风格学习处理器 (Style Learning Processor)

```python
class StyleLearningProcessor:
    def __init__(self):
        self.style_extractors = {
            'python': PythonStyleExtractor(),
            'javascript': JavaScriptStyleExtractor(),
            'java': JavaStyleExtractor()
        }
    
    def learn_from_code(self, original_code, modified_code, language):
        """从用户修改的代码中学习风格偏好"""
        extractor = self.style_extractors.get(language)
        if not extractor:
            return None
        
        original_style = extractor.extract_style(original_code)
        modified_style = extractor.extract_style(modified_code)
        
        # 分析差异，提取偏好
        style_preferences = self._analyze_style_differences(
            original_style, modified_style
        )
        
        return self._create_style_memory(style_preferences, language)
    
    def apply_style(self, code, language, style_memory):
        """将学到的风格应用到新代码"""
        extractor = self.style_extractors.get(language)
        if not extractor:
            return code
        
        preferences = style_memory.content["style_preferences"]
        return extractor.apply_style(code, preferences)
```

## 记忆检索优化

### 1. 编程任务特定的检索策略

```python
class CodingMemoryRetrieval(MemoryRetrieval):
    def __init__(self, memory_network):
        super().__init__(memory_network)
        self.coding_retrievers = {
            "codebase_query": self._retrieve_codebase_knowledge,
            "error_query": self._retrieve_error_solutions,
            "style_query": self._retrieve_style_preferences
        }
    
    def retrieve_for_coding_task(self, task_type, query, context):
        """针对编程任务的专门检索"""
        retriever = self.coding_retrievers.get(task_type)
        if retriever:
            return retriever(query, context)
        
        return self.retrieve_memories(query, context)
    
    def _retrieve_codebase_knowledge(self, query, context):
        """检索代码库相关知识"""
        # 基于项目路径、语言、框架等检索
        filters = {
            "type": "codebase_analysis",
            "project_path": context.get("project_path"),
            "language": context.get("language")
        }
        return self._filtered_retrieval(query, filters)
    
    def _retrieve_error_solutions(self, query, context):
        """检索错误解决方案"""
        filters = {
            "type": "error_experience",
            "resolution.status": "resolved",
            "context.environment": context.get("environment")
        }
        return self._filtered_retrieval(query, filters)
```

## 实际应用场景

### 1. 智能代码生成

```python
def generate_code_with_memory(self, task_description, context):
    """基于记忆生成符合用户风格的代码"""
    # 1. 检索用户编程风格
    style_memories = self.memory_retrieval.retrieve_for_coding_task(
        "style_query", 
        f"{context['language']} {context['framework']}", 
        context
    )
    
    # 2. 检索相关代码库知识
    codebase_memories = self.memory_retrieval.retrieve_for_coding_task(
        "codebase_query",
        task_description,
        context
    )
    
    # 3. 生成代码
    base_code = self.code_generator.generate(task_description, context)
    
    # 4. 应用用户风格
    if style_memories:
        styled_code = self.style_processor.apply_style(
            base_code, 
            context['language'], 
            style_memories[0]
        )
        return styled_code
    
    return base_code
```

### 2. 智能错误处理

```python
def handle_execution_error(self, error_info, context):
    """智能处理执行错误"""
    # 1. 创建错误记忆
    error_memory = self.error_processor.process_error(error_info, context)
    
    # 2. 查找已知解决方案
    solution = self.error_processor.suggest_solution(error_memory)
    
    if solution:
        # 3. 应用已知解决方案
        return self._apply_solution(solution, context)
    else:
        # 4. 尝试新的解决方案并学习
        new_solution = self._try_solve_error(error_info, context)
        if new_solution:
            error_memory.content["resolution"] = new_solution
            self.memory_network.add_segment(error_memory)
        
        return new_solution
```

这种专门针对编程任务的记忆系统设计，能够让Minerva Agent在代码开发过程中真正做到"学习型"的智能助手，不断积累和应用编程知识。
