"""!
@file solve_world.py
@brief Use case UC-001 Solve the maze, run against a world file.
"""

from collections.abc import Callable
from pathlib import Path

from ...domain.wall_following import solve_maze
from ..dto import SolveResult, StartPosition
from ..ports import RobotWorldGateway
from ..world_view import WorldView


class SolveWorld:
    """!
    @brief Place a robot in a world and drive it to the goal by wall following.
    """

    def __init__(self, gateway: RobotWorldGateway) -> None:
        """!
        @param gateway Port that builds the robot in its world.
        """
        self._gateway = gateway

    def execute(
        self,
        world_path: Path,
        start: StartPosition | None = None,
        on_action: Callable[[WorldView], None] | None = None,
    ) -> SolveResult:
        """!
        @brief Run the solver.
        @param world_path File that describes the world.
        @param start Start override, or None for the start stored in the file.
        @param on_action Callback invoked after every move or turn, or None.
        @return Final cell, number of actions and whether the goal was reached.
        """
        robot = self._gateway.create_robot(world_path, start, on_action)
        if on_action is not None:
            on_action(robot)
        solve_maze(robot)
        return SolveResult(robot.x, robot.y, robot.actions, robot.at_goal(), robot)
