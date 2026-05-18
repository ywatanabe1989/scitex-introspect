#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__type_hints.py

"""Tests for scitex_introspect._type_hints module."""

from scitex_introspect import get_class_annotations, get_type_hints_detailed


class TestGetTypeHintsDetailed:
    """Tests for get_type_hints_detailed function."""

    def test_get_type_hints_reports_success_true(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_type_hints_detailed(target)
        # Assert
        assert result["success"] is True

    def test_get_type_hints_returns_hints_or_count_key(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_type_hints_detailed(target)
        # Assert
        assert "hints" in result or "hint_count" in result

    def test_type_hints_optional_reports_success(self):
        # Arrange
        target = "scitex_introspect._signature.q"
        # Act
        result = get_type_hints_detailed(target)
        # Assert
        assert result["success"] is True

    def test_type_hints_optional_each_hint_has_is_optional_flag(self):
        # Arrange
        target = "scitex_introspect._signature.q"
        # Act
        result = get_type_hints_detailed(target)
        # Assert
        assert all("is_optional" in info for info in result.get("hints", {}).values())

    def test_type_hints_return_type_reports_success(self):
        # Arrange
        target = "scitex_introspect._resolve.resolve_object"
        # Act
        result = get_type_hints_detailed(target)
        # Assert
        assert result["success"] is True

    def test_type_hints_class_target_reports_success(self):
        # Arrange
        class_target = "pathlib.Path"
        # Act
        result = get_type_hints_detailed(class_target)
        # Assert
        assert result["success"] is True

    def test_type_hints_no_hints_reports_success(self):
        # Arrange
        target = "json.loads"
        # Act
        result = get_type_hints_detailed(target)
        # Assert
        assert result["success"] is True

    def test_type_hints_invalid_path_reports_success_false(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = get_type_hints_detailed(invalid_target)
        # Assert
        assert result["success"] is False


class TestGetClassAnnotations:
    """Tests for get_class_annotations function."""

    def test_get_class_annotations_reports_success_true(self):
        # Arrange
        class_target = "pathlib.PurePath"
        # Act
        result = get_class_annotations(class_target)
        # Assert
        assert result["success"] is True

    def test_get_class_annotations_includes_class_vars_or_methods(self):
        # Arrange
        class_target = "pathlib.PurePath"
        # Act
        result = get_class_annotations(class_target)
        # Assert
        assert "class_vars" in result or "methods" in result

    def test_class_annotations_non_class_reports_success_false(self):
        # Arrange
        non_class_target = "json.dumps"
        # Act
        result = get_class_annotations(non_class_target)
        # Assert
        assert result["success"] is False

    def test_class_annotations_non_class_carries_error_signal(self):
        # Arrange
        non_class_target = "json.dumps"
        # Act
        result = get_class_annotations(non_class_target)
        # Assert
        assert "not a class" in result.get("error", "") or "error" in result
