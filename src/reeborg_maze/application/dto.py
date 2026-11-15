"""!
@file dto.py
@brief Data that crosses the boundary of the application layer.
"""

from dataclasses import dataclass

from .world_view import WorldView


@dataclass(frozen=True)
class StartPosition:
    """!
    @brief Cell and heading from which the robot starts (heading 0=E 1=N 2=W 3=S).
    """

    x: int
    y: int
    heading: int


@dataclass(frozen=True)
class SolveResult:
    """!
    @brief Outcome of one run.
    """

    x: int
    y: int
    actions: int
    goal_reached: bool
    view: WorldView
