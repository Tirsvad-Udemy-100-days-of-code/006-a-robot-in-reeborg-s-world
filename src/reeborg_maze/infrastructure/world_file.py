"""!
@file world_file.py
@brief Reads Reeborg world JSON files and builds simulated robots from them.
"""

import json
from collections.abc import Callable
from pathlib import Path

from ..application.dto import StartPosition
from ..application.ports import TrackedRobot
from ..application.world_view import WorldView
from .simulated_robot import SimulatedRobot, WorldData


def load_world(path: str | Path) -> WorldData:
    """!
    @brief Read a Reeborg world JSON file.
    @param path File to read.
    @return Parsed world dictionary.
    """
    world: WorldData = json.loads(Path(path).read_text(encoding="utf-8"))
    return world


class WorldFileGateway:
    """!
    @brief Port implementation that builds a SimulatedRobot from a world file.
    """

    def create_robot(
        self,
        world_path: Path,
        start: StartPosition | None,
        on_action: Callable[[WorldView], None] | None,
    ) -> TrackedRobot:
        """!
        @brief Read the world and place a simulated robot in it.
        @param world_path File that describes the world.
        @param start Start override, or None for the start stored in the file.
        @param on_action Callback invoked after every move or turn, or None.
        """
        world = load_world(world_path)
        if start is None:
            return SimulatedRobot(world, on_action=on_action)
        return SimulatedRobot(
            world, start.x, start.y, start.heading, on_action=on_action
        )
