"""!
@file test_wall_following.py
@brief Unit tests of the wall-following rule with a scripted fake robot.
"""

from reeborg_maze.domain import solve_maze, turn_right


class FakeRobot:
    """!
    @brief Robot whose answers are scripted and whose calls are recorded.
    """

    def __init__(self, front: list[bool], right: list[bool], goal_after: int) -> None:
        self.calls: list[str] = []
        self._front = iter(front)
        self._right = iter(right)
        self._goal_after = goal_after

    def move(self) -> None:
        self.calls.append("move")

    def turn_left(self) -> None:
        self.calls.append("left")

    def front_is_clear(self) -> bool:
        return next(self._front)

    def right_is_clear(self) -> bool:
        return next(self._right)

    def at_goal(self) -> bool:
        return len(self.calls) >= self._goal_after


def test_turn_right_turns_left_three_times() -> None:
    robot = FakeRobot([], [], goal_after=0)
    turn_right(robot)
    assert robot.calls == ["left", "left", "left"]


def test_walks_to_the_wall_then_turns_left_before_following() -> None:
    robot = FakeRobot(front=[True, True, False], right=[], goal_after=3)
    solve_maze(robot)
    assert robot.calls == ["move", "move", "left"]


def test_turns_right_and_moves_when_the_right_side_is_clear() -> None:
    robot = FakeRobot(front=[False], right=[True], goal_after=5)
    solve_maze(robot)
    assert robot.calls == ["left", "left", "left", "left", "move"]


def test_moves_forward_when_only_the_front_is_clear() -> None:
    robot = FakeRobot(front=[False, True], right=[False], goal_after=2)
    solve_maze(robot)
    assert robot.calls == ["left", "move"]


def test_turns_left_when_front_and_right_are_blocked() -> None:
    robot = FakeRobot(front=[False, False], right=[False], goal_after=2)
    solve_maze(robot)
    assert robot.calls == ["left", "left"]


def test_stops_at_once_when_the_robot_starts_on_the_goal_after_the_first_turn() -> None:
    robot = FakeRobot(front=[False], right=[], goal_after=1)
    solve_maze(robot)
    assert robot.calls == ["left"]
