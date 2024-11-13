# basic_components/cli.py
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
import copier
import tomli
from copier.main import Worker

app = typer.Typer(
    name="components",
    help="Install and update components from basic-components",
    add_completion=False,
)

console = Console()

REPO_URL = "https://github.com/basicmachines-co/basic-components.git"
DEFAULT_BRANCH = "main"


def get_components_dir() -> Path:
    """Get the components directory from pyproject.toml or use default."""
    try:
        with open("pyproject.toml", "rb") as f:
            config = tomli.load(f)
            return Path(
                config.get("tool", {})
                .get(
                    "basic-components", {}
                )  # Changed from "components" to "basic-components"
                .get("components_dir", "components")
            )
    except FileNotFoundError:
        return Path("components")


async def install_or_update_component(
    component: str, dest_dir: Path, branch: str = DEFAULT_BRANCH, force: bool = False
) -> None:
    """Install or update a component using copier's built-in update mechanism."""

    # Prepare copier answers
    data = {
        "components": [component],  # Only copy specific component
        "components_dir": str(dest_dir),
        "style": "default",
    }

    try:
        # Use copier's worker directly for better control
        worker = await Worker.get_worker(
            src_path=f"{REPO_URL}@{branch}",
            dst_path=str(dest_dir),
            data=data,
            vcs_ref=branch,
            force=force,
            unsafe=True,  # Needed to skip questions in answers file
        )

        # Check if it's an update or new installation
        if worker.is_update:
            console.print("[yellow]Updating existing component...[/yellow]")
            await worker.run_update()
        else:
            console.print("[green]Installing new component...[/green]")
            await worker.run_copy()

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
        False, "--force", "-f", help="Force update without asking"
    ),
) -> None:
    """Add or update a component in your project."""
    components_dir = get_components_dir()
    components_dir.mkdir(parents=True, exist_ok=True)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task(f"Installing {component}...", total=None)

        try:
            import asyncio

            asyncio.run(
                install_or_update_component(component, components_dir, branch, force)
            )

            console.print(
                Panel(
                    f"[green]✓[/green] Component {component} has been installed/updated in {components_dir}\n\n"
                    f"Use the component in your templates:\n"
                    f'[cyan]<{component} variant="primary">Content</{component}>[/cyan]',
                    title="Installation Complete",
                    border_style="green",
                )
            )

        except Exception as e:
            console.print(f"[red]Error processing component: {str(e)}[/red]")
            raise typer.Exit(1)


@app.command()
def init() -> None:
    """Initialize basic-components in your project."""
    if not Path("pyproject.toml").exists():
        config = {
            "tool": {
                "basic-components": {  # Changed from "components" to "basic-components"
                    "components_dir": "components",
                    "style": "default",
                }
            }
        }
        with open("pyproject.toml", "wb") as f:
            tomli.dump(config, f)

    components_dir = get_components_dir()
    components_dir.mkdir(parents=True, exist_ok=True)

    console.print(
        Panel(
            "[green]✓[/green] Initialized basic-components\n\n"
            "Next steps:\n"
            "1. Add components to your project:\n"
            "   [cyan]components add button[/cyan]\n"  # Updated command example
            "2. Import and use components in your templates:\n"
            '[cyan]<Button variant="primary">Click me</Button>[/cyan]\n\n'
            "To update components later:\n"
            "   [cyan]components add button --force[/cyan]",  # Updated command example
            title="Setup Complete",
            border_style="green",
        )
    )


def main():
    app()


if __name__ == "__main__":
    app()
