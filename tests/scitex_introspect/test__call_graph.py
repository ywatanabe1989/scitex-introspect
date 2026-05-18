#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__call_graph.py

"""Tests for scitex_introspect._call_graph module."""

from scitex_introspect import get_call_graph, get_function_calls


class TestGetCallGraph:
    """Tests for get_call_graph function."""

    def test_get_call_graph_function_reports_success(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_call_graph(target)
        # Assert
        assert result["success"] is True

    def test_get_call_graph_function_includes_calls_key(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_call_graph(target)
        # Assert
        assert "calls" in result

    def test_get_call_graph_function_includes_call_count_key(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_call_graph(target)
        # Assert
        assert "call_count" in result

    def test_get_call_graph_module_reports_success(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_call_graph(target_module)
        # Assert
        assert result["success"] is True

    def test_get_call_graph_module_includes_graph_or_calls(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_call_graph(target_module)
        # Assert
        assert "graph" in result or "calls" in result

    def test_call_graph_timeout_returns_envelope_with_success_key(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_call_graph(target_module, timeout_seconds=30)
        # Assert
        assert "success" in result

    def test_call_graph_internal_only_reports_success(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_call_graph(target, internal_only=True)
        # Assert
        assert result["success"] is True

    def test_call_graph_internal_only_false_reports_success(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_call_graph(target, internal_only=False)
        # Assert
        assert result["success"] is True

    def test_call_graph_invalid_path_reports_success_false(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = get_call_graph(invalid_target)
        # Assert
        assert result["success"] is False


class TestGetFunctionCalls:
    """Tests for get_function_calls function."""

    def test_get_function_calls_reports_success_true(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_function_calls(target)
        # Assert
        assert result["success"] is True

    def test_get_function_calls_includes_calls_key(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_function_calls(target)
        # Assert
        assert "calls" in result

    def test_get_function_calls_builtin_reports_success_false(self):
        # Arrange
        builtin_target = "len"
        # Act
        result = get_function_calls(builtin_target)
        # Assert
        assert result["success"] is False
