#!/usr/bin/env python3
from .cell import Cell
from typing import List
from config import Config


class MazeGrid:
    def __init__(self, config: Config):
        self.width = config.width
        self.height = config.height
        self.start = config.entry
        self.end = config.exit
        self.grid: List[List[Cell]] = [
            [Cell() for _ in range(self.width)] for _ in range(self.height)
        ]

    def get_cell(self, cell: Cell) -> Cell:
        x, y = cell
        return self.grid[x][y]

    def get_nieghbors(self, cell: Cell) -> List[tuple[int, int]]:
        x, y = cell
        neighbors = []
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
            self.grid[x1][y1].east = False
            self.grid[x2][y2].west = False
        elif x1 == x2 and y1 > y2:
            self.grid[x1][y1].west = False
            self.grid[x2][y2].east = False
        elif y1 == y2 and x1 < x2:
            self.grid[x1][y1].south = False
            self.grid[x2][y2].north = False
        elif y1 == y2 and x1 > x2:
            self.grid[x1][y1].north = False
            self.grid[x2][y2].south = False
