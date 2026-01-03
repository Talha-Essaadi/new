PYTHON := python3

all :
	ls

active:
	source ./home/tessaadi/Desktop/A-Maze-ing/v1_test/venv/bin/activate

close:
	deactivate

install:
    $(PYTHON) -m pip install -r requirements.txt

run:
    $(PYTHON) a_maze_ing.py config.txt

debug:
    $(PYTHON) -m pdb a_maze_ing.py config.txt

clean:
    rm -rf __pycache__ .mypy_cache

lint:
    flake8 .
    mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

