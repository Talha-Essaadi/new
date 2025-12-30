#!/usr/bin/env python3
from config import Config
from .grid import MazeGrid
from .data_structures import Stack
from typing import Tuple
import random


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
        maze = MazeGrid(self.config)
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