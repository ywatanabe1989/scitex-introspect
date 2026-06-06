#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""THIS_FILE — helper that resolves the caller's source path.

Ported from scitex-gen ``misc.py``. The original code hard-coded the
absolute path of ``misc.py`` itself; this exposes it as a callable
helper that returns the *caller's* file path, which is what most users
of the constant actually need.

Two forms are provided:

- :func:`this_file` — the function form; returns the caller's ``__file__``.
- ``THIS_FILE`` — a module-level constant resolved to the file path of
  this submodule (preserved for parity with the legacy import).
"""
from __future__ import annotations

import sys


def this_file() -> str:
    """Return the absolute path of the file that called this function.

    Uses ``sys._getframe`` to look one frame up. Falls back to an empty
    string if the caller has no ``__file__`` (e.g. interactive shell).

    Example
    -------
    >>> # Inside myscript.py:
    >>> # path = this_file()
    """
    frame = sys._getframe(1)
    return frame.f_globals.get("__file__", "")


# Module-level constant, preserved for backward compatibility with the
# legacy ``from scitex.gen.misc import THIS_FILE`` import path. New code
# should call :func:`this_file` from the caller's scope instead.
THIS_FILE: str = __file__
