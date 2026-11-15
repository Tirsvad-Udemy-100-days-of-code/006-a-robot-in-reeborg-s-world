# Udvikling

🌐 [English](Development) · **Dansk** · [Bahasa Melayu](Development-ms)

## Tjek før en ændring

Kør formatereren, lintern, typetjekkeren og testene:

```bash
ruff format src tests
ruff check src tests
mypy
python -m pytest
```

Koden formateres af `ruff`, tjekkes med `ruff` og `mypy --strict` og følger lagene beskrevet i [Sådan virker det](How-It-Works-da). Importer peger indad: domænet importerer intet fra de andre lag.

## Test

Testene ligger i tre mapper, der afspejler lagene: `tests/unit` (reglen med en falsk robot), `tests/integration` (løseren og simulatoren på testverdenerne) og `tests/e2e` (kommandolinjen og scriptet, der kan indsættes).

## Projektets regler

Projektet følger en dokumenteret proces: en plan, gennemgåede dokumenter og gennemgået kode, før en ændring flettes. Dokumenterne ligger i mappen `docs/` i repositoriet, med forretningscasen og projektplanen først; README oplister dem. En ændring i `src/` eller `tests/` hører til en opgave i en godkendt milepæl.

## Licens

GNU Affero General Public License v3 eller nyere; licensen er angivet i `pyproject.toml`.
