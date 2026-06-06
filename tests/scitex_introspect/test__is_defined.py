#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for is_defined_global / is_defined_local — caller-frame lookups."""
from __future__ import annotations

from scitex_introspect import is_defined_global, is_defined_local


# Module-level binding used by test_global_defined.
_module_level_thing = 42


class TestIsDefinedGlobal:
    def test_finds_module_level_name(self):
        assert is_defined_global("_module_level_thing") is True

    def test_missing_name(self):
        assert is_defined_global("totally_not_defined_xyz") is False


class TestIsDefinedLocal:
    def test_finds_local_binding(self):
        a = 5  # noqa: F841
        assert is_defined_local("a") is True

    def test_local_missing(self):
        assert is_defined_local("definitely_no_such_local") is False

    def test_local_does_not_see_global(self):
        # The module-level binding above is NOT in this function's locals.
        assert is_defined_local("_module_level_thing") is False
