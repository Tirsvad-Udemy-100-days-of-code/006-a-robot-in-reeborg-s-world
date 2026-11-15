# Getting Started

🌐 **English** · [Dansk](Getting-Started-da) · [Bahasa Melayu](Getting-Started-ms)

## Requirements

Python 3.13 or newer. The project has no runtime dependencies; `pytest`, `ruff` and `mypy` are installed as development dependencies.

## Install

Create a virtual environment and install the project in editable mode (Windows PowerShell first, then Linux and macOS):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run in Reeborg's world

Open the maze in [Reeborg's world](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json), choose Python mode, paste the contents of `src/reeborg_maze/presentation/reeborg_script.py` into the editor and press run.

## Run offline

The offline run reads a world file and prints the final world and the result. With `--animate` the robot moves in the terminal; with `--start X Y HEADING` you choose the start (heading 0 is east, 1 north, 2 west, 3 south):

```bash
python -m reeborg_maze tests/worlds/problem_world.json
python -m reeborg_maze tests/worlds/problem_world.json --animate
python -m reeborg_maze tests/worlds/problem_world.json --animate --delay 0.05 --start 1 1 0
```

## Run the tests

```bash
python -m pytest -v
```

Every free cell of the three test worlds is tried with all four headings, for both the tested function and the pasteable script.
