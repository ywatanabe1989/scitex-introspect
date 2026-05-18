"""Smoke test: every example script under examples/ runs to completion."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = list(Path(__file__).parent.parent.joinpath("examples").glob("*.py"))


def test_examples_directory_contains_scripts():
    # Arrange
    discovered = EXAMPLES
    # Act
    count = len(discovered)
    # Assert
    assert count > 0, "No example scripts found under examples/"


@pytest.mark.parametrize("example_path", EXAMPLES, ids=lambda p: p.name)
def test_example_script_runs_to_completion(tmp_path, example_path):
    # Arrange
    cmd = [sys.executable, str(example_path)]
    # Act
    completed = subprocess.run(
        cmd,
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=60,
    )
    # Assert
    assert completed.returncode == 0, (
        f"{example_path.name} failed:\n"
        f"STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
    )
