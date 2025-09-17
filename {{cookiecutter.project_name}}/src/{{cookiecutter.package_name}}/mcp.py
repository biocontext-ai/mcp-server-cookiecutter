from fastmcp import FastMCP

mcp: FastMCP = FastMCP(
    name="{{cookiecutter.project_name}}",
    instructions="{{cookiecutter.project_description}}",
    on_duplicate_tools="error",
)
