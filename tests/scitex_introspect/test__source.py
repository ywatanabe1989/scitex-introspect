#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__source.py

"""Tests for scitex_introspect._source module."""

from scitex_introspect import qq


class TestQQ:
    """Tests for qq function."""

    def test_qq_returns_success_true_for_function(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target)
        # Assert
        assert result["success"] is True

    def test_qq_includes_source_key_for_function(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target)
        # Assert
        assert "source" in result

    def test_qq_includes_file_key_for_function(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target)
        # Assert
        assert "file" in result

    def test_qq_includes_line_start_key_for_function(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target)
        # Assert
        assert "line_start" in result

    def test_qq_includes_line_count_key_for_function(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target)
        # Assert
        assert "line_count" in result

    def test_qq_source_contains_def_keyword(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target)
        # Assert
        assert "def resolve_object" in result["source"]

    def test_qq_max_lines_reports_success(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target, max_lines=5)
        # Assert
        assert result["success"] is True

    def test_qq_max_lines_caps_output_line_count(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        max_lines = 5
        # Act
        result = qq(target, max_lines=max_lines)
        # Assert
        # max_lines + 1 to allow a truncation indicator line
        assert len(result["source"].strip().split("\n")) <= max_lines + 1

    def test_qq_without_decorators_reports_success(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target, include_decorators=False)
        # Assert
        assert result["success"] is True

    def test_qq_without_decorators_first_line_starts_with_def(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = qq(target, include_decorators=False)
        # Assert
        assert result["source"].strip().split("\n")[0].strip().startswith("def ")

    def test_qq_builtin_reports_success_false(self):
        # Arrange
        builtin_target = "len"
        # Act
        result = qq(builtin_target)
        # Assert
        assert result["success"] is False

    def test_qq_class_reports_success_true(self):
        # Arrange
        class_target = "pathlib.PurePath"
        # Act
        result = qq(class_target)
        # Assert
        assert result["success"] is True

    def test_qq_class_source_contains_class_keyword(self):
        # Arrange
        class_target = "pathlib.PurePath"
        # Act
        result = qq(class_target)
        # Assert
        assert "class PurePath" in result["source"]

    def test_qq_invalid_path_reports_success_false(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = qq(invalid_target)
        # Assert
        assert result["success"] is False

    def test_qq_invalid_path_includes_error_key(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = qq(invalid_target)
        # Assert
        assert "error" in result
