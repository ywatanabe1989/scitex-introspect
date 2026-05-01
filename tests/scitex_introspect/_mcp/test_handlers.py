#!/usr/bin/env python3
"""Tests for scitex_introspect._mcp.handlers — async MCP wrappers.

Each handler delegates to the corresponding scitex_introspect public
function and wraps exceptions into ``{"success": False, "error": str}``
envelopes. Tests:
  - happy path returns the underlying function's value
  - exception path returns the error envelope
"""

import asyncio

import pytest

from scitex_introspect._mcp.handlers import (
    docstring_handler,
    q_handler,
    qq_handler,
)


def _run(coro):
    return asyncio.run(coro)


class TestQHandler:
    def test_returns_signature_dict_for_real_callable(self):
        # `len` is a stable, always-importable target.
        result = _run(q_handler("builtins.len"))
        # Successful introspection yields a dict that doesn't carry
        # `success: False`.
        assert isinstance(result, dict)
        assert result.get("success") is not False

    def test_unknown_path_returns_error_envelope(self):
        result = _run(q_handler("nonexistent.module.target"))
        assert result["success"] is False
        assert "error" in result


class TestDocstringHandler:
    def test_returns_dict_for_known_target(self):
        result = _run(docstring_handler("builtins.len"))
        assert isinstance(result, dict)
        assert result.get("success") is not False

    def test_unknown_path_returns_error_envelope(self):
        result = _run(docstring_handler("nope.nope"))
        assert result["success"] is False
        assert "error" in result


class TestQqHandler:
    def test_unknown_path_returns_error_envelope(self):
        result = _run(qq_handler("nope.nope"))
        assert result["success"] is False
        assert "error" in result


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
