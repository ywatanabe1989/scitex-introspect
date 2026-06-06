#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Timestamp: "2025-06-13 22:44:28 (ywatanabe)"
# File: ./src/scitex_introspect/_src.py
"""``src(obj)`` — page an object's source code through ``less``.

Ported from scitex_gen._fs._src (Phase B retirement wave).
Note: this is the legacy ``less``-piping variant. For programmatic
access to source, prefer :func:`scitex_introspect.qq`.
"""

import inspect
import subprocess


def src(obj):
    """
    Returns the source code of a given object using `less`.
    Handles functions, classes, class instances, methods, and built-in functions.
    """
    # If obj is an instance of a class, get the class of the instance.
    if (
        not inspect.isclass(obj)
        and not inspect.isfunction(obj)
        and not inspect.ismethod(obj)
    ):
        obj = obj.__class__

    try:
        # Attempt to retrieve the source code
        source_code = inspect.getsource(obj)

        # Open a subprocess to use `less` for displaying the source code
        process = subprocess.Popen(
            ["less"], stdin=subprocess.PIPE, encoding="utf8"
        )
        process.communicate(input=source_code)
        if process.returncode != 0:
            print(f"Process exited with return code {process.returncode}")
    except OSError as e:
        # Handle cases where the source code cannot be retrieved (e.g., built-in functions)
        print(f"Cannot retrieve source code: {e}")
    except TypeError as e:
        # Handle cases where the object type is not supported
        print(f"TypeError: {e}")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: {e}")


# EOF
