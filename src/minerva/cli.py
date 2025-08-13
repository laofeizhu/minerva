"""
Minerva CLI - Hello World Implementation
"""
import click
from rich.console import Console
from rich.panel import Panel

console = Console()

@click.group()
@click.version_option(version="0.1.0")
def main():
    """Minerva - A memory-based assistant (Hello World)"""
    console.print(Panel.fit(
        "[bold blue]Minerva[/bold blue] - Hello World 🧠",
        subtitle="Basic memory system foundation"
    ))

@main.command()
def hello():
    """Say hello from Minerva"""
    from . import hello_world
    console.print(f"[green]{hello_world()}[/green]")
    console.print("[dim]This is the foundation for a memory-based assistant[/dim]")

@main.command()
def info():
    """Show system information"""
    console.print("🧠 [bold]Minerva Memory System[/bold]")
    console.print("📋 Status: Hello World Implementation")
    console.print("🎯 Goal: Human-inspired memory mechanisms")
    console.print("📚 Next: Implement basic memory storage and retrieval")

if __name__ == "__main__":
    main()
