#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__docstring.py

"""Tests for scitex_introspect._docstring module."""

from scitex_introspect import get_docstring


class TestGetDocstring:
    """Tests for get_docstring function."""

    def test_get_docstring_returns_success_true(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target)
        # Assert
        assert result["success"] is True

    def test_get_docstring_includes_docstring_key(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target)
        # Assert
        assert "docstring" in result

    def test_get_docstring_returns_nonempty_text(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target)
        # Assert
        assert len(result["docstring"]) > 0

    def test_docstring_raw_format_reports_success(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target, format="raw")
        # Assert
        assert result["success"] is True

    def test_docstring_raw_format_has_docstring_key(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target, format="raw")
        # Assert
        assert "docstring" in result

    def test_docstring_summary_format_reports_success(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target, format="summary")
        # Assert
        assert result["success"] is True

    def test_docstring_summary_format_has_docstring_key(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target, format="summary")
        # Assert
        assert "docstring" in result

    def test_docstring_summary_is_not_longer_than_raw(self):
        # Arrange
        target = "json.dumps"
        raw_result = get_docstring(target, format="raw")
        # Act
        summary_result = get_docstring(target, format="summary")
        # Assert
        assert len(summary_result["docstring"]) <= len(raw_result["docstring"])

    def test_docstring_parsed_format_reports_success(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target, format="parsed")
        # Assert
        assert result["success"] is True

    def test_docstring_parsed_format_includes_sections_key(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = get_docstring(target, format="parsed")
        # Assert
        assert "sections" in result

    def test_docstring_missing_target_returns_envelope_with_success_key(self):
        # Arrange
        target_without_docstring = "builtins.None"
        # Act
        result = get_docstring(target_without_docstring)
        # Assert
        assert "success" in result

    def test_docstring_invalid_path_reports_success_false(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = get_docstring(invalid_target)
        # Assert
        assert result["success"] is False

    def test_docstring_invalid_path_includes_error_key(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = get_docstring(invalid_target)
        # Assert
        assert "error" in result
