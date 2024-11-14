import os
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel
import copier

app = typer.Typer(
    name="components",
    help="Install and update components from basic-components",
    add_completion=False,
)

console = Console()

# Base repo URL without branch
REPO_URL = "https://github.com/basicmachines-co/basic-components.git"
DEFAULT_BRANCH = "main"

# Use environment variable if set, otherwise use default
COMPONENTS_DIR = Path(os.getenv("COMPONENTS_DIR", "components/ui"))


def add_component(
    component: str,
    dest_dir: Path,
    branch: str = DEFAULT_BRANCH,
    force: bool = False,
) -> None:
    """Add a specific component to the project."""
    try:
        console.print(f"[green]Installing {component}...[/green]")

        data = {
            "component": component,  # Pass the component name to copier.yml
        }

        copier.run_copy(
            src_path=REPO_URL,
            dst_path=str(dest_dir),
            data=data,
            vcs_ref=branch,
            defaults=True,
            unsafe=True,
            answers_file=None,
        )

    except copier.errors.UserMessageError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command()
def add(
    component: str = typer.Argument(..., help="Name of the component to install"),
    branch: str = typer.Option(
        DEFAULT_BRANCH, "--branch", "-b", help="Branch, tag, or commit to install from"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Skip prompts and use defaults"
    ),
) -> None:
    """Add a component to your project."""
    try:
        add_component(component, COMPONENTS_DIR, branch, force)

        console.print(
            Panel(
                f"[green]✓[/green] Added {component} component\n\n"
                f"Use in your templates:\n"
                f'[cyan]<{component.capitalize()} variant="primary">Content</{component.capitalize()}>[/cyan]',
                title="Installation Complete",
                border_style="green",
            )
        )
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise typer.Exit(1)


@app.command()
def init() -> None:
    """Initialize project for basic-components."""
    # Create components directory structure
    COMPONENTS_DIR.mkdir(parents=True, exist_ok=True)

    # Show the actual path being used
    components_path = (
        "[dim](using default)[/dim]"
        if os.getenv("COMPONENTS_DIR") is None
        else "[dim](from COMPONENTS_DIR)[/dim]"
    )

    console.print(
        Panel(
            "[green]✓[/green] Initialized basic-components\n\n"
            "Directory structure created:\n"
            f"   [cyan]{COMPONENTS_DIR}[/cyan] {components_path}\n\n"
            "Next steps:\n\n"
            "1. Add the cn() utility function:\n"
            "   [cyan]components.basicmachines.co/docs/utilities#cn[/cyan]\n\n"
            "2. Configure JinjaX to use the components directory:\n"
            "   [cyan]components.basicmachines.co/docs/utilities#jinjax[/cyan]\n\n"
            "3. Start adding components:\n"
            "   [cyan]components add button[/cyan]\n\n"
            "View all available components:\n"
            "   [cyan]components.basicmachines.co/docs/components[/cyan]",
            title="Setup Complete",
            border_style="green",
        )
    )


if __name__ == "__main__":
    app()
