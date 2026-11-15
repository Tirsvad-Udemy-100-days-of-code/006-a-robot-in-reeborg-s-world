"""!
@file __main__.py
@brief Command line entry point: python -m reeborg_maze WORLD.json
"""

import sys

from .presentation.cli import main

if __name__ == "__main__":
    sys.exit(main())
