# Minerva 通用记忆系统 - 实现工作流

## 设计原则

基于 [design_v2.md](design_v2.md) 的通用记忆机制，实现简单、通用、人类启发的记忆系统。

### 核心理念
1. **通用性**: 同一套机制处理所有类型的记忆
2. **关联性**: 记忆通过多种方式自然关联
3. **整理性**: 睡眠周期提取模式和经验
4. **智能涌现**: 复杂行为从简单机制中产生

## 实现路线图

### Phase 1: 基础记忆系统 (Week 1)

#### 目标
实现通用的记忆片段存储和基础关联功能

#### 核心组件

**1. MemorySegment (通用记忆片段)**
```python
@dataclass
class MemorySegment:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)
    content: Dict[str, Any] = field(default_factory=dict)  # 完全动态
    context: Dict[str, Any] = field(default_factory=dict)
    associations: List[str] = field(default_factory=list)  # 关联的记忆ID
    references: List[str] = field(default_factory=list)    # 引用的记忆ID
    importance_score: float = 0.0
    access_count: int = 0
    consolidation_level: int = 0  # 0=原始, 1=处理, 2=整理
```

**2. MemoryStore (记忆存储)**
```python
class MemoryStore:
    def add_memory(self, memory: MemorySegment) -> str
    def get_memory(self, memory_id: str) -> Optional[MemorySegment]
    def search_memories(self, query: str) -> List[MemorySegment]
    def get_associated_memories(self, memory_id: str) -> List[MemorySegment]
```

**3. 基础CLI命令**
```bash
uv run minerva add-memory "学习了Python装饰器"
uv run minerva query "装饰器"
uv run minerva show-memory <memory_id>
uv run minerva stats
```

#### 实现步骤
1. 实现 `MemorySegment` 类
2. 实现 `MemoryStore` 基础存储
3. 更新CLI支持基础记忆操作
4. 添加测试和验证

### Phase 2: 关联网络系统 (Week 2)

#### 目标
实现记忆片段之间的智能关联

#### 核心组件

**1. AssociationBuilder (关联构建器)**
```python
class AssociationBuilder:
    def create_associations(self, new_memory: MemorySegment, existing_memories: List[MemorySegment]):
        """为新记忆创建关联"""
        # 时间关联 - 时间邻近的记忆
        # 语义关联 - 内容相似的记忆  
        # 因果关联 - 有因果关系的记忆
        # 情境关联 - 相同环境的记忆
```

**2. 关联类型**
- **Temporal**: 时间邻近 (前后1小时内)
- **Semantic**: 语义相似 (关键词、概念重叠)
- **Causal**: 因果关系 (一个记忆导致另一个)
- **Contextual**: 情境相关 (相同环境、任务)

**3. 增强的CLI命令**
```bash
uv run minerva show-associations <memory_id>
uv run minerva find-related "装饰器"
uv run minerva network-stats
```

#### 实现步骤
1. 实现关联类型和强度计算
2. 创建 `AssociationBuilder` 类
3. 增强记忆检索支持关联查询
4. 添加关联可视化命令

### Phase 3: 睡眠整理系统 (Week 3)

#### 目标
实现记忆的自动整理和模式提取

#### 核心组件

**1. SleepProcessor (睡眠处理器)**
```python
class SleepProcessor:
    def consolidate_memory(self, memory_segment: MemorySegment) -> Optional[MemorySegment]:
        """整理单个记忆片段"""
        # 1. 发现相关记忆
        related_memories = self._discover_related_memories(memory_segment)
        
        # 2. 提取模式
        patterns = self._extract_patterns(memory_segment, related_memories)
        
        # 3. 创建整理后的记忆
        if patterns:
            return self._create_consolidated_memory(patterns, memory_segment, related_memories)
```

**2. 模式提取类型**
- **学习原则**: 从反馈中提取行为准则
- **错误模式**: 识别重复的错误和解决方案
- **行为模式**: 发现习惯和偏好
- **知识结构**: 组织相关概念和事实

**3. 睡眠CLI命令**
```bash
uv run minerva sleep-cycle          # 手动触发睡眠整理
uv run minerva show-principles      # 显示学到的原则
uv run minerva consolidation-stats  # 整理统计信息
```

#### 实现步骤
1. 实现模式识别算法
2. 创建 `SleepProcessor` 类
3. 添加整理后记忆的引用系统
4. 实现睡眠周期调度

### Phase 4: 智能应用系统 (Week 4)

#### 目标
基于整理后的记忆提供智能建议和指导

#### 核心组件

**1. MemoryApplication (记忆应用)**
```python
class MemoryApplication:
    def get_guidance(self, current_situation: Dict[str, Any]) -> List[str]:
        """基于相关记忆提供指导"""
        # 1. 找到相关的整理后记忆
        # 2. 匹配当前情境
        # 3. 提供个性化建议
```

**2. 智能CLI命令**
```bash
uv run minerva ask-guidance "我在写Python测试"
uv run minerva what-learned "测试"
uv run minerva apply-experience <situation>
```

#### 实现步骤
1. 实现情境匹配算法
2. 创建建议生成系统
3. 添加学习反馈循环
4. 完善用户交互体验

## 验证标准

### Phase 1 验证
- ✅ 能存储任意类型的记忆
- ✅ 基础检索功能正常
- ✅ CLI命令响应正确
- ✅ 测试覆盖率 > 80%

### Phase 2 验证
- ✅ 自动建立记忆关联
- ✅ 关联类型识别准确
- ✅ 关联强度计算合理
- ✅ 可视化关联网络

### Phase 3 验证
- ✅ 睡眠整理提取有用模式
- ✅ 整理后记忆保留原始引用
- ✅ 重要性评分动态调整
- ✅ 模式识别准确率 > 70%

### Phase 4 验证
- ✅ 提供相关和有用的建议
- ✅ 学习反馈改进系统表现
- ✅ 用户满意度高
- ✅ 展示智能涌现行为

## 成功指标

1. **通用性**: 能处理编程、学习、生活等各种记忆
2. **关联质量**: 相关记忆能被正确关联
3. **学习能力**: 从经验中提取有用模式
4. **应用效果**: 整理后的经验能指导未来行为
5. **用户体验**: 交互自然，反馈有价值

这个工作流专注于通用机制，让智能从简单原理中自然涌现，而不是硬编码特定领域的逻辑。
