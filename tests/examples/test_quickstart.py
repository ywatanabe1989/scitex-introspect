#!/usr/bin/env python3
"""Compile-only smoke test for examples/quickstart.py."""

import py_compile
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_example_file_exists_on_disk():
    # Arrange
    target = EXAMPLE
    # Act
    exists = target.is_file()
    # Assert
    assert exists, f"missing example: {target}"


def test_quickstart_example_compiles_without_syntax_error():
    # Arrange
    target = EXAMPLE
    # Act
    py_compile.compile(str(target), doraise=True)
    # Assert
    # py_compile.compile raises PyCompileError on failure; reaching here = OK.
    assert True


# EOF
