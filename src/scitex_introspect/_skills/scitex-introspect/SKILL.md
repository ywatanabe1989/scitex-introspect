---
name: scitex-introspect
description: IPython-style introspection for any Python package. `q(obj)` mirrors IPython's `obj?` (signature + type hints + docstring summary). `qq(obj)` mirrors `obj??` (full source). `dir(obj)` lists attributes/methods with smart filtering. `list_api(module)` walks the module tree and returns the recursive public API as a structured tree. `get_docstring(obj)`, `get_exports(module)` (returns `__all__` contents), `find_examples(module)` (scans tests/ and examples/ for usage). Advanced: `get_class_hierarchy(cls)` (MRO + subclasses), `get_call_graph`, `get_dependencies`, `get_imports`, `get_signature`, `get_type_hints`. Drop-in replacement for opening a REPL, importing the target, and running `inspect.getsource(...)` by hand. Use whenever an agent needs to understand an unknown package's public surface, find usage examples without grepping, or inspect a class hierarchy without spelunking source files.
primary_interface: python
interfaces:
  python: 3
  cli: 1
  mcp: 1
  skills: 2
  hook: 0
  http: 0
canonical-location: scitex-introspect/src/scitex_introspect/_skills/scitex-introspect/SKILL.md
tags: [scitex-introspect, scitex-package, introspection, api-discovery, ipython]
---

> **Interfaces:** Python ⭐⭐⭐ (primary) · CLI ⭐ · MCP ⭐ · Skills ⭐⭐ · Hook — · HTTP —

# scitex-introspect

IPython-like introspection for any Python package, programmatic.

## Quick reference

```python
import scitex_introspect as ix

ix.q(some_func)              # like `some_func?` — signature + docstring
ix.qq(some_func)             # like `some_func??` — full source
ix.dir(some_module)          # smart-filtered dir()
ix.list_api(some_module)     # recursive API tree (dict)
```

## Discoverability

```python
ix.get_docstring(obj)        # parsed docstring (sections)
ix.get_exports(module)       # __all__ contents
ix.find_examples(module)     # usage from tests/ and examples/
```

## Class introspection

```python
ix.get_class_hierarchy(cls)  # MRO + known subclasses
ix.get_call_graph(func)      # function call graph (best-effort)
ix.get_dependencies(module)  # imported names per submodule
ix.get_imports(file_path)    # raw import list
ix.get_signature(callable)   # rich signature with defaults / annotations
ix.get_type_hints(func)      # PEP-563-resolved hints
```

## When to use

- ✅ Agent-mode exploration of an unfamiliar package
- ✅ Programmatic generation of API docs / cheatsheets
- ✅ Finding existing usage of a function before refactoring
- ❌ Performance-sensitive paths — introspection is reflective and slow

## See also

- `scitex-dev` — the higher-level `ecosystem` CLI uses scitex-introspect
  for its `list-python-apis` subcommand

## Sub-skills

### Core (01–09)
- [01_installation.md](01_installation.md) — install + import sanity check
- [02_quick-start.md](02_quick-start.md) — 30-second tour
- [03_python-api.md](03_python-api.md) — Python API surface
