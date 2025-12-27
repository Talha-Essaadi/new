# instructions :

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

# Questions:
1. explain this :
    - Include a .gitignore file to exclude Python artifacts.
    - It is recommended to use virtual environments (e.g., venv or conda) for dependency isolation during development.

# Knowledge :

1. What is context manager mean ?
2. What mypy mean ?
3. what is typing module mean ?
4.  Include docstrings in functions and classes following PEP 257 (e.g.     Google or NumPy style) to document purpose, parameters, and returns.
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
11. what is MiniLibX ?
12. explain this :
    debug: Run the main script in debug mode using Python’s built-in debugger (e.g.,
    pdb).
13. explain this command:
```sh
mypy . --strict
```
14. explain Docstrings (PEP 257)
15. explain this Terminal ASCII rendering or MLX graphical display


# before push:
1. flake8
2. 

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