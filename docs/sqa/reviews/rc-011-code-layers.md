# Review: Python code with the layers

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [PY], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version; reviewed in the review itself, autonomous, not independent | [f9581e1] |

---

## Artifact Under Review

- Instance reviewed: [PY]
- Checklist used: [QC-PY-001]
- Scope: full review (re-review after RC-010)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Names follow PEP 8 (`ruff` rules N pass). |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; short names only in tiny scopes. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check` pass on `src` and `tests`; the only suppressions are `# nosemgrep` on the animation delay, explained in the line above, and the per-file rules for the pasteable script, explained in `pyproject.toml`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `ruff` rule ANN and `mypy --strict` (21 files) pass; every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; no swallowed exception. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | `Path.read_text` closes the file itself. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `print` in `presentation/cli.py` and `visualizer.py` is the command line's own output; nothing is logged and no secret or personal data is printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; ADR-0001 skips it. The layers trace to UC-001 and DM-001. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 640 tests: unit (fake robot), integration (every free cell and heading of three worlds, simulator rules), e2e (command line and the script run against the simulator for every start); none depends on order or network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes; the only `Any` is `WorldData`, justified in a comment. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; dev dependencies are declared with bounded ranges. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The wall-following rule is in `domain/wall_following.py`; its second copy in the pasteable script is required by Reeborg's world and is proved equal by `tests/e2e/test_reeborg_script.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports nothing from the other layers, `application` imports only `domain`, `infrastructure` imports `application` and `domain`, and only `presentation/cli.py` (the composition root) names `infrastructure`; checked with grep, no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Single-purpose modules; narrow Protocols (`Robot`, `WorldView`, `RobotWorldGateway`); the use case depends on the port, not on the simulator. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/reeborg_maze`; `unit`, `integration`, `e2e` under `tests/`; snake_case names. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File names are English, lower-case, no spaces. |

## Overall Verdict

Go — every Mandatory criterion passes; criterion 10 is not applicable. Re-review of the findings of RC-010, a full review of `src/` and `tests/` at commit 47d5796. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[PY]: ../../../src
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[f9581e1]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/commit/f9581e128ebea2e751df0bb20267a94301763f4b
