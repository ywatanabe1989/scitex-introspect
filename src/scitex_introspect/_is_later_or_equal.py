#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""is_later_or_equal — version-comparison helper.

Ported from scitex-gen ``misc.py``. The original used a broken
``scitex.gen.search`` reference that no longer exists; this rewrite is
based on ``packaging.version.parse`` and supports the same call shape
plus a few extras.

The legacy signature was::

    is_later_or_equal(package, tgt_version, format="MAJOR.MINOR.PATCH")

where ``package`` could be a module *object* or the *string* name. We
preserve both calling conventions; the ``format`` argument is accepted
but ignored (the parser handles MAJOR/MINOR/PATCH/pre/post natively).
"""
from __future__ import annotations

from types import ModuleType
from typing import Union

try:  # python >=3.8 stdlib metadata
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version as _pkg_version
except ImportError:  # pragma: no cover
    PackageNotFoundError = Exception  # type: ignore[assignment,misc]
    _pkg_version = None  # type: ignore[assignment]


def _resolve_version(package: Union[str, ModuleType]) -> str:
    """Return the installed ``__version__`` string for ``package``.

    Accepts either a module object (uses ``module.__version__``) or a
    string (uses ``importlib.metadata.version``).
    """
    if isinstance(package, ModuleType):
        version = getattr(package, "__version__", None)
        if version is None:
            raise AttributeError(
                f"module {package.__name__!r} has no __version__ attribute"
            )
        return str(version)

    if isinstance(package, str):
        if _pkg_version is None:  # pragma: no cover
            raise RuntimeError("importlib.metadata is unavailable")
        try:
            return _pkg_version(package)
        except PackageNotFoundError as exc:
            raise PackageNotFoundError(
                f"package {package!r} is not installed"
            ) from exc

    raise TypeError(
        f"package must be a module or str, got {type(package).__name__}"
    )


def is_later_or_equal(package, tgt_version, format="MAJOR.MINOR.PATCH"):
    """Return ``True`` if ``package``'s installed version >= ``tgt_version``.

    Parameters
    ----------
    package : module or str
        Either an imported module (e.g. ``numpy``) or the distribution
        name as a string (e.g. ``"numpy"``).
    tgt_version : str
        Target version string. Anything accepted by
        :func:`packaging.version.parse` works.
    format : str, optional
        Accepted for backward compatibility; ignored. The parser handles
        MAJOR.MINOR.PATCH, pre-release, post-release, etc., natively.

    Returns
    -------
    bool
        ``True`` if installed >= target, ``False`` otherwise.

    Example
    -------
    >>> import numpy as np
    >>> is_later_or_equal(np, "1.0.0")
    True
    >>> is_later_or_equal("numpy", "999.0.0")
    False
    """
    del format  # accepted but unused — parser is format-agnostic
    from packaging.version import parse as _parse

    installed = _resolve_version(package)
    return _parse(installed) >= _parse(str(tgt_version))
