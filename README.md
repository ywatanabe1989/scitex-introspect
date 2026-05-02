# scitex-introspect

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>IPython-style introspection for any Python package — `q`, `qq`, `dir`, signatures, source.</b></p>

<p align="center">
  <a href="https://scitex-introspect.readthedocs.io/">Full Documentation</a> · <code>pip install scitex-introspect</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-introspect/"><img src="https://img.shields.io/pypi/v/scitex-introspect.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/scitex-introspect/"><img src="https://img.shields.io/pypi/pyversions/scitex-introspect.svg" alt="Python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/test.yml"><img src="https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/test.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/install-test.yml"><img src="https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/install-test.yml/badge.svg" alt="Install Test"></a>
  <a href="https://codecov.io/gh/ywatanabe1989/scitex-introspect"><img src="https://codecov.io/gh/ywatanabe1989/scitex-introspect/graph/badge.svg" alt="Coverage"></a>
  <a href="https://scitex-introspect.readthedocs.io/en/latest/"><img src="https://readthedocs.org/projects/scitex-introspect/badge/?version=latest" alt="Docs"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/license-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>
<!-- scitex-badges:end -->

---

## Installation

```bash
pip install scitex-introspect
pip install "scitex-introspect[mcp]"   # + MCP server for AI agents
```

## Quick Start

```python
import scitex_introspect as ix

ix.q(my_func)        # Signature with type hints (like `my_func?`)
ix.qq(my_func)       # Full source code (like `my_func??`)
ix.dir(my_pkg)       # List attributes/methods
```

## 2 Interfaces

<details open>
<summary><strong>Python API</strong></summary>

<br>

```python
import scitex_introspect as ix

# IPython-style shortcuts
ix.q(my_func)        # Signature with type hints
ix.qq(my_func)       # Full source code
ix.dir(my_pkg)       # List attributes/methods
ix.list_api(my_pkg)  # Recursive module API tree

# Detailed inspection
ix.signature(my_func)
ix.docstring(my_func)
ix.source(my_func)
ix.members(my_pkg)

# Static analysis
ix.imports(file_path)
ix.call_graph(my_func)
ix.class_hierarchy(MyClass)
ix.examples(my_func)
ix.resolve("scitex.io.save")
```

</details>

<details>
<summary><strong>MCP Server — for AI Agents</strong></summary>

<br>

Install with `pip install "scitex-introspect[mcp]"` and the package
exposes async handlers for IPython-style introspection over MCP — agents
can ask "what's the signature of X?" or "show me the source of Y" without
running Python themselves.

</details>

## Status

Standalone fork of `scitex.introspect`. Pure stdlib core — zero runtime
deps. The umbrella package's `scitex.introspect` import path is preserved
via a `sys.modules`-alias bridge.

## Part of SciTeX

`scitex-introspect` is part of [**SciTeX**](https://scitex.ai). Install via
the umbrella with `pip install scitex[introspect]` to use as
`scitex.introspect` (Python) or `scitex introspect ...` (CLI).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
