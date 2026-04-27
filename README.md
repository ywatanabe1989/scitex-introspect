# scitex-introspect

<!-- scitex-badges:start -->
[![PyPI](https://img.shields.io/pypi/v/scitex-introspect.svg)](https://pypi.org/project/scitex-introspect/)
[![Python](https://img.shields.io/pypi/pyversions/scitex-introspect.svg)](https://pypi.org/project/scitex-introspect/)
[![Tests](https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/test.yml)
[![Install Test](https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/install-test.yml/badge.svg)](https://github.com/ywatanabe1989/scitex-introspect/actions/workflows/install-test.yml)
[![Coverage](https://codecov.io/gh/ywatanabe1989/scitex-introspect/graph/badge.svg)](https://codecov.io/gh/ywatanabe1989/scitex-introspect)
[![Docs](https://readthedocs.org/projects/scitex-introspect/badge/?version=latest)](https://scitex-introspect.readthedocs.io/en/latest/)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
<!-- scitex-badges:end -->


IPython-style introspection for any Python package, extracted from the [SciTeX](https://github.com/ywatanabe1989/scitex-python) ecosystem as a standalone, zero-dep package.

## Install

```bash
pip install scitex-introspect
pip install "scitex-introspect[mcp]"   # + MCP server for AI agents
```

## API

```python
import scitex_introspect as ix

# IPython-style shortcuts
ix.q(my_func)        # Signature with type hints (like `my_func?`)
ix.qq(my_func)       # Full source code (like `my_func??`)
ix.dir(my_pkg)       # List attributes/methods
ix.list_api(my_pkg)  # Recursive module API tree

# Detailed inspection
ix.signature(my_func)
ix.docstring(my_func)
ix.source(my_func)
ix.members(my_pkg)

# Static analysis
ix.imports(file_path)        # Imports of a Python file
ix.call_graph(my_func)       # What functions does this call?
ix.class_hierarchy(MyClass)  # MRO + base classes
ix.examples(my_func)         # Doctest / docstring examples
ix.resolve("scitex.io.save") # Walk dotted path → object
```

## Status

Standalone fork of `scitex.introspect`. Pure stdlib — zero deps. The umbrella
package's `scitex.introspect` import path is preserved via a `sys.modules`-alias
bridge. 76/77 tests pass (1 skipped).

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).
