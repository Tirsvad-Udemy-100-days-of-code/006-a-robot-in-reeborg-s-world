"""!
@file robot.py
@brief The robot as the wall-following rule sees it.
"""

from typing import Protocol


class Robot(Protocol):
    """!
    @brief The subset of Reeborg's API the solver needs.
    """

    def move(self) -> None:
        """!@brief Move one cell forward."""
        ...

    def turn_left(self) -> None:
        """!@brief Rotate 90 degrees counter-clockwise."""
        ...

    def front_is_clear(self) -> bool:
        """!@brief True if the robot can move forward."""
        ...

    def right_is_clear(self) -> bool:
        """!@brief True if the robot could move after turning right."""
        ...

    def at_goal(self) -> bool:
        """!@brief True if the robot stands on the goal."""
        ...
