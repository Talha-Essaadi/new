#!/usr/bin/env python3
import sys
from config import ConfigParser, ConfigError
from mazegen import MazeGenerator, OutputEncoder
import random
import mlx
# from typing import Optional, Tuple










def main() -> None:
    if len(sys.argv) != 2:
        print("Error: expected exactly one configuration file,",
              f"got {len(sys.argv)-1}.")
        print(f"Usage: python3 {sys.argv[0]} <config_file>")
        sys.exit(1)
    try:
        parser = ConfigParser(sys.argv[1])
        parser.parse()
        parser.validate()
        config = parser.get_values()
        print(f"config : {config.__dict__})")
        maze = MazeGenerator(config).generate()
        # path = MazeSolver.solve(maze)
        path = "NESWWSEENNNNNEESESSWW"
        OutputEncoder.write(maze, path, config.output_file)
        # Renderer.display(maze, path)
    except FileNotFoundError:
        print("Error: configuration file not found", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print("Error: permission denied when reading config file",
              file=sys.stderr)
        sys.exit(1)
    except ConfigError as e:
        print(f"Config error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Value error: {e}", file=sys.stderr)
        sys.exit(1)
    # except Exception as e:
    #     print(f"Unexpected error: {e}", file=sys.stderr)
    #     sys.exit(1)


if __name__ == "__main__":
    main()
