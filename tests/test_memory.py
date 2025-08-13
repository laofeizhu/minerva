"""
Tests for Minerva Hello World Implementation
"""
import pytest
from minerva import hello_world

def test_hello_world():
    """Test the basic hello world function"""
    result = hello_world()
    assert "Hello from Minerva" in result
    assert "🧠" in result

def test_hello_world_returns_string():
    """Test that hello world returns a string"""
    result = hello_world()
    assert isinstance(result, str)
    assert len(result) > 0
