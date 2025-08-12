"""
Tests for the Minerva memory system
"""
import pytest
from minerva.memory import MemorySegment, MemoryStore, MemoryType

class TestMemorySegment:
    """Test the MemorySegment class"""
    
    def test_create_basic_memory(self):
        """Test creating a basic memory segment"""
        memory = MemorySegment(
            memory_type=MemoryType.BASIC_INFO,
            content={"info": "test data"}
        )
        
        assert memory.id is not None
        assert memory.memory_type == MemoryType.BASIC_INFO
        assert memory.content["info"] == "test data"
        assert memory.access_count == 0
    
    def test_memory_access_tracking(self):
        """Test that memory access is properly tracked"""
        memory = MemorySegment()
        initial_count = memory.access_count
        initial_time = memory.last_accessed
        
        memory.access()
        
        assert memory.access_count == initial_count + 1
        assert memory.last_accessed > initial_time
    
    def test_memory_associations(self):
        """Test memory association functionality"""
        memory = MemorySegment()
        other_id = "other-memory-id"
        
        memory.add_association(other_id)
        
        assert other_id in memory.associations
        
        # Test that duplicate associations are not added
        memory.add_association(other_id)
        assert memory.associations.count(other_id) == 1
    
    def test_memory_serialization(self):
        """Test memory segment serialization and deserialization"""
        original = MemorySegment(
            memory_type=MemoryType.CODEBASE_ANALYSIS,
            content={"language": "python", "framework": "flask"},
            importance_score=0.8
        )
        
        # Serialize to dict
        data = original.to_dict()
        
        # Deserialize from dict
        restored = MemorySegment.from_dict(data)
        
        assert restored.id == original.id
        assert restored.memory_type == original.memory_type
        assert restored.content == original.content
        assert restored.importance_score == original.importance_score

class TestMemoryStore:
    """Test the MemoryStore class"""
    
    def test_add_and_retrieve_memory(self):
        """Test adding and retrieving memories"""
        store = MemoryStore()
        memory = MemorySegment(
            content={"test": "data"}
        )
        
        memory_id = store.add_memory(memory)
        retrieved = store.get_memory(memory_id)
        
        assert retrieved is not None
        assert retrieved.id == memory.id
        assert retrieved.content == memory.content
        assert retrieved.access_count == 1  # Should be incremented by get_memory
    
    def test_get_memories_by_type(self):
        """Test retrieving memories by type"""
        store = MemoryStore()
        
        # Add different types of memories
        basic_memory = MemorySegment(
            memory_type=MemoryType.BASIC_INFO,
            content={"type": "basic"}
        )
        code_memory = MemorySegment(
            memory_type=MemoryType.CODEBASE_ANALYSIS,
            content={"type": "code"}
        )
        
        store.add_memory(basic_memory)
        store.add_memory(code_memory)
        
        # Retrieve by type
        basic_memories = store.get_memories_by_type(MemoryType.BASIC_INFO)
        code_memories = store.get_memories_by_type(MemoryType.CODEBASE_ANALYSIS)
        
        assert len(basic_memories) == 1
        assert len(code_memories) == 1
        assert basic_memories[0].content["type"] == "basic"
        assert code_memories[0].content["type"] == "code"
    
    def test_search_memories(self):
        """Test memory search functionality"""
        store = MemoryStore()
        
        memory1 = MemorySegment(content={"description": "python flask application"})
        memory2 = MemorySegment(content={"description": "javascript react component"})
        memory3 = MemorySegment(semantic_info={"keywords": ["python", "testing"]})
        
        store.add_memory(memory1)
        store.add_memory(memory2)
        store.add_memory(memory3)
        
        # Search for python-related memories
        python_memories = store.search_memories("python")
        
        assert len(python_memories) == 2
        assert memory1 in python_memories
        assert memory3 in python_memories
        assert memory2 not in python_memories
    
    def test_memory_stats(self):
        """Test memory store statistics"""
        store = MemoryStore()
        
        # Add some memories
        store.add_memory(MemorySegment(memory_type=MemoryType.BASIC_INFO))
        store.add_memory(MemorySegment(memory_type=MemoryType.BASIC_INFO))
        store.add_memory(MemorySegment(memory_type=MemoryType.CODEBASE_ANALYSIS))
        
        stats = store.get_stats()
        
        assert stats['total_memories'] == 3
        assert stats['type_counts'][MemoryType.BASIC_INFO.value] == 2
        assert stats['type_counts'][MemoryType.CODEBASE_ANALYSIS.value] == 1
        assert stats['most_recent'] is not None
