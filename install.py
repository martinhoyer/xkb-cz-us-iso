#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "rich",
# ]
# ///
"""Czech-US ISO Keyboard Layout Installer.

This script installs the custom XKB layout to ~/.config/xkb/
Files are fetched from the GitHub repository.
"""

import sys
from pathlib import Path
from typing import TYPE_CHECKING, cast
from urllib.request import urlopen

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.table import Table

if TYPE_CHECKING:
    from http.client import HTTPResponse

console = Console()

# GitHub repository URLs
GITHUB_BASE = "https://raw.githubusercontent.com/martinhoyer/xkb-cz-us-iso/main"
FILES_TO_DOWNLOAD = {
    "symbols/cz_us_iso": f"{GITHUB_BASE}/symbols/cz_us_iso",
    "rules/evdev.xml": f"{GITHUB_BASE}/rules/evdev.xml",
}


def get_xkb_config_dir() -> Path:
    """Get the user's XKB configuration directory."""
    return Path.home() / ".config" / "xkb"


def download_file(url: str, destination: Path) -> bool:
    """Download a file from URL to destination path."""
    try:
        console.print(f"[dim]Downloading {url}...[/dim]")
        with cast("HTTPResponse", urlopen(url, timeout=30)) as http_response:
            content: bytes = http_response.read()

        destination.parent.mkdir(parents=True, exist_ok=True)
        _ = destination.write_bytes(content)
        return True
    except Exception as e:
        console.print(f"[red]Error downloading {url}:[/red] {e}")
        return False


def install_layout() -> bool:
    """Install the keyboard layout files."""
    xkb_dir = get_xkb_config_dir()

    # Create target directories
    symbols_dir = xkb_dir / "symbols"
    rules_dir = xkb_dir / "rules"

    try:
        symbols_dir.mkdir(parents=True, exist_ok=True)
        rules_dir.mkdir(parents=True, exist_ok=True)
        console.print(f"[green]✓[/green] Created directories in {xkb_dir}")
    except Exception as e:
        console.print(f"[red]Error creating directories:[/red] {e}")
        return False

    # Download and install files
    success = True
    for relative_path, url in FILES_TO_DOWNLOAD.items():
        destination = xkb_dir / relative_path
        if download_file(url, destination):
            console.print(f"[green]✓[/green] Installed {relative_path}")
        else:
            success = False

    return success


def show_activation_instructions() -> None:
    """Display instructions for activating the layout."""
    table = Table(title="Activation Instructions", show_header=False, box=None)
    table.add_column(style="cyan bold")
    table.add_column()

    table.add_row(
        "GNOME",
        "Settings → Keyboard → Input Sources → + → Search for 'Czech (US layout, ISO keyboard)'",
    )
    table.add_row(
        "KDE",
        "System Settings → Input Devices → Keyboard → Layouts → Add → Search for 'cz_us_iso'",
    )
    table.add_row("CLI", "setxkbmap cz_us_iso")

    console.print()
    console.print(table)
    console.print()
    console.print(
        "[yellow]Note:[/yellow] You may need to log out and log back in for the layout to appear in your settings.",
    )


def show_quick_reference() -> None:
    """Display a quick reference of key mappings."""
    table = Table(title="Quick Reference", show_header=True)
    table.add_column("Key", style="cyan")
    table.add_column("Normal", style="green")
    table.add_column("Shift", style="yellow")
    table.add_column("Level3", style="magenta")

    mappings = [
        ("1-0", "+ěščřžýáíé", "!@#$%^&*()", "1234567890"),
        ("[", "[", "{", "ú"),
        (";", ";", ":", "ů"),
        ("\\", "\\", "|", "ň"),
    ]

    for key, normal, shift, level3 in mappings:
        table.add_row(key, normal, shift, level3)

    console.print()
    console.print(table)
    console.print()
    console.print(
        "[dim]Level3 modifier: Extra key between Left Shift and Z (<>| key on ISO keyboards)[/dim]",
    )


def main() -> int:
    """Main installation routine."""
    console.print(
        Panel.fit(
            "[bold cyan]Czech-US ISO Keyboard Layout Installer[/bold cyan]\nInstalling custom XKB layout for bilingual typing",
            border_style="cyan",
        ),
    )
    console.print()

    # Show what will be installed
    xkb_dir = get_xkb_config_dir()
    console.print(f"Installation target: [cyan]{xkb_dir}[/cyan]")
    console.print(f"Source: [cyan]{GITHUB_BASE}[/cyan]")
    console.print()

    # Confirm installation
    if not Confirm.ask("Proceed with installation?", default=True):
        console.print("[yellow]Installation cancelled.[/yellow]")
        return 0

    console.print()

    # Install
    if install_layout():
        console.print()
        console.print("[bold green]✓ Installation successful![/bold green]")
        show_activation_instructions()
        show_quick_reference()
        return 0
    console.print()
    console.print("[bold red]✗ Installation failed![/bold red]")
    return 1


if __name__ == "__main__":
    sys.exit(main())
