from {{cookiecutter.package_name}}.mcp import mcp


@mcp.tool
def greet(name: str) -> str:
    """Greeting function.

    Parameters
    ----------
    name : str
        Name of person to greet.

    Returns
    -------
    str
        Greetings.
    """
    return f"Hello, {name}!"
