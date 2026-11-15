"""!
@file wall_following.py
@brief Right-wall-following rule that works on any robot-like object.
"""

from .robot import Robot


def turn_right(robot: Robot) -> None:
    """!
    @brief Turn the robot 90 degrees clockwise (three left turns).
    @param robot The robot to turn.
    """
    for _ in range(3):
        robot.turn_left()


def solve_maze(robot: Robot) -> None:
    """!
    @brief Drive the robot to the goal by following the wall on its right.
    @param robot Robot with a random start position and heading.

    The robot first walks straight until it hits a wall, then turns left so
    that the wall is on its right. This avoids the infinite loop that happens
    when the robot starts in open space and the right side is never blocked.
    Then, until the goal is reached:
      - right is clear: turn right and move,
      - else front is clear: move,
      - else: turn left.
    """
    while robot.front_is_clear():
        robot.move()
    robot.turn_left()

    while not robot.at_goal():
        if robot.right_is_clear():
            turn_right(robot)
            robot.move()
        elif robot.front_is_clear():
            robot.move()
        else:
            robot.turn_left()
