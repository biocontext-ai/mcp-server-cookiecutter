from unittest.mock import AsyncMock, MagicMock

import pytest
from fastmcp import FastMCP


@pytest.fixture
def mock_mcp_app():
    """Create a mock FastMCP instance for testing."""
    mock_app = MagicMock(spec=FastMCP)
    mock_app.name = "Test MCP App"

    # Create proper mocks for tools with string names
    tool_mock = MagicMock()
    tool_mock.name = "test_tool"
    mock_app.get_tools = AsyncMock(return_value={"test_tool": tool_mock})

    # Create a resource mock with name attribute set to None to match the application behavior
    resource_mock = MagicMock()
    resource_mock.name = None
    mock_app.get_resources = AsyncMock(return_value={"test_resource": resource_mock})

    # Create template mock with string name
    template_mock = MagicMock()
    template_mock.name = "test_template"
    mock_app.get_resource_templates = AsyncMock(return_value={"test_template": template_mock})

    mock_app.import_server = AsyncMock()
    mock_app.http_app = MagicMock(return_value=MagicMock())
    return mock_app
