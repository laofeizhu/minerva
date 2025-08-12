# Minerva 🧠

A memory-based coding assistant inspired by human memory mechanisms.

## Overview

Minerva is an AI coding assistant that learns from every interaction, remembers codebase structures, learns from errors, and adapts to your coding style. Unlike traditional AI assistants that start fresh each time, Minerva builds a persistent memory system that gets smarter with use.

## Key Features

- 🧠 **Memory-Based Learning**: Builds persistent memory from every interaction
- 📚 **Codebase Understanding**: Analyzes and remembers project architectures
- 🐛 **Error Learning**: Learns from mistakes to avoid repeating them
- 🎨 **Style Adaptation**: Learns and applies your coding preferences
- 🔍 **Intelligent Retrieval**: Finds relevant memories using associative search

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/laofeizhu/minerva.git
cd minerva

# Install with uv (recommended)
uv sync

# Or install with pip
pip install -e .
```

### Basic Usage

```bash
# Add a memory
uv run minerva add-memory "My GitHub username is john_doe"

# Ask a question
uv run minerva ask "What is my GitHub username?"

# Analyze a codebase
uv run minerva analyze-code ./my_project

# View memory statistics
uv run minerva stats
```

## Development Status

This project is in early development. Current milestone: **Milestone 1 - Basic Memory Storage**

- [x] Project structure and CLI framework
- [x] Basic memory segment implementation
- [x] In-memory storage system
- [ ] Complete CLI functionality
- [ ] First working demo

See [docs/execution.md](docs/execution.md) for detailed development roadmap.

## Architecture

Minerva is inspired by human memory mechanisms:

- **Memory Segments**: Multi-dimensional information storage (like human memory episodes)
- **Associative Networks**: Memories connected by time, space, semantics, and emotions
- **Importance Scoring**: Automatic prioritization of valuable information
- **Memory Consolidation**: Sleep-like processes for organizing and optimizing memories

## Documentation

- [Design Overview](docs/computer_memory.md) - Detailed system architecture
- [Use Cases](docs/usecases.md) - Example scenarios and workflows
- [Execution Plan](docs/execution.md) - Development milestones and progress
- [Quick Start with uv](docs/quickstart_with_uv.md) - Setup and development guide

## Contributing

This project follows the principle of simplicity and step-by-step development. Each milestone introduces clear, verifiable improvements.

## License

MIT License - see LICENSE file for details.