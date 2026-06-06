#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for scitex_introspect.is_later_or_equal."""
from __future__ import annotations

import pytest

from scitex_introspect import is_later_or_equal


class TestIsLaterOrEqual:
    def test_module_object_install_passes_floor(self):
        import numpy as np
        assert is_later_or_equal(np, "0.0.1") is True

    def test_module_object_below_ceiling(self):
        import numpy as np
        assert is_later_or_equal(np, "999.0.0") is False

    def test_string_package_name(self):
        assert is_later_or_equal("numpy", "0.0.1") is True

    def test_equal_returns_true(self):
        import numpy as np
        assert is_later_or_equal(np, np.__version__) is True

    def test_missing_package(self):
        try:
            from importlib.metadata import PackageNotFoundError
        except ImportError:  # pragma: no cover
            pytest.skip("importlib.metadata not available")
        with pytest.raises(PackageNotFoundError):
            is_later_or_equal("definitely-not-a-real-package-x", "1.0.0")

    def test_format_kwarg_is_accepted_but_ignored(self):
        import numpy as np
        assert is_later_or_equal(np, "0.0.1", format="X.Y.Z") is True
