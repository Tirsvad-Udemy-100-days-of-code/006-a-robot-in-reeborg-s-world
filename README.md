# 🚀 Reeborg Maze

A beginner-friendly Python project that guides a robot through a maze in Reeborg's world by following the right wall, whatever its random start position and direction.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

This is the final project of day 6 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*. The maze is fixed, but the robot starts at a random position and heading, so the program must work from anywhere.

The robot follows the right wall:

1. Walk forward until a wall is hit, then turn left (this puts a wall on the right and avoids infinite loops).
2. Until the goal is reached:
   - if the right side is clear: turn right and move,
   - else if the front is clear: move,
   - else: turn left.

The project contains:

- `src/reeborg_maze/presentation/reeborg_script.py` – the script to paste into [Reeborg's world](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json).
- `src/reeborg_maze/domain/` – the same algorithm as a testable function (`wall_following.py`) and the robot interface it needs.
- `src/reeborg_maze/application/` – the use case that solves a world file, and the ports it needs.
- `src/reeborg_maze/infrastructure/` – a small offline simulator that reads Reeborg world JSON files.
- `src/reeborg_maze/presentation/` – the command line, and the drawing that shows the world as text and animates the robot.
- `tests/` – unit, integration and end-to-end tests, and three test worlds with different start headings.

## 📋 Requirements

- Python 3.13 or newer
- No runtime dependencies (pytest is installed as a dev dependency for the tests)
- Optional: [Doxygen](https://www.doxygen.nl/) to build the API documentation

## 🛠️ Setup

Create and activate a local virtual environment, upgrade pip and install the project in editable mode.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

In Reeborg's world: open the maze link above, choose Python mode, paste the contents of `src/reeborg_maze/reeborg_script.py` into the editor and press run.

Offline, against a world file:

```bash
python -m reeborg_maze tests/worlds/problem_world.json
```

Watch the robot move in the terminal (optionally pick a start with `X Y HEADING`, where heading is 0=east, 1=north, 2=west, 3=south):

```bash
python -m reeborg_maze tests/worlds/problem_world.json --animate
python -m reeborg_maze tests/worlds/problem_world.json --animate --delay 0.05 --start 1 1 0
```

![Animated run of the robot solving the maze in the terminal](docs/demo.webp)

The robot is drawn as `>` `^` `<` `v`, the goal as `G` and mud as `~~~`.

Build the documentation (written to `docs/html`):

```bash
doxygen Doxyfile
```

## 🧪 Tests

The tests use [pytest](https://pytest.org); each world is solved from every free cell and all four headings.

```bash
python -m pytest -v
```

Check the style and the types with `ruff check src tests` and `mypy`.

## 📄 License

[GNU AGPL v3 or later](LICENSE)

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Governance][GOV-001] | The review workflow, who decides and how disputes escalate |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/006-a-robot-in-reeborg-s-world/issues
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[GOV-001]: ./docs/sqa/governance.md
