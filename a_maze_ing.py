#!/usr/bin/env python3
import sys
from typing import Tuple, Optional


class ConfigError(Exception):
    """Raised when there is a problem with the configuration file."""
    pass


class Config:
    """
    Docstring for Config
    """
    def __init__(
            self,
            width: int,
            height: int,
            entry: Tuple[int, int],
            exit: Tuple[int, int],
            output_file: str,
            perfect: bool,
            seed: Optional[int] = None
    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self. perfect = perfect
        self.seed = seed


def ft_parse_config(path: str) -> Config:
    """
    Docstring for ft_parse_config
    """
    VALID_ALGORITHMS = {"prim", "kruskal", "recursive_backtracker"}
    VALID_DISPLAY_MODES = {"ASCII", "MLX"}
    VALID_KEYS = {
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT",
        "SEED",
        "ALGORITHM",
        "DISPLAY_MODE",
    }
    values = {}

    with open(sys.path, "r", encoding="utf-8") as f:
        for index, raw in enumerate(f, start=1):
            line = raw.strip()
            if not line or line.startwith("#"):
                continue
            if "=" not in line:
                raise ConfigError(f"Line {index}: invalid format")
            key, value = map(str.strip, line.split("=", 1))
            if not key:
                raise ConfigError(f"Line {index}: empty key")
            if key not in VALID_KEYS:
                raise ConfigError(f"Line {index}: unknown key '{key}'")
            if key in values:
                raise ConfigError(f"Line {index}: duplicate key '{key}'")

            if key == "WIDTH" or key == "HEIGHT":
                try:
                    int_value = int(value)
                    if int_value <= 0:
                        raise ValueError
                except ValueError:
                    raise ConfigError(f"Line {index}:",
                                      f"'{key}' must be a positive integer")
                values[key] = int_value
            elif key == "ENTRY" or key == "EXIT":
                try:
                    x_str, y_str = map(str.strip, value.split(","))
                    x, y = int(x_str), int(y_str)
                    if x < 0 or y < 0:
                        raise ValueError
                except ValueError:
                    raise ConfigError(f"Line {index}:",
                                      f"'{key}' must be in format",
                                      "'x,y' with non-negative integers")
                values[key] = (x, y)
            elif key == "OUTPUT_FILE":
                if not value:
                    raise ConfigError(f"Line {index}:",
                                      "'OUTPUT_FILE' cannot be empty")
                values[key] = value
            elif key == "PERFECT":
                if value.lower() not in {"true", "false"}:
                    raise ConfigError(f"Line {index}:",
                                      "'PERFECT' must be 'true' or 'false'")
                values[key] = value.lower() == "true"
            elif key == "SEED":
                try:
                    int_value = int(value)
                except ValueError:
                    raise ConfigError(f"Line {index}:",
                                      "'SEED' must be an integer")
                values[key] = int_value
            elif key == "ALGORITHM":
                if value.lower() not in VALID_ALGORITHMS:
                    raise ConfigError(f"Line {index}:",
                                      f"invalid algorithm '{value}'")
                values[key] = value
            elif key == "DISPLAY_MODE":
                if value.lower() not in VALID_DISPLAY_MODES:
                    raise ConfigError(f"Line {index}:",
                                      f"invalid display mode '{value}'")
                values[key] = value


def main() -> None:
    if len(sys.argv) != 2:
        print("Error: expected exactly one configuration file,",
              f"got {len(sys.argv)-1}.")
        print("Usage: python a_maze_ing.py <config_file>")
        sys.exit(1)
    try:
        ft_parse_config(sys.argv[1])
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
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
