# instructions : ✅ ❌

1. Your functions should handle exceptions gracefully to avoid crashes. Use try-except blocks to manage potential errors. Prefer context managers for resources like files or connections to ensure automatic cleanup. If your program crashes due to unhandled exceptions during the review, it will be considered non-functional.

2. • All resources (e.g., file handles, network connections) must be properly managed to prevent leaks. Use context managers where possible for automatic handling.

3. • Your code must include type hints for function parameters, return types, and variables where applicable (using the typing module). Use `mypy` for static type checking. All functions must pass mypy without errors.

4. • Include docstrings in functions and classes following PEP 257 (e.g., Google or
NumPy style) to document purpose, parameters, and returns.

5. Create test programs to verify project functionality (not submitted or graded). Use
frameworks like pytest or unittest for unit tests, covering edge cases.

6. Include a Makefile in your project to automate common tasks. It must contain the
following rules (mandatory lint implies the specified flags; it is strongly recommended to
try –strict for enhanced checking):



# help :
```py
[ Config Parser ]
        ↓
[ MazeGenerator (core, reusable, tested) ]
        ↓
[ Solver (shortest path) ]
        ↓
[ Output Encoder (hex format) ]
        ↓
[ Visual Renderer ]
```
1. Propose a clean project architecture

2. Help you choose the best algorithm (Prim / DFS / Kruskal)

3. Design the MazeGenerator class API

4. Explain hex encoding with examples

5. Help you plan the “42” pattern insertion safely

# Project Architecture:

```sh
┌──────────────────────┐
│  a_maze_ing.py       │  ← CLI entry point (thin)
└─────────┬────────────┘
          ↓
┌──────────────────────┐
│  ConfigParser        │  ← config.txt validation
└─────────┬────────────┘
          ↓
┌──────────────────────┐
│  MazeGenerator       │  ← core reusable engine (PACKAGE)
│  + MazeCell          │
│  + MazeGrid          │
└─────────┬────────────┘
          ↓
┌──────────────────────┐
│  MazeSolver          │  ← shortest path
└─────────┬────────────┘
          ↓
┌──────────────────────┐
│  OutputEncoder       │  ← hex + file writing
└─────────┬────────────┘
          ↓
┌──────────────────────┐
│  Renderer            │  ← ASCII / MLX display
└──────────────────────┘

```

```py
def main():
    parser = ConfigParser("config.txt")
    parser.parse()
    config = parser.validate()

    maze = MazeGenerator(config).generate()
    OutputEncoder().write(maze, config.output_file)
    Renderer().render_ascii(maze)
```

# Repository Architecture:
```sh
.
├── a_maze_ing.py              # Main executable (required name)
├── config/
│   └── default_config.txt
├── mazegen/                   # Reusable package
│   ├── __init__.py
│   ├── generator.py           # MazeGenerator (CORE)
│   ├── cell.py                # MazeCell abstraction
│   ├── grid.py                # MazeGrid (2D structure)
│   ├── algorithms.py          # DFS / Prim / Kruskal
│   ├── solver.py              # Shortest path logic
│   ├── encoder.py             # Hex encoding logic
│   ├── exceptions.py          # Custom errors
│   └── types.py               # Shared typing aliases
├── display/
│   ├── ascii_renderer.py
│   └── __init__.py
├── Makefile
├── README.md
├── pyproject.toml              # Packaging
├── setup.cfg / setup.py        # flake8 / mypy config
└── .gitignore
```

# hints:
```py
class MazeGenerator:
    def __init__(
        self,
        width: int,
        height: int,
        entry: Coord,
        exit: Coord,
        seed: Optional[int] = None,
        perfect: bool = True,
        algorithm: Algorithm = Algorithm.DFS,
    ) -> None
```

# Questions:
1. explain this :
    1. Include a .gitignore file to exclude Python artifacts.
    2. It is recommended to use virtual environments (e.g., venv or conda) for dependency isolation during development.
    3. The structure ensures full connectivity and no isolated cells (except the ’42’ pattern, see below).
    4. ◦ As entry and exist are specific cells, there must be walls at the external borders.

# Knowledge :

1. What is context manager mean ?

2. ✅ What mypy mean ?
    - **mypy** is a static type checker for Python that verifies your code against its type hints before execution, helping detect type-related errors early and improve code reliability and maintainability.

3. ✅ what is typing module mean ?
4. ✅ Include docstrings in functions and classes following PEP 257 (e.g.     Google or NumPy style) to document purpose, parameters, and returns.
5. define this flag -strict
6. explain python debugger
7. know what this folder contain ? __pycache__, .mypy_cache
8. know these command :
```sh
 mypy . --warn-return-any
--warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
```
9. know `pytest` and `unittest`
10. what is virutal envirenmment in python ? (venv , conda)
11. what is MiniLibX ? MiniLibX (MLX) Library
12. explain this :
    debug: Run the main script in debug mode using Python’s built-in debugger (e.g.,
    pdb).
13. explain this command:
```sh
mypy . --strict
```
14. ✅ explain Docstrings (PEP 257)
15. explain this Terminal ASCII rendering or MLX graphical display
16. what this mean : no 3×3 open areas
17. what happen when i write and mazegen is a folder:
```py
from mazegen import MazeGenerator
```
18. ✅ explain all config file Keys
    ```py
    config = {
        "width": 20,
        "height": 10,
        "seed": 42,
        "algorithm": "dfs",
        "display_mode": "ascii"
    }
    ```
    - seed key is integer if i pass the generate maze function the number 42 it generate the same maze each time 


# before push:
1. flake8
2. create Numpy docstrings

# Steps:✅ ❌

1. ✅ Read the config file plus handle errors
2. ❌ parse the file and save thier key in object and return the object
    - Your program must handle all errors gracefully:
    1. ✅ invalid configuration: 
    2. ✅ file not found:
    3. ✅ bad syntax:
        - ✅ line doesnt contian "="
    4. ❌ impossible maze parameters:
    5. ✅ the ENTRY and EXIT values mast be logic values
    6. ✅ the ENTRY and EXIT values mast be deffrent
    7. ✅ handle Permission Error
    8. ✅ handle duplicate key
    9. ❌ handle incorrect values
    10. ✅ skip comments
    11. ✅ skip Empty lines
    11. ✅ missing requierd keys
    16. etc. 
    - It must never crash unexpectedly, and must always provide a clear error message to the user.
3. generate valid maze:
    -  The maze must be valid, meaning:
    1. Entry and exit exist and are different, inside the maze bounds.
    2. ◦ Your generated data must be coherent: each neighbouring cell must have the
    same wall if any. E.g., it is forbidden to have a first cell with a wall on the
    east side, and the second cell behind that wall without a wall on the west side.
    3. When visually represented (see below), the maze must contain a visible “42” drawn by several fully closed cells.
    4.  The maze can’t have large open areas. Corridors can’t be wider than 2 cells.
    For example, you can have 2x3 or 3x2 open area, but never a 3x3 open area.
    5. • If the PERFECT flag is activated, the maze must contain exactly one path between
    the entry and the exit (i.e., it must be a perfect maze).

```py
def main() -> None:
    config = load_config(sys.argv[1])
    maze = MazeGenerator.from_config(config).generate()
    path = MazeSolver.solve(maze)
    OutputEncoder.write(maze, path, config.output_file)
    Renderer.display(maze, path)
```

```
WIDTH       | WIDTH=20
HEIGHT      | HEIGHT=15
ENTRY       | ENTRY=0,0
EXIT        | EXIT=19,14
OUTPUT_FILE | OUTPUT_FILE=maze.txt
PERFECT     | PERFECT=True
```