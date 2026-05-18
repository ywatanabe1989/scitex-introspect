#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__members.py

"""Tests for scitex_introspect._members module."""

from scitex_introspect import dir as introspect_dir
from scitex_introspect import get_exports


class TestDir:
    """Tests for dir function."""

    def test_dir_returns_success_true_for_module(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module)
        # Assert
        assert result["success"] is True

    def test_dir_includes_members_key_for_module(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module)
        # Assert
        assert "members" in result

    def test_dir_reports_nonzero_count_for_module(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module)
        # Assert
        assert result["count"] > 0

    def test_dir_public_filter_reports_success(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, filter="public")
        # Assert
        assert result["success"] is True

    def test_dir_public_filter_excludes_underscore_names(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, filter="public")
        # Assert
        assert all(not m["name"].startswith("_") for m in result["members"])

    def test_dir_private_filter_reports_success(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, filter="private")
        # Assert
        assert result["success"] is True

    def test_dir_private_filter_returns_single_underscore_names(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, filter="private")
        # Assert
        assert all(
            m["name"].startswith("_") and not m["name"].startswith("__")
            for m in result["members"]
        )

    def test_dir_dunder_filter_reports_success(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, filter="dunder")
        # Assert
        assert result["success"] is True

    def test_dir_dunder_filter_returns_double_underscore_names(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, filter="dunder")
        # Assert
        assert all(m["name"].startswith("__") for m in result["members"])

    def test_dir_kind_functions_reports_success(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, kind="functions")
        # Assert
        assert result["success"] is True

    def test_dir_kind_functions_returns_only_function_entries(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, kind="functions")
        # Assert
        assert all(m["kind"] == "function" for m in result["members"])

    def test_dir_kind_classes_reports_success(self):
        # Arrange
        target_module = "pathlib"
        # Act
        result = introspect_dir(target_module, kind="classes")
        # Assert
        assert result["success"] is True

    def test_dir_kind_classes_returns_only_class_entries(self):
        # Arrange
        target_module = "pathlib"
        # Act
        result = introspect_dir(target_module, kind="classes")
        # Assert
        assert all(m["kind"] == "class" for m in result["members"])

    def test_dir_public_members_carry_summary_field(self):
        # Arrange
        target_module = "json"
        # Act
        result = introspect_dir(target_module, filter="public")
        # Assert
        assert len([m["summary"] for m in result["members"] if m["summary"]]) > 0

    def test_dir_class_target_reports_success(self):
        # Arrange
        class_target = "pathlib.Path"
        # Act
        result = introspect_dir(class_target)
        # Assert
        assert result["success"] is True

    def test_dir_class_target_reports_nonzero_count(self):
        # Arrange
        class_target = "pathlib.Path"
        # Act
        result = introspect_dir(class_target)
        # Assert
        assert result["count"] > 0

    def test_dir_invalid_path_reports_success_false(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = introspect_dir(invalid_target)
        # Assert
        assert result["success"] is False

    def test_dir_invalid_path_includes_error_key(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = introspect_dir(invalid_target)
        # Assert
        assert "error" in result


class TestGetExports:
    """Tests for get_exports function."""

    def test_get_exports_with_all_reports_success(self):
        # Arrange
        target_module = "json"
        # Act
        result = get_exports(target_module)
        # Assert
        assert result["success"] is True

    def test_get_exports_with_all_includes_exports_key(self):
        # Arrange
        target_module = "json"
        # Act
        result = get_exports(target_module)
        # Assert
        assert "exports" in result

    def test_get_exports_with_all_includes_has_all_key(self):
        # Arrange
        target_module = "json"
        # Act
        result = get_exports(target_module)
        # Assert
        assert "has_all" in result

    def test_get_exports_without_all_reports_success(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_exports(target_module)
        # Assert
        assert result["success"] is True

    def test_get_exports_invalid_path_reports_success_false(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = get_exports(invalid_target)
        # Assert
        assert result["success"] is False
