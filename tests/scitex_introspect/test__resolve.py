#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__resolve.py

"""Tests for scitex_introspect._resolve module."""

import json
from collections.abc import Mapping
from pathlib import Path

from scitex_introspect import get_type_info, resolve_object


class TestResolveObject:
    """Tests for resolve_object function."""

    def test_resolve_module_returns_no_error(self):
        # Arrange
        path = "json"
        # Act
        _, error = resolve_object(path)
        # Assert
        assert error is None

    def test_resolve_module_returns_module_object(self):
        # Arrange
        path = "json"
        # Act
        obj, _ = resolve_object(path)
        # Assert
        assert obj is json

    def test_resolve_function_returns_no_error(self):
        # Arrange
        path = "json.dumps"
        # Act
        _, error = resolve_object(path)
        # Assert
        assert error is None

    def test_resolve_function_returns_function_object(self):
        # Arrange
        path = "json.dumps"
        # Act
        obj, _ = resolve_object(path)
        # Assert
        assert obj is json.dumps

    def test_resolve_class_returns_no_error(self):
        # Arrange
        path = "pathlib.Path"
        # Act
        _, error = resolve_object(path)
        # Assert
        assert error is None

    def test_resolve_class_returns_class_object(self):
        # Arrange
        path = "pathlib.Path"
        # Act
        obj, _ = resolve_object(path)
        # Assert
        assert obj is Path

    def test_resolve_nested_path_returns_no_error(self):
        # Arrange
        path = "collections.abc.Mapping"
        # Act
        _, error = resolve_object(path)
        # Assert
        assert error is None

    def test_resolve_nested_path_returns_target_object(self):
        # Arrange
        path = "collections.abc.Mapping"
        # Act
        obj, _ = resolve_object(path)
        # Assert
        assert obj is Mapping

    def test_resolve_invalid_path_returns_none_object(self):
        # Arrange
        path = "nonexistent.module.thing"
        # Act
        obj, _ = resolve_object(path)
        # Assert
        assert obj is None

    def test_resolve_invalid_path_returns_non_none_error(self):
        # Arrange
        path = "nonexistent.module.thing"
        # Act
        _, error = resolve_object(path)
        # Assert
        assert error is not None

    def test_resolve_invalid_path_error_mentions_could_not_resolve(self):
        # Arrange
        path = "nonexistent.module.thing"
        # Act
        _, error = resolve_object(path)
        # Assert
        assert "Could not resolve" in error


class TestGetTypeInfo:
    """Tests for get_type_info function."""

    def test_type_info_module_reports_module_kind(self):
        # Arrange
        target = json
        # Act
        info = get_type_info(target)
        # Assert
        assert info["kind"] == "module"

    def test_type_info_function_reports_function_kind(self):
        # Arrange
        target = json.dumps
        # Act
        info = get_type_info(target)
        # Assert
        assert info["kind"] == "function"

    def test_type_info_class_reports_class_kind(self):
        # Arrange
        target = Path
        # Act
        info = get_type_info(target)
        # Assert
        assert info["kind"] == "class"

    def test_type_info_list_value_reports_data_kind(self):
        # Arrange
        target = [1, 2, 3]
        # Act
        info = get_type_info(target)
        # Assert
        assert info["kind"] == "data"
