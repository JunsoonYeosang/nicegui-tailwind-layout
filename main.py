from collections.abc import Callable, Iterator
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from nicegui import ui

TEMPLATES_DIR = "templates"
PYCACHE = "__pycache__"
BASE_URL = "http://localhost:8080"


@dataclass
class Template:
    """Template information container."""

    path: Path
    route: str
    func: Callable[[], None]


def get_template_files() -> Iterator[Path]:
    """Get all Python template files excluding __pycache__."""
    return (f for f in Path(TEMPLATES_DIR).glob("*.py") if PYCACHE not in str(f))


def load_template(template_file: Path) -> Template:
    """Load a template module and return its info."""
    module_path = f"{TEMPLATES_DIR}.{template_file.stem}"
    module = import_module(module_path)
    route = f"/{template_file.stem}"

    return Template(path=template_file, route=route, func=getattr(module, "app"))


# Load all templates
templates = [load_template(f) for f in get_template_files()]

# Set up routes
for template in templates:
    ui.page(template.route)(template.func)
    print(f"Route: {BASE_URL}{template.route}")


@ui.page("/")
def home() -> None:
    """Home page with links to all templates."""
    with ui.card().classes("w-full p-4 mb-4"):
        ui.label("NiceGUI Layout Templates").classes("text-2xl mb-2")
        ui.label("Click on any template to view").classes("text-gray-500")

    with ui.grid(columns=3).classes("gap-4 w-full"):
        # Sort templates by name for consistent display
        for template in sorted(templates, key=lambda t: t.path.stem):
            ui.button(
                template.path.stem,
                on_click=lambda t=template.route: ui.navigate.to(t),
            ).classes("h-[100px]")


if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
