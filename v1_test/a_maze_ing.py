#!/usr/bin/env python3
import sys
from config.config_parser import ConfigParser
from config.exceptions import ConfigError
from config.models import Config
from typing import List, Tuple
import mlx
import random

# from typing import Optional, Tuple



# class MazeGenerator:
#     def __init__(
#         self,
#         width: int,
#         height: int,
#         entry: Coord,
#         exit: Coord,
#         seed: Optional[int] = None,
#         perfect: bool = True,
#         algorithm: Algorithm = Algorithm.DFS,
#     ) -> None:
#         self.width = width
#         self.height = height
#         self.entry = entry
#         self.exit = exit
#         self.seed = seed
#         self.perfect = perfect
#         self.algorithm = algorithm


class Stack:
    """
    Docstring for Stack
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.items.pop()

    def peek(self):
        print(f"Peeking stack: {self.items}")
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


class Cell:
    def __init__(self):
        self.north = True
        self.south = True
        self.east = True
        self.west = True
        self.visited = False


class MazeGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid: List[List[Cell]] = [
            [Cell() for _ in range(width)] for _ in range(height)
        ]

    def get_cell(self, cell: Cell) -> Cell:
        x, y = cell
        return self.grid[x][y]

    def get_nieghbors(self, cell: Cell) -> List[tuple[int, int]]:
        x, y = cell
        neighbors = []
        print(f"Getting neighbors for cell: {cell} at position ({x}, {y})")
        if x - 1 >= 0 and not self.grid[x-1][y].visited:
            neighbors.append((x - 1, y))  # North

        if x + 1 < self.height and not self.grid[x+1][y].visited:
            neighbors.append((x + 1, y))  # South

        if y - 1 >= 0 and not self.grid[x][y-1].visited:
            neighbors.append((x, y - 1))  # West

        if y + 1 < self.width and not self.grid[x][y+1].visited:
            neighbors.append((x, y + 1))  # East
        return neighbors
    
    def remove_walls(self, cell_1, cell_2) -> None:
        if cell_1 is None:
            return
        x1, y1 = cell_1
        x2, y2 = cell_2
        if x1 == x2 and y1 < y2:
            print(f"Removing east wall of {cell_1} and west wall of {cell_2}")
            self.grid[x1][y1].east = False
            self.grid[x2][y2].west = False
        elif x1 == x2 and y1 > y2:
            print(f"Removing west wall of {cell_1} and east wall of {cell_2}")
            self.grid[x1][y1].west = False
            self.grid[x2][y2].east = False
        elif y1 == y2 and x1 < x2:
            print(f"Removing south wall of {cell_1} and north wall of {cell_2}")
            self.grid[x1][y1].south = False
            self.grid[x2][y2].north = False
        elif y1 == y2 and x1 > x2:
            print(f"Removing north wall of {cell_1} and south wall of {cell_2}")
            self.grid[x1][y1].north = False
            self.grid[x2][y2].south = False


class MazeGenerator:
    """
    Docstring for MazeGenerator
    """
    def __init__(self, config: Config):
        self.config = config

    def generate(self):
        seed = random.randint(1, 1000)
        if self.config.seed is not None:
            seed = self.config.seed
        random.seed(seed)
        cell: Tuple[int, int] = (0, 0)
        maze = MazeGrid(self.config.width, self.config.height)
        stack = Stack()
        i = 0
        limit = maze.width * maze.height
        stack.push(cell)
        while stack.is_empty() is False:
            print(f"i: {i}, limit: {limit}")
            maze.get_cell(cell).visited = True
            neighbors = maze.get_nieghbors(cell)
            print(f"neighbors: {neighbors}")
            if neighbors:
                i += 1
                cell = random.choice(neighbors)
                print(f"Chosen cell: {cell}")
                maze.remove_walls(stack.peek(), cell)
                stack.push(cell)
            else:
                print("No neighbors, backtracking")
                stack.pop()
                cell = stack.peek()
            print("\n\n\n\n")
        return maze




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
        # OutputEncoder.write(maze, path, config.output_file)
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
