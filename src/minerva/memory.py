"""
Minerva Memory System - Core memory management classes
"""
import time
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum

class MemoryType(Enum):
    """Types of memories in the Minerva system"""
    BASIC_INFO = "basic_info"
    CODEBASE_ANALYSIS = "codebase_analysis"
    ERROR_EXPERIENCE = "error_experience"
    CODING_STYLE = "coding_style_preference"
    CONVERSATION = "conversation"

@dataclass
class MemorySegment:
    """
    A single memory segment containing multi-dimensional information
    """
    # Core identification
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)
    memory_type: MemoryType = MemoryType.BASIC_INFO
    
    # Dynamic content - the main information storage
    content: Dict[str, Any] = field(default_factory=dict)
    
    # Context information
    context: Dict[str, Any] = field(default_factory=dict)
    
    # Emotional and importance metadata
    emotions: Dict[str, Any] = field(default_factory=dict)
    importance_score: float = 0.0
    
    # Sensory and semantic information
    sensory_data: Dict[str, Any] = field(default_factory=dict)
    semantic_info: Dict[str, Any] = field(default_factory=dict)
    
    # Memory management metadata
    associations: List[str] = field(default_factory=list)  # IDs of related memories
    access_count: int = 0
    last_accessed: Optional[float] = None
    
    def __post_init__(self):
        """Initialize computed fields after creation"""
        if self.last_accessed is None:
            self.last_accessed = self.timestamp
    
    def access(self):
        """Record an access to this memory segment"""
        self.access_count += 1
        self.last_accessed = time.time()
    
    def add_association(self, memory_id: str):
        """Add an association to another memory"""
        if memory_id not in self.associations:
            self.associations.append(memory_id)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert memory segment to dictionary for storage"""
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'memory_type': self.memory_type.value,
            'content': self.content,
            'context': self.context,
            'emotions': self.emotions,
            'importance_score': self.importance_score,
            'sensory_data': self.sensory_data,
            'semantic_info': self.semantic_info,
            'associations': self.associations,
            'access_count': self.access_count,
            'last_accessed': self.last_accessed
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MemorySegment':
        """Create memory segment from dictionary"""
        memory_type = MemoryType(data.get('memory_type', MemoryType.BASIC_INFO.value))
        
        return cls(
            id=data['id'],
            timestamp=data['timestamp'],
            memory_type=memory_type,
            content=data.get('content', {}),
            context=data.get('context', {}),
            emotions=data.get('emotions', {}),
            importance_score=data.get('importance_score', 0.0),
            sensory_data=data.get('sensory_data', {}),
            semantic_info=data.get('semantic_info', {}),
            associations=data.get('associations', []),
            access_count=data.get('access_count', 0),
            last_accessed=data.get('last_accessed')
        )

class MemoryStore:
    """
    In-memory storage for memory segments (will be replaced with database in Milestone 5)
    """
    
    def __init__(self):
        self.memories: Dict[str, MemorySegment] = {}
        self.type_index: Dict[MemoryType, List[str]] = {
            memory_type: [] for memory_type in MemoryType
        }
    
    def add_memory(self, memory: MemorySegment) -> str:
        """Add a memory segment to the store"""
        self.memories[memory.id] = memory
        self.type_index[memory.memory_type].append(memory.id)
        return memory.id
    
    def get_memory(self, memory_id: str) -> Optional[MemorySegment]:
        """Retrieve a memory by ID"""
        memory = self.memories.get(memory_id)
        if memory:
            memory.access()
        return memory
    
    def get_memories_by_type(self, memory_type: MemoryType) -> List[MemorySegment]:
        """Get all memories of a specific type"""
        memory_ids = self.type_index.get(memory_type, [])
        memories = []
        for memory_id in memory_ids:
            memory = self.memories.get(memory_id)
            if memory:
                memory.access()
                memories.append(memory)
        return memories
    
    def search_memories(self, query: str) -> List[MemorySegment]:
        """Simple keyword search across all memories"""
        query_lower = query.lower()
        matching_memories = []
        
        for memory in self.memories.values():
            # Search in content
            content_str = str(memory.content).lower()
            if query_lower in content_str:
                memory.access()
                matching_memories.append(memory)
                continue
            
            # Search in semantic info
            semantic_str = str(memory.semantic_info).lower()
            if query_lower in semantic_str:
                memory.access()
                matching_memories.append(memory)
        
        # Sort by importance score and recency
        matching_memories.sort(
            key=lambda m: (m.importance_score, m.last_accessed), 
            reverse=True
        )
        
        return matching_memories
    
    def get_stats(self) -> Dict[str, Any]:
        """Get memory store statistics"""
        total_memories = len(self.memories)
        type_counts = {
            memory_type.value: len(memory_ids) 
            for memory_type, memory_ids in self.type_index.items()
        }
        
        return {
            'total_memories': total_memories,
            'type_counts': type_counts,
            'most_accessed': max(self.memories.values(), key=lambda m: m.access_count) if self.memories else None,
            'most_recent': max(self.memories.values(), key=lambda m: m.timestamp) if self.memories else None
        }

# Global memory store instance (will be replaced with proper dependency injection)
memory_store = MemoryStore()
