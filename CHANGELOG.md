# Changelog

All notable changes to `scitex-introspect` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

- docs(refresh): refresh _sphinx_html/ from CI build.

## [0.1.7] — 2026-05-09

- fix(workflows): resync integrated release pipeline from scitex-dev v0.11.20.
- ci(codecov): disable PR comments (comment: false) to stop email noise.

## [0.1.6] — 2026-05-03

- fix(workflows): standardize to scitex-dev canonical workflow set.
- ci(quality): replace broken ecosystem-clone template with single-package
  audit-all via `scitex-dev ecosystem audit-all`.

## [0.1.5] — 2026-04-11

- **API**: canonical `__version__` + `from __future__ import annotations` +
  dangling `__all__` cleanup.
- **Audit**: clear all audit warnings (PA501, PA201, PA203, PS139, etc.).
- **Docs**: README Architecture + Demo sections, CHANGELOG, CONTRIBUTING,
  sphinx/RTD scaffolding, skills leaves (01–03), mandatory badges layout.
- **CI**: full test/docs/release pipeline — tests.yml, docs.yml,
  publish-pypi.yml, sync-main.yml, weekly doc-quality workflow.
- **Tests**: subprocess coverage wiring, audit-all integration,
  cross-package imports integration test.
- **Deps**: drop umbrella `scitex` from runtime dependencies; pin
  `scitex-dev>=0.11.7` for audit tooling.

## [0.1.4]

- Initial CHANGELOG entry — see git log for prior history.
