"""!
@file visualizer.py
@brief Text rendering and animation of a SimulatedRobot in its world.
"""

import time
from collections.abc import Callable

from ..application.world_view import WorldView
from ..domain.headings import EAST, NORTH, SOUTH, WEST
from .constants import ANSI_CLEAR, ANSI_HOME, HEADING_SYMBOL


def render(robot: WorldView) -> str:
    """!
    @brief Draw the world as text: walls, mud, goal (G) and the robot (> ^ < v).
    @param robot Robot whose world and position are drawn.
    @return Multi-line string.
    """
    lines = []
    for y in range(robot.rows, 0, -1):
        top = "".join(
            "+" + ("---" if robot.wall_between(x, y, NORTH) else "   ")
            for x in range(1, robot.cols + 1)
        )
        lines.append(top + "+")

        row = ""
        for x in range(1, robot.cols + 1):
            row += "|" if robot.wall_between(x, y, WEST) else " "
            if (x, y) == (robot.x, robot.y):
                row += f" {HEADING_SYMBOL[robot.heading]} "
            elif (x, y) == robot.goal:
                row += " G "
            elif robot.is_blocked_tile(x, y):
                row += "~~~"
            else:
                row += "   "
        row += "|" if robot.wall_between(robot.cols, y, EAST) else " "
        lines.append(row)

    lines.append(
        "".join(
            "+" + ("---" if robot.wall_between(x, 1, SOUTH) else "   ")
            for x in range(1, robot.cols + 1)
        )
        + "+"
    )
    lines.append(f"actions: {robot.actions}  position: ({robot.x}, {robot.y})")
    return "\n".join(lines)


def make_frame_printer(delay: float) -> Callable[[WorldView], None]:
    """!
    @brief Build an on_action callback that redraws the world in place.
    @param delay Seconds to pause after each frame.
    @return Callback accepting a view of the world.
    """
    print(ANSI_CLEAR, end="")

    def show(robot: WorldView) -> None:
        print(ANSI_HOME + render(robot), flush=True)
        # The pause is the animation frame delay the user chose, not a leftover.
        time.sleep(delay)  # nosemgrep

    return show
