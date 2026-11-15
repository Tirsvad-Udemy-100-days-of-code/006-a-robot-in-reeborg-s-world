# Review: Python code before the layers

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [PY], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | S01 (Product Owner) | Initial version; reviewed in the review itself, autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: [PY]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (AI as stand-in for S02)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Names follow PEP 8: SimulatedRobot, solve_maze, HEADING_STEP. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; x, y, dx, dy, nx, ny only in tiny scopes. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Fail | `ruff format --check` would reformat 4 files; `ruff check` reports 12 errors (reeborg_script.py names are the script's own and need a per-file rule). |
| 4 | Every function and method signature is type-annotated, including `-> None` | Fail | `make_frame_printer` has no return type; `world: dict` and `load_world -> dict` lack type arguments (`mypy --strict`: 18 errors). |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; SimulationError is specific. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default arguments; no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | `Path.read_text` closes the file itself. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `print` is the command line's own output, shown to the learner; nothing is logged and no secret or personal data is printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; ADR-0001 skips it. The code traces to UC-001 and DM-001. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Fail | Only the solver is tested. The simulator's wall and action-limit rules, the visualiser and the command line have no test, and nothing checks that `reeborg_script.py` matches the solver. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Fail | `mypy --strict` reports 18 errors in 3 files (Optional criterion). |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No runtime dependencies; the dev dependency is declared. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The algorithm exists twice, in `maze_solver.py` and in the self-contained `reeborg_script.py`, because the script cannot import; the second copy is not yet tested against the first (see criterion 11). |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `maze_solver.py` imports nothing outside the standard library; there are no cycles. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | The solver depends on a narrow Protocol of five methods. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Fail | The package is flat (`constants`, `maze_solver`, `simulator`, `visualizer`); no `domain`, `application`, `infrastructure` or `presentation` packages, and tests are not split into `unit`, `integration`, `e2e`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File names are English, lower-case, no spaces. |

## Overall Verdict

No-Go — four Mandatory criteria fail (3, 4, 11, 17), which are blocking findings. The code returns to its owner; the findings are fixed under MIL-002 task 6 and the code is reviewed again. Subject: `src/` and `tests/` at commit e817207. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Format and lint the code with ruff and fix the findings (criterion 3) | S01 | 2026-11-17 |
| Annotate every signature and fix the strict mypy errors (criteria 4, 12) | S01 | 2026-11-17 |
| Add tests for the simulator, the visualiser, the command line and the script (criterion 11) | S01 | 2026-11-18 |
| Move the code into the four layers and the tests into unit, integration and e2e (criterion 17) | S01 | 2026-11-18 |

---

[PY]: ../../../src
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
