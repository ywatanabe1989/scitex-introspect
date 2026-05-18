#!/usr/bin/env python3
# Timestamp: 2025-01-20
# File: tests/scitex/introspect/test__signature.py

"""Tests for scitex_introspect._signature module."""

from scitex_introspect import q


class TestQ:
    """Tests for q function."""

    def test_q_returns_success_true_for_function(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target)
        # Assert
        assert result["success"] is True

    def test_q_returns_correct_name_for_function(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target)
        # Assert
        assert result["name"] == "dumps"

    def test_q_includes_signature_key_for_function(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target)
        # Assert
        assert "signature" in result

    def test_q_includes_parameters_key_for_function(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target)
        # Assert
        assert "parameters" in result

    def test_q_with_annotations_reports_success(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target, include_annotations=True)
        # Assert
        assert result["success"] is True

    def test_q_with_annotations_includes_parameters_key(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target, include_annotations=True)
        # Assert
        assert "parameters" in result

    def test_q_without_defaults_reports_success(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target, include_defaults=False)
        # Assert
        assert result["success"] is True

    def test_q_without_defaults_drops_default_field(self):
        # Arrange
        target = "json.dumps"
        # Act
        result = q(target, include_defaults=False)
        # Assert
        assert all("default" not in param for param in result["parameters"])

    def test_q_class_reports_success_true(self):
        # Arrange
        class_target = "pathlib.Path"
        # Act
        result = q(class_target)
        # Assert
        assert result["success"] is True

    def test_q_class_type_info_reports_class_kind(self):
        # Arrange
        class_target = "pathlib.Path"
        # Act
        result = q(class_target)
        # Assert
        assert result["type_info"]["kind"] == "class"

    def test_q_invalid_path_reports_success_false(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = q(invalid_target)
        # Assert
        assert result["success"] is False

    def test_q_invalid_path_includes_error_key(self):
        # Arrange
        invalid_target = "nonexistent.module"
        # Act
        result = q(invalid_target)
        # Assert
        assert "error" in result

    def test_q_builtin_returns_envelope_with_success_key(self):
        # Arrange
        builtin_target = "len"
        # Act
        result = q(builtin_target)
        # Assert
        assert "success" in result
