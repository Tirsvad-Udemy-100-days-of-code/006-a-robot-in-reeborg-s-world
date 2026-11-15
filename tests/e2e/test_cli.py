"""!
@file test_cli.py
@brief The command line from argument to printed result.
"""

import pytest

from reeborg_maze.presentation.cli import main
from support import WORLDS


def test_prints_the_world_and_the_result(capsys: pytest.CaptureFixture[str]) -> None:
    code = main([str(WORLDS[0])])
    out = capsys.readouterr().out
    assert code == 0
    assert "Goal reached at" in out
    assert "G" in out


def test_start_option_overrides_the_start(capsys: pytest.CaptureFixture[str]) -> None:
    code = main([str(WORLDS[0]), "--start", "1", "1", "0"])
    assert code == 0
    assert "Goal reached at" in capsys.readouterr().out


def test_animation_draws_frames_without_the_final_world(
    capsys: pytest.CaptureFixture[str],
) -> None:
    code = main([str(WORLDS[0]), "--animate", "--delay", "0"])
    out = capsys.readouterr().out
    assert code == 0
    assert "\x1b[2J" in out
    assert out.count("actions:") > 1
