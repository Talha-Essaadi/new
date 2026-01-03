Reads options from a text file (config file).
Generates a maze using those options.
Saves the maze into an output file in a special text format (with hex digits).
Can show the maze on screen (terminal or graphical window).
Organizes the maze logic so it can be reused later as a separate library.

# config.txt
WIDTH → number of columns (cells) of the maze.
HEIGHT → number of rows (cells).
ENTRY → coordinates of the start cell, like ENTRY=0,0.
EXIT → coordinates of the end cell, like EXIT=19,14.
OUTPUT_FILE → name of the file where you write the maze.  -> mssg if file not exists 
PERFECT → True or False (whether there is exactly one path from start to end).


# maze
Up (North), Right (East), Down (South), Left (West)

0 → 0000 → all walls open.
F → 1111 → all walls closed.
3 → 0011 → North + East closed, South + West open.
A → 1010 → East + West closed, North + South open
-----limn lt7t lisr lfoq-----

# Makefile
mypy . : type checking for hints in all file code
flake8 . : style checking

1- warnings
--warn-return-any : warn if a function returns Any type
--disallow-untyped-defs : warn if a function has no type hints
--warn-unused-ignores : warn if there are unused type ignore comments ex: x=10 # type: ignore
    ex : x: int = "hello" # type: ignore = warn && like x = "hello" # type: ignore = warn 
--ignore-missing-imports : ignore imports that mypy cannot find stubs for
    ex : Mypy will not show errors about “missing types for mlx”.

2- lint
Looks at your code,
Finds style issues, bad patterns, and some bugs, its like flake8 + mypy
*** __pycache__ ***
Created automatically by Python when you run code.
It stores compiled .pyc files to make imports faster.
You never edit it by hand; it can always be deleted safely.
.py = your source code.
.pyc (in __pycache__) = compiled version Python reuses for speed.
*** .mypy_cache ***
Created automatically by mypy when it checks your types.
It stores analysis results so future mypy runs are faster.
Also safe to delete anytime


# venv
venv has its own Python interpreter and libraries.
why need it to avoid package conflicts
Different projects may need different versions of the same library.
example : You install packages globally with pip install ....
          All projects share the same versions.
          One project may need mypy==1.10, another needs mypy==1.5 → conflicts.

❌ Without venv:
Project A → Django 3.2
Project B → Django 5.0

Installing one breaks the other

✔️ With venv:
venv_A → Django 3.2
venv_B → Django 5.0
*** install venv ***
cd my_project
python -m venv venv
source venv/bin/activate