from fastmcp import FastMCP, Client

from {{cookiecutter.package_name}} import __version__, mcp


def test_package_has_version():
    """Testing package version exist."""
    assert {{cookiecutter.package_name}}.__version__ is not None

async def test_mcp_server():
    """Testing MCP server."""
    async with Client(mcp) as client:
        await client.call_tool("greet", {"name": "test"})
