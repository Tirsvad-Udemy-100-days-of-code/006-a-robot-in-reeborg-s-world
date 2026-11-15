"""!
@file __init__.py
@brief Business rules of the maze exercise; imports nothing outside the package.
"""

from .robot import Robot
from .wall_following import solve_maze, turn_right

__all__ = ["Robot", "solve_maze", "turn_right"]
