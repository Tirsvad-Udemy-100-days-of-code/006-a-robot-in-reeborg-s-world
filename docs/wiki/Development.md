# Development

🌐 **English** · [Dansk](Development-da) · [Bahasa Melayu](Development-ms)

## Checks before a change

Run the formatter, the linter, the type checker and the tests:

```bash
ruff format src tests
ruff check src tests
mypy
python -m pytest
```

The code is formatted by `ruff`, checked with `ruff` and `mypy --strict`, and follows the layers described in [How It Works](How-It-Works). Imports point inward: the domain imports nothing from the other layers.

## Tests

Tests are in three folders that mirror the layers: `tests/unit` (the rule with a fake robot), `tests/integration` (the solver and the simulator on the test worlds) and `tests/e2e` (the command line and the pasteable script).

## Project rules

The project follows a documented process: a plan, reviewed documents and reviewed code before a change is merged. The documents are in the `docs/` folder of the repository, starting with the Business Case and the Project Plan; the README lists them. A change to `src/` or `tests/` belongs to a task of an accepted milestone.

## Licence

GNU Affero General Public License v3 or later; the licence is declared in `pyproject.toml`.
