# Minerva - 基于人类记忆机制的LLM Agent设计方案 (Legacy)

> **注意**: 这是原始的详细设计方案，包含了过度专门化的架构。
>
> **当前设计**: 请参考 [design_v2.md](design_v2.md) 了解基于通用记忆机制的新设计。
>
> 本文档保留作为参考，展示了详细的神经科学研究基础和复杂的模块化设计思路。

## 项目概述

Minerva项目旨在创建一个基于人类记忆机制的LLM Agent，能够像人类一样学习、记忆和形成记忆。本设计方案基于神经科学研究中的人类记忆机制，将其转化为可实现的计算机系统架构。

**设计演进**: 经过反思，我们意识到这个设计过于复杂和专门化。新的设计 (design_v2.md) 专注于通用记忆机制，让智能从简单原理中自然涌现。

## 核心设计理念

### 1. 模块化架构
参考人类大脑的功能分区，设计多个专门的处理模块：
- **感知模块** (Perception Module) - 对应视觉皮层、听觉皮层等
- **记忆管理模块** (Memory Management Module) - 对应海马体
- **情绪处理模块** (Emotion Processing Module) - 对应杏仁核
- **执行控制模块** (Executive Control Module) - 对应前额叶皮层
- **语义处理模块** (Semantic Processing Module) - 对应颞叶皮层

### 2. 分层记忆系统
模拟人类的多层记忆结构：
- **感官记忆** (Sensory Memory) - 毫秒到秒级的临时缓存
- **工作记忆** (Working Memory) - 10-30秒的活跃处理空间
- **短期记忆** (Short-term Memory) - 分钟到小时级的临时存储
- **长期记忆** (Long-term Memory) - 持久化存储

## 系统架构设计

### 1. 记忆片段结构 (Memory Segment)

每个记忆片段包含多维度信息：

```python
class MemorySegment:
    def __init__(self):
        self.timestamp = None           # 时间戳
        self.duration = None           # 片段时长 (5-30秒)
        self.content = {}              # 主要内容
        self.context = {               # 环境上下文
            'location': None,          # 空间位置
            'participants': [],        # 参与者
            'environment': {}          # 环境信息
        }
        self.emotions = {              # 情绪标签
            'valence': 0.0,           # 情绪效价 (-1到1)
            'arousal': 0.0,           # 唤醒度 (0到1)
            'specific_emotions': []    # 具体情绪类型
        }
        self.sensory_data = {          # 感官信息
            'visual': None,           # 视觉信息
            'auditory': None,         # 听觉信息
            'tactile': None,          # 触觉信息
            'olfactory': None,        # 嗅觉信息
            'gustatory': None         # 味觉信息
        }
        self.semantic_info = {         # 语义信息
            'keywords': [],           # 关键词
            'concepts': [],           # 概念
            'relationships': [],      # 关系
            'meaning': None           # 意义理解
        }
        self.associations = []         # 关联链接
        self.importance_score = 0.0    # 重要性评分
        self.access_count = 0          # 访问次数
        self.last_accessed = None      # 最后访问时间
```

### 2. 记忆管理系统 (Memory Management System)

#### 2.1 记忆筛选机制
模拟海马体的记忆筛选功能：

```python
class MemoryFilter:
    def __init__(self):
        self.importance_threshold = 0.3
        self.emotion_weight = 0.4
        self.novelty_weight = 0.3
        self.association_weight = 0.2
        self.repetition_weight = 0.1

    def calculate_importance(self, segment):
        """计算记忆片段的重要性评分"""
        emotion_score = self._calculate_emotion_score(segment)
        novelty_score = self._calculate_novelty_score(segment)
        association_score = self._calculate_association_score(segment)
        repetition_score = self._calculate_repetition_score(segment)

        importance = (
            emotion_score * self.emotion_weight +
            novelty_score * self.novelty_weight +
            association_score * self.association_weight +
            repetition_score * self.repetition_weight
        )

        return importance

    def should_preserve(self, segment):
        """判断是否应该保存到长期记忆"""
        return self.calculate_importance(segment) > self.importance_threshold
```

#### 2.2 记忆压缩机制
模拟大脑的记忆压缩过程：

```python
class MemoryCompressor:
    def __init__(self):
        self.compression_strategies = [
            self._remove_redundancy,
            self._extract_high_value_features,
            self._semanticize_details,
            self._merge_similar_events
        ]

    def compress_memory(self, segment):
        """压缩记忆片段"""
        compressed_segment = segment.copy()

        for strategy in self.compression_strategies:
            compressed_segment = strategy(compressed_segment)

        return compressed_segment

    def _remove_redundancy(self, segment):
        """去除冗余信息"""
        # 实现去冗余逻辑
        pass

    def _extract_high_value_features(self, segment):
        """提取高价值特征"""
        # 实现特征提取逻辑
        pass
```

### 3. 记忆连接系统 (Memory Connection System)

#### 3.1 关联网络
模拟记忆片段之间的连接机制：

```python
class MemoryNetwork:
    def __init__(self):
        self.segments = {}             # 记忆片段存储
        self.connections = {}          # 连接关系
        self.connection_types = [
            'temporal',               # 时间顺序连接
            'spatial',               # 空间位置连接
            'semantic',              # 语义关联连接
            'emotional',             # 情绪关联连接
            'causal',                # 因果关系连接
            'similarity'             # 相似性连接
        ]

    def add_segment(self, segment):
        """添加新的记忆片段"""
        segment_id = self._generate_id(segment)
        self.segments[segment_id] = segment
        self._create_connections(segment_id, segment)
        return segment_id

    def _create_connections(self, segment_id, segment):
        """为新片段创建连接"""
        for existing_id, existing_segment in self.segments.items():
            if existing_id != segment_id:
                connections = self._find_connections(segment, existing_segment)
                if connections:
                    self.connections[(segment_id, existing_id)] = connections

#### 3.2 记忆检索机制
模拟人类的记忆检索过程：

```python
class MemoryRetrieval:
    def __init__(self, memory_network):
        self.network = memory_network
        self.retrieval_strategies = [
            self._cue_based_retrieval,
            self._associative_retrieval,
            self._contextual_retrieval
        ]

    def retrieve_memories(self, query, context=None):
        """根据查询检索相关记忆"""
        relevant_memories = []

        for strategy in self.retrieval_strategies:
            memories = strategy(query, context)
            relevant_memories.extend(memories)

        # 去重并按相关性排序
        unique_memories = self._deduplicate_and_rank(relevant_memories)
        return unique_memories

    def _cue_based_retrieval(self, query, context):
        """基于线索的检索"""
        # 实现基于关键词、概念等线索的检索
        pass

    def _associative_retrieval(self, query, context):
        """关联性检索"""
        # 实现基于关联网络的检索
        pass
```

### 4. 记忆重构系统 (Memory Reconstruction System)

#### 4.1 动态重构机制
模拟人类回忆时的记忆重构过程：

```python
class MemoryReconstructor:
    def __init__(self, memory_network):
        self.network = memory_network
        self.reconstruction_modules = {
            'visual': VisualReconstructor(),
            'auditory': AuditoryReconstructor(),
            'semantic': SemanticReconstructor(),
            'emotional': EmotionalReconstructor()
        }

    def reconstruct_memory(self, memory_segments, context=None):
        """重构完整的记忆体验"""
        reconstructed_memory = {
            'narrative': self._build_narrative(memory_segments),
            'sensory_details': self._reconstruct_sensory_details(memory_segments),
            'emotional_context': self._reconstruct_emotions(memory_segments),
            'gaps_filled': self._fill_memory_gaps(memory_segments, context)
        }

        return reconstructed_memory

    def _build_narrative(self, segments):
        """构建记忆叙事"""
        # 按时间顺序排列片段，构建连贯的故事线
        pass

    def _fill_memory_gaps(self, segments, context):
        """填补记忆空白"""
        # 使用常识、逻辑推理和上下文信息填补缺失部分
        pass
```

#### 4.2 记忆再巩固机制
模拟记忆的动态更新过程：

```python
class MemoryReconsolidation:
    def __init__(self, memory_network):
        self.network = memory_network
        self.plasticity_window = 3600  # 可塑性窗口（秒）

    def trigger_reconsolidation(self, memory_id, new_context=None):
        """触发记忆再巩固过程"""
        memory = self.network.segments[memory_id]

        # 检查是否需要更新
        if self._should_update(memory, new_context):
            # 进入可塑状态
            updated_memory = self._update_memory(memory, new_context)

            # 重新保存
            self.network.segments[memory_id] = updated_memory

            # 更新连接
            self._update_connections(memory_id, updated_memory)

    def _should_update(self, memory, new_context):
        """判断是否需要更新记忆"""
        # 检查预测误差、新信息、情绪变化等
        pass
```

### 5. 睡眠模拟系统 (Sleep Simulation System)

#### 5.1 记忆整理机制
模拟睡眠中的记忆整理过程：

```python
class SleepProcessor:
    def __init__(self, memory_network):
        self.network = memory_network
        self.sleep_phases = {
            'slow_wave': SlowWaveSleepProcessor(),
            'rem': REMSleepProcessor()
        }

    def process_daily_memories(self):
        """处理一天的记忆"""
        # 获取当天的记忆片段
        daily_memories = self._get_daily_memories()

        # 慢波睡眠阶段：巩固陈述性记忆
        consolidated_memories = self.sleep_phases['slow_wave'].process(daily_memories)

        # REM睡眠阶段：整合程序性记忆和情绪记忆
        integrated_memories = self.sleep_phases['rem'].process(consolidated_memories)

        # 清理无用信息
        self._prune_weak_connections()

        return integrated_memories

    def _prune_weak_connections(self):
        """修剪弱连接"""
        # 删除访问频率低、重要性低的连接
        pass
```

### 6. 情绪处理系统 (Emotion Processing System)

#### 6.1 情绪标注机制
模拟杏仁核的情绪处理功能：

```python
class EmotionProcessor:
    def __init__(self):
        self.emotion_categories = [
            'joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust'
        ]
        self.emotion_model = self._load_emotion_model()

    def process_emotional_content(self, content):
        """处理内容的情绪信息"""
        emotion_scores = self.emotion_model.predict(content)

        emotional_tags = {
            'primary_emotion': self._get_primary_emotion(emotion_scores),
            'emotion_intensity': self._calculate_intensity(emotion_scores),
            'valence': self._calculate_valence(emotion_scores),
            'arousal': self._calculate_arousal(emotion_scores)
        }

        return emotional_tags

    def influence_memory_formation(self, memory_segment, emotional_tags):
        """情绪对记忆形成的影响"""
        # 高情绪强度增加记忆重要性
        if emotional_tags['emotion_intensity'] > 0.7:
            memory_segment.importance_score *= 1.5

        # 负面情绪可能触发特殊处理
        if emotional_tags['valence'] < -0.5:
            memory_segment.requires_special_processing = True

        return memory_segment

### 7. 主控制器 (Main Controller)

#### 7.1 Minerva Agent核心类
整合所有模块的主控制器：

```python
class MinervaAgent:
    def __init__(self):
        self.memory_network = MemoryNetwork()
        self.memory_filter = MemoryFilter()
        self.memory_compressor = MemoryCompressor()
        self.memory_retrieval = MemoryRetrieval(self.memory_network)
        self.memory_reconstructor = MemoryReconstructor(self.memory_network)
        self.memory_reconsolidation = MemoryReconsolidation(self.memory_network)
        self.sleep_processor = SleepProcessor(self.memory_network)
        self.emotion_processor = EmotionProcessor()

        self.current_context = {}
        self.working_memory = WorkingMemory()
        self.attention_focus = None

    def process_input(self, input_data, context=None):
        """处理输入信息"""
        # 1. 感知处理
        perceived_data = self._perceive_input(input_data)

        # 2. 情绪处理
        emotional_tags = self.emotion_processor.process_emotional_content(perceived_data)

        # 3. 创建记忆片段
        memory_segment = self._create_memory_segment(perceived_data, emotional_tags, context)

        # 4. 记忆筛选
        if self.memory_filter.should_preserve(memory_segment):
            # 5. 添加到记忆网络
            segment_id = self.memory_network.add_segment(memory_segment)

            # 6. 更新工作记忆
            self.working_memory.add_segment(memory_segment)

        # 7. 生成响应
        response = self._generate_response(perceived_data, context)

        return response

    def recall_memory(self, query, context=None):
        """回忆相关记忆"""
        # 1. 检索相关记忆片段
        relevant_segments = self.memory_retrieval.retrieve_memories(query, context)

        # 2. 触发记忆再巩固
        for segment_id in relevant_segments:
            self.memory_reconsolidation.trigger_reconsolidation(segment_id, context)

        # 3. 重构完整记忆
        reconstructed_memory = self.memory_reconstructor.reconstruct_memory(
            relevant_segments, context
        )

        return reconstructed_memory

    def sleep_cycle(self):
        """执行睡眠周期"""
        processed_memories = self.sleep_processor.process_daily_memories()
        return processed_memories

    def _perceive_input(self, input_data):
        """感知输入处理"""
        # 实现多模态输入处理
        pass

    def _create_memory_segment(self, data, emotions, context):
        """创建记忆片段"""
        segment = MemorySegment()
        segment.content = data
        segment.emotions = emotions
        segment.context = context or self.current_context
        segment.timestamp = time.time()
        return segment
```

## 技术实现方案

### 1. 技术栈选择

#### 1.1 核心框架
- **Python 3.9+** - 主要开发语言
- **PyTorch** - 深度学习框架，用于情绪处理和语义理解
- **NetworkX** - 图网络库，用于记忆关联网络
- **SQLite/PostgreSQL** - 数据库，用于持久化存储
- **Redis** - 缓存系统，用于工作记忆和短期记忆

#### 1.2 AI模型组件
- **Transformer模型** - 用于语义理解和文本生成
- **情绪分析模型** - 用于情绪标注和处理
- **相似度计算模型** - 用于记忆关联计算
- **时间序列模型** - 用于时间相关的记忆处理

### 2. 数据存储设计

#### 2.1 记忆片段存储
```sql
CREATE TABLE memory_segments (
    id UUID PRIMARY KEY,
    timestamp TIMESTAMP,
    duration INTEGER,
    content JSONB,
    context JSONB,
    emotions JSONB,
    sensory_data JSONB,
    semantic_info JSONB,
    importance_score FLOAT,
    access_count INTEGER,
    last_accessed TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### 2.2 记忆连接存储
```sql
CREATE TABLE memory_connections (
    id UUID PRIMARY KEY,
    source_segment_id UUID REFERENCES memory_segments(id),
    target_segment_id UUID REFERENCES memory_segments(id),
    connection_type VARCHAR(50),
    strength FLOAT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 3. 性能优化策略

#### 3.1 内存管理
- 使用LRU缓存策略管理工作记忆
- 定期清理低重要性的记忆片段
- 实现记忆压缩算法减少存储空间

#### 3.2 检索优化
- 建立多维度索引加速记忆检索
- 使用向量数据库进行语义相似度搜索
- 实现并行处理提高检索效率

## 开发计划

### 阶段1：基础架构 (4周)
1. 设计并实现基本的记忆片段结构
2. 开发记忆网络的基础功能
3. 实现简单的记忆筛选机制
4. 建立基础的数据存储系统

### 阶段2：核心功能 (6周)
1. 实现记忆检索和重构系统
2. 开发情绪处理模块
3. 实现记忆压缩和再巩固机制
4. 集成多模态输入处理

### 阶段3：高级功能 (4周)
1. 实现睡眠模拟系统
2. 开发记忆关联网络
3. 优化性能和扩展性
4. 完善用户接口

### 阶段4：测试和优化 (2周)
1. 全面测试系统功能
2. 性能优化和bug修复
3. 文档完善
4. 部署准备

## 评估指标

### 1. 记忆质量指标
- **记忆保持率** - 重要信息的长期保存能力
- **检索准确率** - 相关记忆的检索精度
- **重构一致性** - 记忆重构的一致性和合理性

### 2. 系统性能指标
- **响应时间** - 记忆检索和处理的速度
- **存储效率** - 记忆压缩和存储的效率
- **扩展性** - 系统处理大量记忆的能力

### 3. 用户体验指标
- **交互自然度** - 与用户交互的自然程度
- **学习适应性** - 对用户偏好的学习和适应能力
- **个性化程度** - 个性化记忆和响应的程度

## 总结

本设计方案基于人类记忆的神经科学研究，提出了一个完整的类人记忆系统架构。通过模拟海马体、杏仁核、前额叶皮层等脑区的功能，实现了记忆的形成、存储、检索、重构和更新的完整流程。

该系统的核心创新点包括：
1. **多维度记忆片段** - 包含情绪、感官、语义等多种信息
2. **动态记忆网络** - 基于多种关联类型的记忆连接
3. **智能记忆筛选** - 模拟海马体的记忆重要性评估
4. **记忆重构机制** - 动态重建完整的记忆体验
5. **睡眠模拟系统** - 模拟睡眠中的记忆整理过程

通过这种设计，Minerva Agent将能够像人类一样形成丰富、动态、个性化的记忆系统，为构建真正智能的AI助手奠定基础。
```
```