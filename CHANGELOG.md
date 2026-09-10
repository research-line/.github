# Changelog

All notable changes to the `research-line/.github` repository will be documented in this file.

## [1.0.7] - 2026-09-10

### Changed
- Refreshed start page verification timestamps across all index surfaces (`profile/README.md`, `profile/README_de.md`, `README.md`, `llms.txt`, and `tests/test_profile_parity.py`) to `2026-09-10` (`10. September 2026`).
- Synchronized live public activity snapshot with latest GitHub pushes from live API (`functional-stability-theory` 2026-09-10, `abc-hct` 2026-09-10, `rh-even-dominance` 2026-09-02, `.github` 2026-09-10, `fst-nash` 2026-08-20, `crm-cosmology` 2026-08-09, `ai-elite-swr` 2026-08-05).
- Integrated `locuterra` (civic tech / location-based digital commons demonstrator) into related Um:bruch research directory in `profile/README.md`, `profile/README_de.md`, and `llms.txt`.
- Enhanced external discoverability for `research-line/abc-hct` on GitHub by setting its official Zenodo DOI homepage (`https://doi.org/10.5281/zenodo.21916900`) and adding targeted repository topics (`open-science`, `reproducible-research`, `zenodo`).

### Verified
- Live GitHub API inventory confirmed: 11 repositories total across `research-line` — 8 public (7 active, `rfep-framework` archived) and 3 private repositories.
- Strict zero-leak invariant maintained: zero private repositories exposed in public documentation or indices.
- All automated contract tests (`tests/test_profile_parity.py`) pass 100% (9/9).
- Mermaid diagram syntax verified (0 errors across all markdown files via `lint_mermaid.py`).

## [1.0.6] - 2026-08-24

### Fixed
- Corrected two push dates that were off by one day. `rh-even-dominance` and
  `functional-stability-theory` were listed as `2026-08-23`; the API reports
  `2026-08-22T23:51:52Z` and `2026-08-22T22:19:58Z`. Both fall on the 23rd once
  converted to CEST, so the previous pass recorded local time while the index
  claims the figures are "verified via GitHub API" - which serves UTC. Anyone
  re-checking would have seen the 22nd and concluded the index was wrong.
- Every snapshot heading in `README.md`, `profile/README.md`,
  `profile/README_de.md` and `llms.txt` now states that the dates are the UTC day
  of `pushed_at`, so the next pass does not repeat the conversion.

### Changed
- Verification timestamp advanced to `2026-08-24` across all four index surfaces.

### Verified
- Live read-only API on 2026-08-24: 11 repositories total - 8 public (7 active,
  `rfep-framework` archived) and 3 private. The public count of 8 and the
  active/archived split in the index match that readback.
- No private repository name appears in any public surface. Checked explicitly
  for all three.
- All 8 public repositories are named in `README.md`, both profile READMEs and
  `llms.txt`; `abc-hct` included with a valid link.
- Remaining, deliberately untouched: the snapshot tables are not strictly sorted
  by date - `.github` (2026-08-23) sits between entries dated 2026-08-20 and
  2026-08-09. That predates this pass, and reordering someone else's document
  without a mandate risks more than it fixes.
- No commit, push or GitHub write took place. The task's Definition of Done
  requires the local diff to remain reviewable until separate approval.

## [1.0.5] - 2026-08-23

### Changed
- Synchronized live public activity snapshot with latest GitHub pushes (`rh-even-dominance` 2026-08-23, `functional-stability-theory` 2026-08-23, `abc-hct` 2026-08-21, `fst-nash` 2026-08-20, `.github` 2026-08-23).
- Refreshed verification timestamps to `2026-08-23` across `profile/README.md`, `profile/README_de.md`, `README.md`, and `llms.txt`.
- Enhanced `SECURITY.md` with comprehensive bilingual security policy, open science invariants, and direct security contacts (`security@open-bricks.org`, `security@ellmos.ai`, `support@lukasgeiger.com`, `lukas@open-bricks.org`).
- Re-verified complete 8 public repository inventory, strict privacy boundaries, and 1:1 bilingual parity.

## [1.0.4] - 2026-08-21

### Added
- Integrated public repository `abc-hct` (High-Characteristic-Torsion abc research papers, Manin symbol pairings over Hecke algebras, and deterministic rank certificates) into `profile/README.md`, `profile/README_de.md`, `README.md`, and `llms.txt`.
- Added `abc-hct` node to the Mermaid Open-Science architecture flowchart under `Research_Pillars`.
- Added automated contract test suite `tests/test_profile_parity.py` to enforce bilingual parity, encoding validity, public repository inventory, strict privacy boundaries, and timestamp synchronization.

### Changed
- Refreshed verification timestamps across all profile files to `2026-08-21`.
- Synchronized live public activity snapshot with latest GitHub pushes (`abc-hct` 2026-08-21, `functional-stability-theory` 2026-08-21, `rh-even-dominance` 2026-08-21, `fst-nash` 2026-08-20, `.github` 2026-08-21).
- Updated public repository count badge and inventory from 7 to 8 public repositories.
- Updated discovery phrases and search terms in `profile/README.md`, `profile/README_de.md`, and `llms.txt`.

## [1.0.3] - 2026-08-14

### Changed
- Refreshed verification timestamps to `2026-08-14` across `profile/README.md`, `profile/README_de.md`, `README.md`, and `llms.txt`.
- Synchronized the live activity snapshot table with recent GitHub pushes (`fst-nash` 2026-08-13, `functional-stability-theory` 2026-08-13, `crm-cosmology` 2026-08-09, `rh-even-dominance` 2026-08-05, `ai-elite-swr` 2026-08-05, `.github` 2026-08-14).
- Updated sister organization descriptions in `profile/README.md` and `profile/README_de.md` to reflect current flagship tools across `dev-bricks`, `entertain-and-more`, and `open-bricks`.
- Synchronized `llms.txt` AI discovery search phrases, related repositories, and interpretation guidance.
- Verified 1:1 bilingual parity, genuine UTF-8 German umlauts, and markdown link integrity.

### Added
- Added standard `CHANGELOG.md` to track organization profile releases and audit history.

## [1.0.2] - 2026-08-06

### Changed
- Refreshed verification timestamps across profile documents to `2026-08-06`.
- Re-verified the public repository directory (7 public repositories: `.github`, `ai-elite-swr`, `crm-cosmology`, `fst-nash`, `functional-stability-theory`, `rfep-framework`, `rh-even-dominance`).
- Verified strict privacy boundary excluding all draft/internal repositories from public documentation.

## [1.0.1] - 2026-07-29

### Added
- Added German organization profile landing page `profile/README_de.md` with bilingual language switchers.
- Added interactive Mermaid architecture flowchart detailing Open Science Pillars, reproducibility outputs, and sister networks.
- Added modern Shields.io badges for GitHub Org, open-bricks ecosystem, Open Science domain, Zenodo DOIs, llms.txt, and CC-BY 4.0 / MIT license.
- Added machine-readable `llms.txt` for AI agent context and crawler discovery.
