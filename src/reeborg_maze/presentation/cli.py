"""!
@file cli.py
@brief Command line entry point and composition root: python -m reeborg_maze WORLD.json
"""

import argparse
from collections.abc import Sequence
from pathlib import Path

from ..application.dto import StartPosition
from ..application.use_cases.solve_world import SolveWorld
from ..infrastructure.world_file import WorldFileGateway
from .constants import DEFAULT_FRAME_DELAY
from .visualizer import make_frame_printer, render


def main(argv: Sequence[str] | None = None) -> int:
    """!
    @brief Solve a world file offline and report the final position.
    @param argv Command line arguments; None means the process arguments.
    @return Exit code: 0 when the robot reached the goal, 1 otherwise.
    """
    parser = argparse.ArgumentParser(description="Solve a Reeborg maze offline.")
    parser.add_argument("world", help="path to a Reeborg world JSON file")
    parser.add_argument(
        "--animate", action="store_true", help="show the robot moving in the terminal"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_FRAME_DELAY,
        help="seconds between animation frames (default: %(default)s)",
    )
    parser.add_argument(
        "--start",
        nargs=3,
        type=int,
        metavar=("X", "Y", "HEADING"),
        help="override start; heading 0=E 1=N 2=W 3=S",
    )
    args = parser.parse_args(argv)

    start = StartPosition(*args.start) if args.start else None
    callback = make_frame_printer(args.delay) if args.animate else None
    result = SolveWorld(WorldFileGateway()).execute(Path(args.world), start, callback)
    if not args.animate:
        print(render(result.view))
    print(f"Goal reached at ({result.x}, {result.y}) in {result.actions} actions.")
    return 0 if result.goal_reached else 1
