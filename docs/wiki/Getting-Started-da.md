# Kom i gang

🌐 [English](Getting-Started) · **Dansk** · [Bahasa Melayu](Getting-Started-ms)

## Krav

Python 3.13 eller nyere. Projektet har ingen afhængigheder ved kørsel; `pytest`, `ruff` og `mypy` installeres som udviklingsafhængigheder.

## Installation

Opret et virtuelt miljø og installér projektet i redigerbar tilstand (først Windows PowerShell, derefter Linux og macOS):

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

## Kør i Reeborgs verden

Åbn labyrinten i [Reeborgs verden](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json), vælg Python-tilstand, indsæt indholdet af `src/reeborg_maze/presentation/reeborg_script.py` i editoren og tryk på kør.

## Kør uden forbindelse

Kørslen uden forbindelse læser en verdensfil og udskriver den endelige verden og resultatet. Med `--animate` bevæger robotten sig i terminalen; med `--start X Y HEADING` vælger du starten (retning 0 er øst, 1 nord, 2 vest, 3 syd):

```bash
python -m reeborg_maze tests/worlds/problem_world.json
python -m reeborg_maze tests/worlds/problem_world.json --animate
python -m reeborg_maze tests/worlds/problem_world.json --animate --delay 0.05 --start 1 1 0
```

## Kør testene

```bash
python -m pytest -v
```

Hver ledig celle i de tre testverdener prøves med alle fire retninger, både for den testede funktion og for scriptet, der kan indsættes.
