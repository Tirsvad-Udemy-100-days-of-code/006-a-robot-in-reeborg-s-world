"""!
@file world_view.py
@brief The read-only view of a world and its robot that a presentation draws.
"""

from typing import Protocol


class WorldView(Protocol):
    """!
    @brief What a presentation needs to draw the world and the robot in it.
    """

    cols: int
    rows: int
    x: int
    y: int
    heading: int
    goal: tuple[int, int]
    actions: int

    def wall_between(self, x: int, y: int, heading: int) -> bool:
        """!@brief Whether a wall or the world edge blocks leaving toward heading."""
        ...

    def is_blocked_tile(self, x: int, y: int) -> bool:
        """!@brief Whether the cell holds a tile the robot cannot enter."""
        ...
