"""!
@file support.py
@brief Helpers shared by the test layers: the provided worlds and every start.
"""

from pathlib import Path

from reeborg_maze import load_world
from reeborg_maze.domain.headings import HEADING_COUNT

WORLDS_DIR = Path(__file__).parent / "worlds"
WORLDS = sorted(WORLDS_DIR.glob("*.json"))
BLOCKING = {"mud", "water"}


def free_starts() -> list[tuple[str, int, int, int]]:
    """!
    @brief Every (world, x, y, heading) where the robot can start.
    """
    starts = []
    for path in WORLDS:
        world = load_world(path)
        for x in range(1, world["cols"] + 1):
            for y in range(1, world["rows"] + 1):
                if BLOCKING.intersection(world.get("tiles", {}).get(f"{x},{y}", [])):
                    continue
                for heading in range(HEADING_COUNT):
                    starts.append((path.name, x, y, heading))
    return starts
