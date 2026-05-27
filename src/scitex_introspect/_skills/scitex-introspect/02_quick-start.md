---
description: |
  [TOPIC] Quick Start
  [DETAILS] Smallest useful example demonstrating the primary use case in
  under 30 seconds.
tags: [scitex-introspect-quick-start]
---

# Quick Start

```python
import scitex_introspect as ix

# Like func? in IPython — signature + type hints + docstring summary
ix.q("json.loads")

# Like func?? in IPython — full source code
ix.qq("json.loads")

# Smart-filtered dir() with metadata
ix.dir("json")

# Recursive module API tree
ix.list_api("json", max_depth=2)
```
