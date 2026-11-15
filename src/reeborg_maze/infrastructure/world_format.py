"""!
@file world_format.py
@brief Names and limits of the Reeborg world JSON format and of the simulator.
"""

from ..domain.headings import EAST, NORTH, SOUTH, WEST

## Wall names used in Reeborg world JSON files, keyed by heading.
HEADING_WALL_NAME: dict[int, str] = {
    EAST: "east",
    NORTH: "north",
    WEST: "west",
    SOUTH: "south",
}

## Tiles the robot cannot enter.
BLOCKING_TILES: frozenset[str] = frozenset({"mud", "water"})

## Safety limit on simulator actions, so a bad algorithm cannot loop forever.
MAX_ACTIONS: int = 10_000
