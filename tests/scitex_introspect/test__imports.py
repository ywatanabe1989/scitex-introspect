#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__imports.py

"""Tests for scitex_introspect._imports module."""

import pytest

from scitex_introspect import get_dependencies, get_imports


class TestGetImports:
    """Tests for get_imports function."""

    def test_get_imports_returns_success_true(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module)
        # Assert
        assert result["success"] is True

    def test_get_imports_includes_imports_key(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module)
        # Assert
        assert "imports" in result

    def test_get_imports_reports_nonzero_import_count(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module)
        # Assert
        assert result["import_count"] > 0

    def test_get_imports_categorize_true_reports_success(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=True)
        # Assert
        assert result["success"] is True

    def test_get_imports_categorize_true_includes_categories_key(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=True)
        # Assert
        assert "categories" in result

    def test_get_imports_categorize_true_includes_stdlib_bucket(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=True)
        # Assert
        assert "stdlib" in result["categories"]

    def test_get_imports_categorize_true_includes_third_party_bucket(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=True)
        # Assert
        assert "third_party" in result["categories"]

    def test_get_imports_categorize_true_includes_local_bucket(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=True)
        # Assert
        assert "local" in result["categories"]

    def test_get_imports_categorize_false_reports_success(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=False)
        # Assert
        assert result["success"] is True

    def test_get_imports_categorize_false_omits_categories_key(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=False)
        # Assert
        assert "categories" not in result

    def test_get_imports_categorize_false_includes_imports_key(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module, categorize=False)
        # Assert
        assert "imports" in result

    def test_get_imports_includes_from_style_imports(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_imports(target_module)
        # Assert
        assert len([i for i in result["imports"] if i["type"] == "from"]) > 0

    def test_get_imports_non_module_reports_success_false(self):
        # Arrange
        non_module_target = "json.dumps"
        # Act
        result = get_imports(non_module_target)
        # Assert
        assert result["success"] is False

    def test_get_imports_non_module_error_mentions_not_a_module(self):
        # Arrange
        non_module_target = "json.dumps"
        # Act
        result = get_imports(non_module_target)
        # Assert
        assert "not a module" in result["error"]


class TestGetDependencies:
    """Tests for get_dependencies function."""

    def test_get_dependencies_returns_success_true(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_dependencies(target_module)
        # Assert
        assert result["success"] is True

    def test_get_dependencies_includes_dependencies_key(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_dependencies(target_module)
        # Assert
        assert "dependencies" in result

    def test_get_dependencies_reports_nonnegative_dependency_count(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_dependencies(target_module)
        # Assert
        assert result["dependency_count"] >= 0

    def test_get_dependencies_non_recursive_reports_success(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_dependencies(target_module, recursive=False)
        # Assert
        assert result["success"] is True

    def test_get_dependencies_non_recursive_omits_tree_key(self):
        # Arrange
        target_module = "scitex_introspect._resolve"
        # Act
        result = get_dependencies(target_module, recursive=False)
        # Assert
        assert "tree" not in result

    @pytest.mark.skipif(
        True, reason="Recursive deps can timeout due to stdlib scanning"
    )
    def test_get_dependencies_recursive_returns_dependencies_or_tree(self):
        # Arrange
        target_module = "json"
        # Act
        result = get_dependencies(target_module, recursive=True, max_depth=1)
        # Assert
        assert "dependencies" in result or "tree" in result
