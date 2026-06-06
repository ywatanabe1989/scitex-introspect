#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""is_defined_global / is_defined_local — caller-frame name-lookup helpers.

Ported from scitex-gen ``misc.py``. The original implementations checked
``globals()`` / ``locals()`` of the *callee*, which was always wrong
because those namespaces belong to ``misc.py`` itself, not to the caller.
This rewrite uses ``sys._getframe`` to inspect the *caller's* namespace,
which is what the docstring example claimed to do.
"""
from __future__ import annotations

import sys


def is_defined_global(x_str):
    """Return True if ``x_str`` is a defined name in the caller's global scope.

    Parameters
    ----------
    x_str : str
        The name to look up in the caller's ``globals()``.

    Returns
    -------
    bool
        True if defined, False otherwise.

    Example
    -------
    >>> is_defined_global("os")  # we don't import os in this test scope
    False
    >>> import os
    >>> is_defined_global("os")
    True
    """
    caller_globals = sys._getframe(1).f_globals
    return x_str in caller_globals


def is_defined_local(x_str):
    """Return True if ``x_str`` is a defined name in the caller's local scope.

    Parameters
    ----------
    x_str : str
        The name to look up in the caller's ``locals()``.

    Returns
    -------
    bool
        True if defined, False otherwise.

    Example
    -------
    >>> def demo():
    ...     a = 5
    ...     return is_defined_local("a")
    >>> demo()
    True
    """
    caller_locals = sys._getframe(1).f_locals
    return x_str in caller_locals
