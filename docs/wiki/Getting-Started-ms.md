# Bermula

🌐 [English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Melayu**

## Keperluan

Python 3.13 atau lebih baharu. Projek ini tiada kebergantungan semasa larian; `pytest`, `ruff` dan `mypy` dipasang sebagai kebergantungan pembangunan.

## Pemasangan

Cipta persekitaran maya dan pasang projek dalam mod boleh disunting (Windows PowerShell dahulu, kemudian Linux dan macOS):

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

## Jalankan di dunia Reeborg

Buka labirin di [dunia Reeborg](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json), pilih mod Python, tampal kandungan `src/reeborg_maze/presentation/reeborg_script.py` ke dalam editor dan tekan jalankan.

## Jalankan tanpa talian

Larian tanpa talian membaca fail dunia dan mencetak dunia akhir serta keputusannya. Dengan `--animate` robot bergerak dalam terminal; dengan `--start X Y HEADING` anda memilih permulaan (arah 0 ialah timur, 1 utara, 2 barat, 3 selatan):

```bash
python -m reeborg_maze tests/worlds/problem_world.json
python -m reeborg_maze tests/worlds/problem_world.json --animate
python -m reeborg_maze tests/worlds/problem_world.json --animate --delay 0.05 --start 1 1 0
```

## Jalankan ujian

```bash
python -m pytest -v
```

Setiap sel kosong dalam tiga dunia ujian dicuba dengan keempat-empat arah, untuk fungsi yang diuji dan juga skrip yang boleh ditampal.
