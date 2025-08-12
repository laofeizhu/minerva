"""
Minerva - A memory-based coding assistant inspired by human memory mechanisms

This package provides a coding assistant that learns from interactions,
remembers codebase structures, learns from errors, and adapts to user coding styles.
"""

__version__ = "0.1.0"
__author__ = "laofeizhu"

from .memory import MemorySegment, MemoryStore, MemoryType, memory_store
from .cli import main

__all__ = [
    "MemorySegment",
    "MemoryStore",
    "MemoryType",
    "memory_store",
    "main"
]
