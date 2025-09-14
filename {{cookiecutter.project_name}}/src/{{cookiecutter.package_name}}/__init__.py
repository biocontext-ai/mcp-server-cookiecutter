from importlib.metadata import version

from {{cookiecutter.package_name}}.main import run_app
from {{cookiecutter.package_name}}.mcp import mcp

__version__ = version("{{cookiecutter.package_name}}")

__all__ = [
    "mcp",
    "run_app",
    "__version__"
]


if __name__ == "__main__":
    run_app()
