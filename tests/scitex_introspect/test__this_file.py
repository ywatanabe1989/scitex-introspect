#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for this_file() / THIS_FILE."""
from __future__ import annotations

from scitex_introspect import THIS_FILE, this_file


class TestThisFile:
    def test_function_returns_caller_file(self):
        # Called from this test file, this_file() should resolve to it.
        assert this_file().endswith("test__this_file.py")

    def test_module_constant_points_at_module(self):
        # THIS_FILE is the constant captured at scitex_introspect._this_file
        # import time, so it should end with _this_file.py.
        assert THIS_FILE.endswith("_this_file.py")
