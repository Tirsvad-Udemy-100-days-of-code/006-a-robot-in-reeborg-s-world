"""!
@file constants.py
@brief Characters and timing used when the world is drawn in the terminal.
"""

from ..domain.headings import EAST, NORTH, SOUTH, WEST

## Characters that show the robot's heading in the text visualisation.
HEADING_SYMBOL: dict[int, str] = {
    EAST: ">",
    NORTH: "^",
    WEST: "<",
    SOUTH: "v",
}

## Default pause between animation frames, in seconds.
DEFAULT_FRAME_DELAY: float = 0.15

## ANSI escape sequences: clear the screen, and move the cursor to the top left.
ANSI_CLEAR: str = "\x1b[2J"
ANSI_HOME: str = "\x1b[H"
