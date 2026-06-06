# Changelog

All notable changes to `scitex-introspect` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0]

- feat: port `list_packages`, `main`, and `src` from `scitex-gen` (Phase B
  of the scitex-gen full retirement wave). `list_packages` now binds its
  inner `list_api` against this package's own `_list_api` (was an optional
  cross-package import upstream); `src` is the `less`-piping variant for
  interactive REPL use.
- `__import__("ipdb").set_trace()` stub removed from `main`.
- feat: port variable / version / file inspection helpers from
  `scitex-gen` `misc.py`:
  - `is_defined_global`, `is_defined_local` — caller-frame name lookups
    (the legacy impls checked the callee's namespace, which was
    always wrong; rewritten using `sys._getframe`).
  - `is_later_or_equal` — version comparison using
    `packaging.version.parse` (the legacy impl referenced a non-existent
    `scitex.gen.search` and was broken).
  - `this_file()` + `THIS_FILE` constant — resolve the caller's
    `__file__` (legacy version was a hard-coded absolute path).
- Add `packaging` to runtime dependencies (for `is_later_or_equal`).

## [0.1.4]

- Initial CHANGELOG entry — see git log for prior history.
