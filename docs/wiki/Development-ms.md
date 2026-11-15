# Pembangunan

🌐 [English](Development) · [Dansk](Development-da) · **Bahasa Melayu**

## Semakan sebelum perubahan

Jalankan pemformat, linter, penyemak jenis dan ujian:

```bash
ruff format src tests
ruff check src tests
mypy
python -m pytest
```

Kod diformat oleh `ruff`, disemak dengan `ruff` dan `mypy --strict`, dan mengikut lapisan yang diterangkan dalam [Cara Ia Berfungsi](How-It-Works-ms). Import menghala ke dalam: domain tidak mengimport apa-apa daripada lapisan lain.

## Ujian

Ujian berada dalam tiga folder yang mencerminkan lapisan: `tests/unit` (peraturan dengan robot palsu), `tests/integration` (penyelesai dan simulator pada dunia ujian) dan `tests/e2e` (baris arahan dan skrip yang boleh ditampal).

## Peraturan projek

Projek ini mengikut proses yang didokumenkan: pelan, dokumen yang disemak dan kod yang disemak sebelum perubahan digabungkan. Dokumen berada dalam folder `docs/` repositori, bermula dengan Kes Perniagaan dan Pelan Projek; README menyenaraikannya. Perubahan pada `src/` atau `tests/` tergolong dalam satu tugas bagi pencapaian yang diterima.

## Lesen

GNU Affero General Public License v3 atau lebih baharu; lesen diisytiharkan dalam `pyproject.toml`.
