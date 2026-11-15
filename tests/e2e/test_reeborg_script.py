"""!
@file test_reeborg_script.py
@brief The pasteable Reeborg script behaves like the tested solver (objective O2).
"""

from pathlib import Path

import pytest

import reeborg_maze
from reeborg_maze import SimulatedRobot, load_world
from support import WORLDS_DIR, free_starts

SCRIPT_PATH = Path(reeborg_maze.__file__).parent / "presentation" / "reeborg_script.py"
SCRIPT = SCRIPT_PATH.read_text(encoding="utf-8")
CODE = compile(SCRIPT, "reeborg_script.py", "exec")


def run_script(robot: SimulatedRobot) -> None:
    """!
    @brief Execute the script with Reeborg's five functions bound to the robot.
    """
    names = {
        "move": robot.move,
        "turn_left": robot.turn_left,
        "front_is_clear": robot.front_is_clear,
        "right_is_clear": robot.right_is_clear,
        "at_goal": robot.at_goal,
    }
    exec(CODE, {"__name__": "reeborg_script", **names})  # noqa: S102


@pytest.mark.parametrize(("name", "x", "y", "heading"), free_starts())
def test_script_reaches_goal_from_every_free_cell_and_heading(
    name: str, x: int, y: int, heading: int
) -> None:
    robot = SimulatedRobot(load_world(WORLDS_DIR / name), x, y, heading)
    run_script(robot)
    assert robot.at_goal()
