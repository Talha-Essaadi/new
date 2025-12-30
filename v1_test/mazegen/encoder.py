#!/usr/bin/env python3
from mazegen.grid import MazeGrid


class OutputEncoder:
    @staticmethod
    def write(maze: MazeGrid, path: str, output_file: str) -> None:
        with open(output_file, 'w') as f:
            for y in range(maze.height):
                row = ''
                for x in range(maze.width):
                    number = 0
                    cell = maze.get_cell((y, x))
                    if cell.north:
                        number = number | 1
                    if cell.east:
                        number = number | 2
                    if cell.south:
                        number = number | 4
                    if cell.west:
                        number = number | 8
                    row += hex(number)[2:].upper()
                f.write(row + '\n')
                print(row)
            f.write('\n')
            f.write(f"{maze.start[0]},{maze.start[1]}\n")
            f.write(f"{maze.end[0]},{maze.end[1]}\n")
            f.write(path + '\n')