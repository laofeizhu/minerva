# Minerva 执行计划与进度追踪

## 项目概述
构建一个基于人类记忆机制的AI助手，使用**通用记忆机制**而非领域特定的实现。重点是模拟人类记忆的基本原理：关联网络、重要性评分、睡眠整理等。

## 技术选择

### 为什么选择uv？
- **极快的依赖解析**: uv比pip快10-100倍，适合频繁的依赖管理
- **现代项目管理**: 内置虚拟环境管理，无需手动创建venv
- **锁文件支持**: 自动生成uv.lock确保依赖版本一致性
- **简化工作流**: `uv run` 自动处理环境激活和依赖安装
- **Python版本管理**: 内置Python版本管理，无需pyenv
- **与现有工具兼容**: 完全兼容pip和requirements.txt

### 项目结构
```
minerva/
├── pyproject.toml          # uv项目配置
├── uv.lock                 # 锁定的依赖版本
├── src/minerva/            # 源代码
├── tests/                  # 测试代码
├── docs/                   # 文档
└── README.md
```

## 开发原则
- **简单性**: 每个milestone都足够简单，能看到明确的改变
- **渐进式**: 每一步都在前一步的基础上增加功能
- **可验证**: 每个milestone都有明确的验证标准

---

## 🎯 Milestone 1: 通用记忆系统基础 (Week 1)

### 目标
实现通用的记忆片段存储和基础关联功能，为所有类型的学习和记忆奠定基础

### 任务列表
- [ ] **1.1 创建项目结构** (Day 1)
  - 使用uv创建Python项目：`uv init minerva`
  - 配置pyproject.toml和依赖管理
  - 初始化Git仓库
  - **验证**: 能运行`uv run python -m minerva --version`

- [ ] **1.2 实现基础记忆片段类** (Day 1-2)
  - 创建`MemorySegment`基础类
  - 实现动态content字段
  - 添加时间戳和重要性评分
  - **验证**: 能创建和序列化记忆片段

- [ ] **1.3 实现内存存储** (Day 2-3)
  - 创建`MemoryStore`类
  - 实现添加、查询、更新记忆
  - 使用Python字典作为临时存储
  - **验证**: 能存储和检索记忆片段

- [ ] **1.4 基础CLI界面** (Day 3-4)
  - 创建简单的命令行界面
  - 实现`add-memory`和`get-memory`命令
  - **验证**: 能通过CLI添加和查询记忆

- [ ] **1.5 第一个可工作的demo** (Day 4-5)
  - 实现简单的问答功能
  - 能记住用户告诉它的信息
  - **验证**: 复现usecases.md中的基础信息记忆场景

### 预期输出
```bash
# 用户可以这样使用
$ uv run minerva add-memory "My GitHub username is john_doe"
✓ Memory stored with ID: mem_001

$ uv run minerva ask "What is my GitHub username?"
Your GitHub username is john_doe (stored 2 minutes ago)
```

---

## 🔗 Milestone 2: 关联网络系统 (Week 2)

### 目标
实现记忆片段之间的关联机制，让系统能够建立记忆网络并发现相关经验

### 任务列表
- [ ] **2.1 实现关联构建器** (Day 6-7)
  - 创建`AssociationBuilder`类
  - 实现时间、语义、因果关联
  - 添加关联强度计算
  - **验证**: 能为新记忆自动建立关联

- [ ] **2.2 增强记忆检索** (Day 7-8)
  - 实现基于关联的记忆检索
  - 添加相关性评分算法
  - 支持多跳关联查询
  - **验证**: 能通过关联找到相关记忆

- [ ] **2.3 记忆重要性评分** (Day 8-9)
  - 实现动态重要性计算
  - 基于访问频率和关联强度
  - 添加时间衰减机制
  - **验证**: 重要记忆排序靠前

- [ ] **2.4 关联可视化** (Day 9-10)
  - 添加`show-associations`命令
  - 显示记忆网络结构
  - 展示关联强度和类型
  - **验证**: 能可视化记忆关联网络

### 预期输出
```bash
# 添加记忆并查看关联
$ uv run minerva add-memory "学习了Python装饰器的用法"
✓ Memory stored: 学习了Python装饰器的用法
🔗 Found 2 related memories, created associations

# 查看记忆关联
$ uv run minerva show-associations mem_001
📊 Memory: "学习了Python装饰器的用法"
🔗 Associations:
  - mem_002 (semantic, strength: 0.8): "Python函数定义语法"
  - mem_003 (temporal, strength: 0.6): "阅读Python文档"
  - mem_004 (causal, strength: 0.9): "遇到装饰器语法错误"
```

---

## 🔍 Milestone 3: 智能检索系统 (Week 3)

### 目标
实现基于关键词和语义的记忆检索功能

### 任务列表
- [ ] **3.1 关键词检索** (Day 11-12)
  - 实现基于关键词的记忆搜索
  - 支持模糊匹配和同义词
  - **验证**: 能通过关键词找到相关记忆

- [ ] **3.2 记忆关联网络** (Day 12-13)
  - 实现记忆片段之间的关联
  - 基于时间、主题、类型建立连接
  - **验证**: 相关记忆能互相关联

- [ ] **3.3 智能问答** (Day 13-14)
  - 实现基于记忆的问答功能
  - 能组合多个记忆片段回答问题
  - **验证**: 能回答复杂的编程相关问题

- [ ] **3.4 记忆重要性评分** (Day 14-15)
  - 实现动态重要性评分算法
  - 基于访问频率和时间衰减
  - **验证**: 重要记忆排序靠前

### 预期输出
```bash
$ uv run minerva ask "How do I run tests in my Flask project?"
Based on your project analysis (codebase_001) and previous error (error_003):
- Your Flask project uses pytest for testing
- Use 'python -m pytest tests/' to avoid installation issues
- Tests are located in the tests/ directory
```

---

## 🎨 Milestone 4: 编程风格学习 (Week 4)

### 目标
学习用户的编程风格偏好，并在代码生成中应用

### 任务列表
- [ ] **4.1 代码风格分析器** (Day 16-17)
  - 分析代码的命名规范、结构等
  - 提取用户的编程偏好
  - **验证**: 能识别用户的代码风格特征

- [ ] **4.2 风格学习机制** (Day 17-18)
  - 从用户修改的代码中学习偏好
  - 更新编程风格记忆
  - **验证**: 能从代码修改中学习风格

- [ ] **4.3 简单代码生成** (Day 18-19)
  - 实现基础的代码模板生成
  - 应用学到的用户风格
  - **验证**: 生成的代码符合用户风格

- [ ] **4.4 风格应用验证** (Day 19-20)
  - 完整的风格学习和应用流程
  - 用户反馈机制
  - **验证**: 复现usecases.md中的风格学习场景

### 预期输出
```bash
$ uv run minerva generate-api "user login endpoint"
Based on your coding style preferences:
✓ Using try-catch error handling
✓ Chinese error messages
✓ Consistent JSON response format
✓ Detailed parameter validation

Generated code saved to login_endpoint.py
```

---

## 💾 Milestone 5: 持久化存储 (Week 5)

### 目标
实现数据库存储，支持大量记忆的持久化和高效查询

### 任务列表
- [ ] **5.1 数据库设计** (Day 21-22)
  - 设计SQLite数据库schema
  - 实现记忆片段表和关联表
  - **验证**: 数据库能正确存储记忆结构

- [ ] **5.2 数据库集成** (Day 22-23)
  - 将内存存储替换为数据库存储
  - 实现数据迁移功能
  - **验证**: 所有功能在数据库存储下正常工作

- [ ] **5.3 查询优化** (Day 23-24)
  - 添加数据库索引
  - 优化复杂查询性能
  - **验证**: 大量记忆下查询仍然快速

- [ ] **5.4 数据备份恢复** (Day 24-25)
  - 实现记忆导出和导入功能
  - 支持数据备份和恢复
  - **验证**: 能完整备份和恢复所有记忆

### 预期输出
```bash
$ uv run minerva stats
Memory Statistics:
- Total memories: 1,247
- Codebase memories: 23
- Error memories: 156
- Style memories: 8
- Database size: 2.3 MB
- Average query time: 12ms
```

---

## 🚀 Milestone 6: 高级功能集成 (Week 6)

### 目标
集成所有功能，实现完整的编程助手体验

### 任务列表
- [ ] **6.1 记忆睡眠机制** (Day 26-27)
  - 实现记忆重要性衰减
  - 自动清理低价值记忆
  - **验证**: 系统能自动维护记忆质量

- [ ] **6.2 Web界面** (Day 27-28)
  - 创建简单的Web界面
  - 可视化记忆网络
  - **验证**: 能通过Web界面管理记忆

- [ ] **6.3 完整集成测试** (Day 28-29)
  - 端到端测试所有用例
  - 性能和稳定性测试
  - **验证**: 所有usecases.md中的场景都能正常工作

- [ ] **6.4 文档和部署** (Day 29-30)
  - 完善用户文档
  - 创建安装和部署指南
  - **验证**: 新用户能快速上手使用

---

## 📊 进度追踪

### 当前状态
- [x] 项目设计完成
- [x] 技术方案确定
- [ ] 开发环境准备
- [ ] 第一个milestone开始

### 每周检查点
- **Week 1**: 基础记忆功能可用
- **Week 2**: 编程特化功能可用
- **Week 3**: 智能检索功能可用
- **Week 4**: 风格学习功能可用
- **Week 5**: 数据持久化完成
- **Week 6**: 完整系统交付

### 风险和缓解
- **风险**: 某个milestone比预期复杂
- **缓解**: 每个任务都可以简化，优先保证核心功能

### 成功标准
每个milestone完成后，用户都能看到明确的新功能，并且能通过简单的命令验证功能正常工作。
