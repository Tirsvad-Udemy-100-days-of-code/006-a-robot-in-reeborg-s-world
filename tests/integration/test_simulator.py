"""!
@file test_simulator.py
@brief The solver and the simulator together, on the provided world files.
"""

import copy
from pathlib import Path

import pytest

from reeborg_maze import SimulatedRobot, load_world, solve_maze
from reeborg_maze.infrastructure.simulated_robot import SimulationError
from support import WORLDS, WORLDS_DIR, free_starts


def test_worlds_exist() -> None:
    assert WORLDS


@pytest.mark.parametrize("path", WORLDS, ids=lambda p: p.name)
def test_reaches_goal_from_the_start_in_the_file(path: Path) -> None:
    robot = SimulatedRobot(load_world(path))
    solve_maze(robot)
    assert robot.at_goal()


@pytest.mark.parametrize(("name", "x", "y", "heading"), free_starts())
def test_reaches_goal_from_every_free_cell_and_heading(
    name: str, x: int, y: int, heading: int
) -> None:
    robot = SimulatedRobot(load_world(WORLDS_DIR / name), x, y, heading)
    solve_maze(robot)
    assert robot.at_goal()


def test_moving_into_a_wall_raises_a_simulation_error() -> None:
    robot = SimulatedRobot(load_world(WORLDS[0]), 1, 1, 3)
    with pytest.raises(SimulationError):
        robot.move()


def test_the_action_limit_stops_an_endless_run(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("reeborg_maze.infrastructure.simulated_robot.MAX_ACTIONS", 3)
    robot = SimulatedRobot(copy.deepcopy(load_world(WORLDS[0])), 1, 1, 0)
    with pytest.raises(SimulationError):
        for _ in range(10):
            robot.turn_left()


def test_on_action_is_called_after_each_turn() -> None:
    seen: list[int] = []
    robot = SimulatedRobot(
        load_world(WORLDS[0]), on_action=lambda r: seen.append(r.actions)
    )
    robot.turn_left()
    robot.turn_left()
    assert seen == [1, 2]
