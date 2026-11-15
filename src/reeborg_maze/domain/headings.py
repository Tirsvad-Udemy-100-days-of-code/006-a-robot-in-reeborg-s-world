"""!
@file headings.py
@brief Compass headings of Reeborg's world and the step each one takes.
"""

## Compass headings in Reeborg's world, counter-clockwise: east, north, west, south.
EAST: int = 0
NORTH: int = 1
WEST: int = 2
SOUTH: int = 3

## Number of headings; used for modular turning.
HEADING_COUNT: int = 4

## Unit step (dx, dy) for each heading. Reeborg's y axis grows northwards.
HEADING_STEP: dict[int, tuple[int, int]] = {
    EAST: (1, 0),
    NORTH: (0, 1),
    WEST: (-1, 0),
    SOUTH: (0, -1),
}
