from {{cookiecutter.package_name}}.mcp import mcp


@mcp.tool
def greet(name: str) -> str:
    """Greeting function.

    Params:
        name (str): Name of person to greet.

    Returns: Greetings.
    ReturnType: str
    """
    return f"Hello, {name}!"
