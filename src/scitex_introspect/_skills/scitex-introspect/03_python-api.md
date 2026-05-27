---
description: |
  [TOPIC] Python API
  [DETAILS] Public Python API of scitex-introspect — exported functions, signatures,
  return types, and minimal usage examples per function.
tags: [scitex-introspect-python-api]
---

# Python API

```python
import scitex_introspect as ix
```

## IPython-style shortcuts

### `ix.q(dotted_path: str) -> dict`

Signature with type hints (like ``func?`` in IPython).

```python
result = ix.q("json.loads")
# Returns dict with name, signature, docstring summary, etc.
```

### `ix.qq(dotted_path: str) -> dict`

Full source code (like ``func??`` in IPython).

```python
result = ix.qq("json.loads")
# Returns dict with name, source, file path, etc.
```

### `ix.dir(dotted_path: str, ...) -> list`

List attributes/methods of a module or class with metadata.

```python
members = ix.dir("json")
# Returns list of member info dicts with name, kind, docstring preview
```

### `ix.list_api(module, max_depth=3) -> DataFrame`

Recursive module API tree.

```python
api = ix.list_api("json", max_depth=2)
# Returns DataFrame with Type, Name, Description columns
```

## Basic introspection

### `ix.get_docstring(dotted_path, format="raw") -> dict`

Extract and parse docstring.

```python
doc = ix.get_docstring("math.sqrt")
# Returns dict with summary, sections, params, returns
```

### `ix.get_exports(dotted_path) -> dict`

Return a module's ``__all__`` or public names.

```python
exports = ix.get_exports("json")
# Returns dict with module, exports list, has_all flag
```

### `ix.find_examples(dotted_path, search_paths=None) -> dict`

Find usage examples in tests/ and examples/ directories.

```python
examples = ix.find_examples("json.loads")
# Returns dict with function name, examples list per file
```

## Advanced: Class hierarchy

### `ix.get_class_hierarchy(dotted_path) -> dict`

MRO + known subclasses.

```python
hierarchy = ix.get_class_hierarchy("json.JSONDecoder")
# Returns dict with class, mro list, subclasses list
```

### `ix.get_mro(dotted_path, include_builtins=False) -> dict`

Method Resolution Order only.

```python
mro = ix.get_mro("json.JSONDecoder")
# Returns dict with class, mro list
```

## Advanced: Type hints

### `ix.get_type_hints_detailed(dotted_path) -> dict`

PEP-563-resolved type annotations.

```python
hints = ix.get_type_hints_detailed("json.loads")
# Returns dict with parameters, return_annotation, resolved hints
```

### `ix.get_class_annotations(dotted_path) -> dict`

Class variable and method annotations.

```python
ann = ix.get_class_annotations("json.JSONDecoder")
# Returns dict with class annotations
```

## Advanced: Imports

### `ix.get_imports(dotted_path, categorize=False) -> dict`

Static import analysis using AST.

```python
imports = ix.get_imports("json", categorize=True)
# Returns dict with raw_imports list, and optionally categorized
```

### `ix.get_dependencies(dotted_path, max_depth=2) -> dict`

Module dependency tree.

```python
deps = ix.get_dependencies("json", max_depth=1)
# Returns dict with tree, max_depth
```

## Advanced: Call graph

### `ix.get_call_graph(dotted_path, max_depth=2, internal_only=True) -> dict`

Function call graph (with timeout protection).

```python
graph = ix.get_call_graph("json.loads")
# Returns dict with function, calls list, callees list
```

### `ix.get_function_calls(dotted_path) -> dict`

Simple outgoing calls list.

```python
calls = ix.get_function_calls("json.loads")
# Returns dict with function, calls list
```

## Resolution

### `ix.resolve_object(dotted_path) -> tuple[Any, str | None]`

Resolve a dotted path to a Python object.

```python
obj, error = ix.resolve_object("json.loads")
# Returns (function_object, None) or (None, error_message)
```

### `ix.get_type_info(dotted_path) -> dict`

Detailed type information about a callable.

```python
info = ix.get_type_info("json.loads")
# Returns dict with type, module, signature, annotations
```
