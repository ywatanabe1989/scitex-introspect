#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__examples.py

"""Tests for scitex_introspect._examples module."""

from scitex_introspect import find_examples


class TestFindExamples:
    """Tests for find_examples function."""

    def test_find_examples_returns_success_true(self):
        # Arrange
        target = "scitex_introspect.q"
        # Act
        result = find_examples(target)
        # Assert
        assert result["success"] is True

    def test_find_examples_includes_examples_key(self):
        # Arrange
        target = "scitex_introspect.q"
        # Act
        result = find_examples(target)
        # Assert
        assert "examples" in result

    def test_find_examples_includes_count_key(self):
        # Arrange
        target = "scitex_introspect.q"
        # Act
        result = find_examples(target)
        # Assert
        assert "count" in result

    def test_find_examples_accepts_search_paths_argument(self):
        # Arrange
        target = "scitex_introspect.q"
        search_paths = ["tests/scitex/introspect"]
        # Act
        result = find_examples(target, search_paths=search_paths)
        # Assert
        assert result["success"] is True

    def test_find_examples_max_results_reports_success(self):
        # Arrange
        target = "scitex_introspect.q"
        # Act
        result = find_examples(target, max_results=2)
        # Assert
        assert result["success"] is True

    def test_find_examples_max_results_caps_returned_count(self):
        # Arrange
        target = "scitex_introspect.q"
        max_results = 2
        # Act
        result = find_examples(target, max_results=max_results)
        # Assert
        assert len(result["examples"]) <= max_results

    def test_find_examples_each_entry_has_file_field(self):
        # Arrange
        target = "scitex_introspect.q"
        # Act
        result = find_examples(target)
        # Assert
        assert all("file" in ex for ex in result["examples"])

    def test_find_examples_each_entry_has_line_field(self):
        # Arrange
        target = "scitex_introspect.q"
        # Act
        result = find_examples(target)
        # Assert
        assert all("line" in ex for ex in result["examples"])

    def test_find_examples_each_entry_has_context_field(self):
        # Arrange
        target = "scitex_introspect.q"
        # Act
        result = find_examples(target)
        # Assert
        assert all("context" in ex for ex in result["examples"])

    def test_find_examples_unknown_target_returns_dict_envelope(self):
        # Arrange
        unknown_target = "nonexistent_function_xyz123"
        # Act
        result = find_examples(unknown_target)
        # Assert
        assert isinstance(result, dict) and "success" in result
