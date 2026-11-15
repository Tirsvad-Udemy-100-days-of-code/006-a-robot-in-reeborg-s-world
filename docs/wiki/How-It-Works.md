# How It Works

🌐 **English** · [Dansk](How-It-Works-da) · [Bahasa Melayu](How-It-Works-ms)

## The method

The robot follows the right wall:

1. Walk forward until a wall is hit, then turn left. This puts a wall on the right and avoids an endless walk in open space.
2. Until the goal is reached: if the right side is clear, turn right and move; otherwise, if the front is clear, move; otherwise turn left.

Reeborg's world has no "turn right", so turning right is three left turns.

## The parts

| Layer | Folder in `src/reeborg_maze` | What it holds |
| --- | --- | --- |
| Domain | `domain/` | The wall-following rule and the interface of a robot; imports nothing else |
| Application | `application/` | The use case that solves a world file, and the ports it needs |
| Infrastructure | `infrastructure/` | The offline simulator and the reader of Reeborg world files |
| Presentation | `presentation/` | The command line, the text drawing and the script to paste into Reeborg's world |

The script in `presentation/reeborg_script.py` repeats the rule because Reeborg's world cannot import code. A test runs the script against the simulator for every free start, so the two copies cannot drift apart.
