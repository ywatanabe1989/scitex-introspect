#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__class_hierarchy.py

"""Tests for scitex_introspect._class_hierarchy module."""

from scitex_introspect import get_class_hierarchy, get_mro


class TestGetClassHierarchy:
    """Tests for get_class_hierarchy function."""

    def test_get_hierarchy_returns_success_true(self):
        # Arrange
        target = "collections.abc.Mapping"
        # Act
        result = get_class_hierarchy(target)
        # Assert
        assert result["success"] is True

    def test_get_hierarchy_includes_mro_key(self):
        # Arrange
        target = "collections.abc.Mapping"
        # Act
        result = get_class_hierarchy(target)
        # Assert
        assert "mro" in result

    def test_get_hierarchy_includes_subclasses_key(self):
        # Arrange
        target = "collections.abc.Mapping"
        # Act
        result = get_class_hierarchy(target)
        # Assert
        assert "subclasses" in result

    def test_get_hierarchy_reports_nonzero_mro_count(self):
        # Arrange
        target = "collections.abc.Mapping"
        # Act
        result = get_class_hierarchy(target)
        # Assert
        assert result["mro_count"] > 0

    def test_hierarchy_mro_includes_self_class_name(self):
        # Arrange
        target = "collections.abc.MutableMapping"
        # Act
        result = get_class_hierarchy(target)
        # Assert
        assert "MutableMapping" in [c["name"] for c in result["mro"]]

    def test_hierarchy_mro_includes_parent_class_name(self):
        # Arrange
        target = "collections.abc.MutableMapping"
        # Act
        result = get_class_hierarchy(target)
        # Assert
        assert "Mapping" in [c["name"] for c in result["mro"]]

    def test_hierarchy_excludes_object_when_builtins_false(self):
        # Arrange
        target = "pathlib.Path"
        # Act
        result = get_class_hierarchy(target, include_builtins=False)
        # Assert
        assert "object" not in [c["name"] for c in result["mro"]]

    def test_hierarchy_includes_object_when_builtins_true(self):
        # Arrange
        target = "pathlib.Path"
        # Act
        result = get_class_hierarchy(target, include_builtins=True)
        # Assert
        assert "object" in [c["name"] for c in result["mro"]]

    def test_hierarchy_non_class_reports_success_false(self):
        # Arrange
        non_class_target = "json.dumps"
        # Act
        result = get_class_hierarchy(non_class_target)
        # Assert
        assert result["success"] is False

    def test_hierarchy_non_class_error_mentions_not_a_class(self):
        # Arrange
        non_class_target = "json.dumps"
        # Act
        result = get_class_hierarchy(non_class_target)
        # Assert
        assert "not a class" in result["error"]

    def test_hierarchy_max_depth_one_truncates_subclass_tree(self):
        # Arrange
        target = "collections.abc.Mapping"
        # Act
        result = get_class_hierarchy(target, max_depth=1)
        # Assert
        assert all(
            "subclasses" not in sub or len(sub["subclasses"]) == 0
            for sub in result.get("subclasses", [])
        )


class TestGetMro:
    """Tests for get_mro function."""

    def test_get_mro_returns_success_true(self):
        # Arrange
        target = "collections.OrderedDict"
        # Act
        result = get_mro(target)
        # Assert
        assert result["success"] is True

    def test_get_mro_includes_mro_key(self):
        # Arrange
        target = "collections.OrderedDict"
        # Act
        result = get_mro(target)
        # Assert
        assert "mro" in result

    def test_get_mro_returns_nonempty_mro_list(self):
        # Arrange
        target = "collections.OrderedDict"
        # Act
        result = get_mro(target)
        # Assert
        assert len(result["mro"]) > 0

    def test_get_mro_returns_qualified_names_with_dots(self):
        # Arrange
        target = "pathlib.Path"
        # Act
        result = get_mro(target)
        # Assert
        assert all("." in name for name in result["mro"])
