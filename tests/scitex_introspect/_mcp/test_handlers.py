#!/usr/bin/env python3
"""Tests for scitex_introspect._mcp.handlers — async MCP wrappers.

Each handler delegates to the corresponding scitex_introspect public
function and wraps exceptions into ``{"success": False, "error": str}``
envelopes. Tests:
  - happy path returns the underlying function's value
  - exception path returns the error envelope
"""

import asyncio
import os

import pytest

from scitex_introspect._mcp.handlers import (
    docstring_handler,
    q_handler,
    qq_handler,
)


def _run(coro):
    return asyncio.run(coro)


class TestQHandler:
    def test_q_handler_returns_dict_for_known_target(self):
        # Arrange
        target = "builtins.len"
        # Act
        result = _run(q_handler(target))
        # Assert
        assert isinstance(result, dict)

    def test_q_handler_known_target_is_not_error_envelope(self):
        # Arrange
        target = "builtins.len"
        # Act
        result = _run(q_handler(target))
        # Assert
        assert result.get("success") is not False

    def test_q_handler_unknown_path_reports_success_false(self):
        # Arrange
        unknown_target = "nonexistent.module.target"
        # Act
        result = _run(q_handler(unknown_target))
        # Assert
        assert result["success"] is False

    def test_q_handler_unknown_path_includes_error_key(self):
        # Arrange
        unknown_target = "nonexistent.module.target"
        # Act
        result = _run(q_handler(unknown_target))
        # Assert
        assert "error" in result


class TestDocstringHandler:
    def test_docstring_handler_returns_dict_for_known_target(self):
        # Arrange
        target = "builtins.len"
        # Act
        result = _run(docstring_handler(target))
        # Assert
        assert isinstance(result, dict)

    def test_docstring_handler_known_target_is_not_error_envelope(self):
        # Arrange
        target = "builtins.len"
        # Act
        result = _run(docstring_handler(target))
        # Assert
        assert result.get("success") is not False

    def test_docstring_handler_unknown_path_reports_success_false(self):
        # Arrange
        unknown_target = "nope.nope"
        # Act
        result = _run(docstring_handler(unknown_target))
        # Assert
        assert result["success"] is False

    def test_docstring_handler_unknown_path_includes_error_key(self):
        # Arrange
        unknown_target = "nope.nope"
        # Act
        result = _run(docstring_handler(unknown_target))
        # Assert
        assert "error" in result


class TestQqHandler:
    def test_qq_handler_unknown_path_reports_success_false(self):
        # Arrange
        unknown_target = "nope.nope"
        # Act
        result = _run(qq_handler(unknown_target))
        # Assert
        assert result["success"] is False

    def test_qq_handler_unknown_path_includes_error_key(self):
        # Arrange
        unknown_target = "nope.nope"
        # Act
        result = _run(qq_handler(unknown_target))
        # Assert
        assert "error" in result


if __name__ == "__main__":
    pytest.main([os.path.abspath(__file__), "-v"])

# EOF
