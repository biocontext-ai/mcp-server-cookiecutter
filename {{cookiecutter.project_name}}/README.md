# {{ cookiecutter.project_name }}

[![BioContextAI - Registry](https://img.shields.io/badge/Registry-package?style=flat&label=BioContextAI&labelColor=%23fff&color=%233555a1&link=https%3A%2F%2Fbiocontext.ai%2Fregistry)](https://biocontext.ai/registry)
[![Tests][badge-tests]][tests]
[![Documentation][badge-docs]][documentation]

[badge-tests]: https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/test.yaml?branch=main
[badge-docs]: https://img.shields.io/readthedocs/{{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Getting started

Please refer to the [documentation][],
in particular, the [API documentation][].

You can also find the project on [BioContextAI](https://biocontext.ai), the community-hub for biomedical MCP servers: [{{ cookiecutter.project_name }} on BioContextAI](https://biocontext.ai/registry/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}).

## Installation

You need to have Python 3.10 or newer installed on your system.
If you don't have Python installed, we recommend installing [uv][].

There are several alternative options to install {{ cookiecutter.project_name }}:

### 1. Use `uvx` to run it immediately
After publication to PyPI:
```bash
uvx {{ cookiecutter.package_name }}
```

Or from a Git repository:

```bash
uvx git+https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}.git@main
```

### 2. Include it in one of various clients that supports the `mcp.json` standard

If your MCP server is published to PyPI, use the following configuration:

```json
{
  "mcpServers": {
    "{{ cookiecutter.github_repo }}": {
      "command": "uvx",
      "args": ["{{ cookiecutter.package_name }}"]
    }
  }
}
```
In case the MCP server is not yet published to PyPI, use this configuration:

```json
{
  "mcpServers": {
    "{{ cookiecutter.github_repo }}": {
      "command": "uvx",
      "args": ["git+https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}.git@main"]
    }
  }
}
```

For purely local development, use the following configuration:

```json
{
  "mcpServers": {
    "{{ cookiecutter.github_repo }}": {
      "command": "uvx",
      "args": ["--from", "path/to/repository", "{{ cookiecutter.package_name }}"]
    }
  }
}
```

If you want to reuse and existing environment for local development, use the following configuration:

```json
{
  "mcpServers": {
    "{{ cookiecutter.github_repo }}": {
      "command": "uv",
      "args": ["run", "--directory", "path/to/repository", "{{ cookiecutter.package_name }}"]
    }
  }
}
```

### 3. Install it through `pip`:

```bash
pip install --user {{ cookiecutter.package_name }}
```

### 4. Install the latest development version:

```bash
pip install git+https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}.git@main
```

## Contact

If you found a bug, please use the [issue tracker][].

## Citation

> t.b.a

[uv]: https://github.com/astral-sh/uv
[issue tracker]: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_name }}/issues
[tests]: https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }}/actions/workflows/test.yaml
[documentation]: https://{{ cookiecutter.project_name }}.readthedocs.io
[changelog]: https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/changelog.html
[api documentation]: https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/api.html
[pypi]: https://pypi.org/project/{{ cookiecutter.project_name }}
