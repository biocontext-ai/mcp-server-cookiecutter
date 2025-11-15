# BioContextAI MCP Server Cookiecutter Template

Cookiecutter template for a Python-based biomedical MCP server with [FastMCP](https://gofastmcp.com/). For more information about the BioContextAI project, please refer to https://biocontext.ai.

## Usage

Use this template with `cookiecutter` by running:

```bash
uvx cookiecutter https://github.com/biocontext-ai/mcp-server-cookiecutter.git
```

Alternatively, you can also install `cookiecutter` with `pip`:

```bash
python3 -m pip install --user cookiecutter
cookiecutter https://github.com/biocontext-ai/mcp-server-cookiecutter.git
```

## Publishing Your MCP Server

## Python Package

We recommend that you publish your MCP server through [PyPi](https://pypi.org) so that it can be installed through `uv` and `pip`. The easiest way to do so, is to create a release on the GitHub repository of your MCP server and use the included `release.yaml` GitHub action. Make sure to add the repository and action as a trusted publisher in your PyPi account before releasing the first version.

With the setup of this cookiecutter, users will be able to simple run your MCP server with:

```bash
uvx your_package_name
```

To include it in one of various clients that supports the `mcp.json` standard, please use:

```jsonc
{
  "mcpServers": {
    "server-name": {
      "command": "uvx",
      "args": ["your_package_name"],
      "env": {
        "UV_PYTHON": "3.12" // or required version
      }
    }
  }
}
```

### Submit to BioContextAI

To make your MCP server discoverable to the community, please consider submitting it to the [BioContextAI Registry](https://biocontext.ai/registry). You can create the required metadata file easily through our online editor at: https://biocontext.ai/registry/editor. Once you have this file ready, simply open a pull request on the [Registry repository](https://github.com/biocontext-ai/registry). We will review your submission, include it in the Registry and announce it on social media.

You are also welcome to join our [community](https://scverse.zulipchat.com/#narrow/channel/518508) within the scverse® Zulip to connect with users, developers and present your work.

## Citation

If this template is useful to your research, please cite:

```bibtex
@article{BioContext_AI_Kuehl_Schaub_2025,
  title={BioContextAI is a community hub for agentic biomedical systems},
  url={http://dx.doi.org/10.1038/s41587-025-02900-9},
  urldate = {2025-11-06},
  doi={10.1038/s41587-025-02900-9},
  year = {2025},
  month = nov,
  journal={Nature Biotechnology},
  publisher={Springer Science and Business Media LLC},
  author={Kuehl, Malte and Schaub, Darius P. and Carli, Francesco and Heumos, Lukas and Hellmig, Malte and Fernández-Zapata, Camila and Kaiser, Nico and Schaul, Jonathan and Kulaga, Anton and Usanov, Nikolay and Koutrouli, Mikaela and Ergen, Can and Palla, Giovanni and Krebs, Christian F. and Panzer, Ulf and Bonn, Stefan and Lobentanzer, Sebastian and Saez-Rodriguez, Julio and Puelles, Victor G.},
  year={2025},
  month=nov,
  language={en},
}
```
