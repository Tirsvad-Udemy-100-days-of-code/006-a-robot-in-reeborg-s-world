"""!
@file ports.py
@brief Interfaces the use case needs from the outside world.
"""

from collections.abc import Callable
from pathlib import Path
from typing import Protocol

from ..domain.robot import Robot
from .dto import StartPosition
from .world_view import WorldView


class TrackedRobot(Robot, WorldView, Protocol):
    """!
    @brief A robot that also reports where it is and how many actions it took.
    """


class RobotWorldGateway(Protocol):
    """!
    @brief Builds a robot in a world stored outside the program.
    """

    def create_robot(
        self,
        world_path: Path,
        start: StartPosition | None,
        on_action: Callable[[WorldView], None] | None,
    ) -> TrackedRobot:
        """!
        @brief Read the world and place a robot in it.
        @param world_path File that describes the world.
        @param start Start override, or None for the start stored in the file.
        @param on_action Callback invoked after every move or turn, or None.
        """
        ...
