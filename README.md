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
@misc{kuehlCommunitybasedBiomedicalContext2025,
  title = {Community-Based Biomedical Context to Unlock Agentic Systems},
  author = {Kuehl, Malte and Schaub, Darius P. and Carli, Francesco and Heumos, Lukas and {Fern{\'a}ndez-Zapata}, Camila and Kaiser, Nico and Schaul, Jonathan and Panzer, Ulf and Bonn, Stefan and Lobentanzer, Sebastian and {Saez-Rodriguez}, Julio and Puelles, Victor G.},
  year = {2025},
  month = jul,
  pages = {2025.07.21.665729},
  publisher = {bioRxiv},
  issn = {2692-8205},
  doi = {10.1101/2025.07.21.665729},
  urldate = {2025-07-28},
  abstract = {Large language models (LLMs) face reliability challenges stemming from hallucinations and insufficient access to validated scientific resources. Existing solutions are often fragmented and limited to specific applications, hindering broader adoption and interoperability. Here, we present Biomedical Context for Artificial Intelligence (BioContextAI), an open-source initiative centered on Model Context Protocol (MCP) servers to address these limitations. BioContextAI provides a community-oriented registry for discovering domain-specific MCP servers and a proof-of-concept server implementation that integrates widely-used biomedical knowledgebases. By enabling standardized access to validated scientific knowledge, BioContextAI aims to facilitate the development of composable agentic systems for biomedical research. Together, this work contributes to an emerging ecosystem of community-driven approaches for expanding the capabilities and reliability of biomedical AI systems.},
  archiveprefix = {bioRxiv},
  copyright = {{\copyright} 2025, Posted by Cold Spring Harbor Laboratory. This pre-print is available under a Creative Commons License (Attribution 4.0 International), CC BY 4.0, as described at http://creativecommons.org/licenses/by/4.0/},
}
```
