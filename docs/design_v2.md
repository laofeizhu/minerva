# Minerva Memory System - Design v2

## Core Philosophy: Universal Memory Mechanisms

After reflection, we're redesigning Minerva to focus on **universal memory mechanisms** rather than domain-specific implementations. The key insight is that human memory doesn't have separate systems for "coding errors" vs "life experiences" - it uses the same fundamental mechanisms for all learning.

## Design Principles

### 1. Universal Memory Segments
All memories use the same basic structure, regardless of content:

```python
@dataclass
class MemorySegment:
    id: str
    timestamp: float
    content: Dict[str, Any]        # Completely dynamic content
    context: Dict[str, Any]        # Environmental context
    associations: List[str]        # IDs of related memories
    references: List[str]          # IDs of memories this one references
    importance_score: float        # Dynamic importance (0.0-1.0)
    access_count: int             # How often accessed
    consolidation_level: int      # 0=raw, 1=processed, 2=consolidated
```

### 2. Associative Networks
Memories connect through multiple association types:
- **Temporal**: Memories close in time
- **Semantic**: Similar content or concepts  
- **Causal**: One memory led to another
- **Emotional**: Similar emotional context
- **Contextual**: Same environment or situation

### 3. Consolidation Through Sleep
Raw memories get processed and consolidated during "sleep" cycles:
- **Pattern extraction**: Find common themes across related memories
- **Reference creation**: Link consolidated memories back to source experiences
- **Importance adjustment**: Update scores based on usage and relevance
- **Network optimization**: Strengthen useful connections, weaken unused ones

## Example: Learning from User Feedback

### Raw Memory Formation
```python
# User writes 20 unit tests
test_memory = MemorySegment(
    content={
        "action": "wrote_unit_tests",
        "count": 20,
        "approach": "testing_internal_methods",
        "files": ["test_user_service.py", "test_auth_helpers.py"]
    },
    context={
        "task": "implementing_user_authentication",
        "time_spent": "2_hours"
    }
)

# User gives feedback
feedback_memory = MemorySegment(
    content={
        "event": "user_feedback",
        "message": "不要加太多的测试，这些都是在测试实现细节",
        "tone": "corrective",
        "specific_issue": "testing_implementation_details"
    },
    associations=[test_memory.id],  # Link to the testing behavior
    context={
        "situation": "code_review",
        "relationship": "mentor_feedback"
    }
)
```

### Sleep Consolidation
```python
class SleepConsolidator:
    def consolidate_memory(self, memory_segment: MemorySegment) -> Optional[MemorySegment]:
        # 1. Discover related memories through association network
        related_memories = self._discover_related_memories(memory_segment)
        
        # 2. Extract patterns from the memory cluster
        patterns = self._extract_patterns(memory_segment, related_memories)
        
        # 3. Create consolidated memory with references
        if patterns:
            return MemorySegment(
                content={
                    "type": "learned_principle",
                    "principle": patterns["main_principle"],
                    "context": patterns["applicable_context"],
                    "evidence": patterns["supporting_evidence"],
                    "confidence": patterns["confidence_score"]
                },
                references=[memory_segment.id] + [m.id for m in related_memories],
                consolidation_level=memory_segment.consolidation_level + 1,
                importance_score=self._calculate_consolidated_importance(patterns)
            )
```

### Consolidated Result
```python
# After sleep processing
principle_memory = MemorySegment(
    content={
        "type": "learned_principle",
        "principle": "focus_on_behavior_not_implementation_in_testing",
        "context": "when_writing_unit_tests",
        "evidence": "user_feedback_indicated_implementation_tests_not_valuable",
        "confidence": 0.85
    },
    references=[test_memory.id, feedback_memory.id],
    consolidation_level=2,
    importance_score=0.9
)
```

### Future Application
```python
# When encountering similar situation
def handle_testing_task(context):
    # Retrieve relevant memories
    relevant_memories = memory_retrieval.query_by_context("writing_tests")
    
    # Find applicable principles
    for memory in relevant_memories:
        if (memory.content.get("type") == "learned_principle" and 
            memory.content.get("context") == "when_writing_unit_tests"):
            
            # Apply the learned principle
            return apply_principle(memory.content["principle"])
```

## Architecture Components

### 1. Memory Storage
```python
class MemoryStore:
    def add_memory(self, memory: MemorySegment) -> str
    def get_memory(self, memory_id: str) -> Optional[MemorySegment]
    def search_memories(self, query: str, context: Dict = None) -> List[MemorySegment]
    def get_associated_memories(self, memory_id: str) -> List[MemorySegment]
```

### 2. Association Builder
```python
class AssociationBuilder:
    def create_associations(self, new_memory: MemorySegment, existing_memories: List[MemorySegment])
    def strengthen_association(self, memory_id_1: str, memory_id_2: str)
    def weaken_unused_associations(self)
```

### 3. Sleep Processor
```python
class SleepProcessor:
    def consolidate_memory(self, memory: MemorySegment) -> Optional[MemorySegment]
    def run_sleep_cycle(self) -> List[MemorySegment]  # Process multiple memories
    def optimize_network(self)  # Strengthen/weaken connections
```

### 4. Memory Retrieval
```python
class MemoryRetrieval:
    def query_by_content(self, query: str) -> List[MemorySegment]
    def query_by_context(self, context: str) -> List[MemorySegment]
    def query_by_association(self, memory_id: str) -> List[MemorySegment]
    def query_consolidated_principles(self, domain: str) -> List[MemorySegment]
```

## Implementation Strategy

### Phase 1: Basic Memory System
1. Implement `MemorySegment` with universal structure
2. Create `MemoryStore` with basic storage and retrieval
3. Build simple association mechanisms
4. Add basic CLI for memory operations

### Phase 2: Association Networks
1. Implement `AssociationBuilder` with multiple association types
2. Add semantic similarity matching
3. Create temporal and contextual association logic
4. Build association visualization tools

### Phase 3: Sleep Consolidation
1. Implement `SleepProcessor` with pattern extraction
2. Add consolidation algorithms for different memory types
3. Create reference tracking system
4. Build importance scoring mechanisms

### Phase 4: Intelligent Retrieval
1. Implement context-aware memory retrieval
2. Add relevance ranking algorithms
3. Create principle application logic
4. Build learning feedback loops

## Key Advantages of This Approach

1. **Universality**: Same mechanisms work for any domain (coding, life, learning)
2. **Emergent Intelligence**: Smart behavior emerges from simple mechanisms
3. **Natural Learning**: Mirrors how humans actually learn and remember
4. **Extensibility**: New domains automatically benefit from existing mechanisms
5. **Simplicity**: Fewer specialized components, more general principles

## Success Metrics

- **Memory Formation**: Can store any type of experience as memory segments
- **Association Quality**: Related memories are properly connected
- **Consolidation Effectiveness**: Sleep cycles extract useful patterns
- **Application Success**: Consolidated principles improve future decisions
- **Learning Demonstration**: System gets better at tasks through experience

This design focuses on the fundamental mechanisms of memory and learning, allowing intelligence to emerge naturally rather than being hardcoded for specific domains.
