#!/usr/bin/env python3
from config.exceptions import ConfigError
from config.models import Config


class ConfigParser:
    """
    Docstring for ConfigParser
    """
    def __init__(self, path: str) -> None:
        self.path = path
        self.values = {}

    def parse(self) -> Config:
        VALID_ALGORITHMS = {"dfs", "prim", "kruskal", "recursive_backtracker"}
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

        with open(self.path, "r", encoding="utf-8") as f:
            for index, raw in enumerate(f, start=1):
                line = raw.strip()
                line = line.split("#", 1)[0].strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    raise ConfigError(f"Line {index}: invalid format")
                key, value = map(str.strip, line.split("=", 1))
                if not key:
                    raise ConfigError(f"Line {index}: empty key")
                if key not in VALID_KEYS:
                    raise ConfigError(f"Line {index}: unknown key '{key}'")
                if key in self.values:
                    raise ConfigError(f"Line {index}: duplicate key '{key}'")

                if key == "WIDTH" or key == "HEIGHT":
                    try:
                        int_value = int(value)
                        if int_value <= 0:
                            raise ValueError
                    except ValueError:
                        raise ConfigError(f"Line {index}: '{key}'",
                                          "must be a positive integer")
                    self.values[key] = int_value
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
                    self.values[key] = (x, y)
                elif key == "OUTPUT_FILE":
                    if not value:
                        raise ConfigError(f"Line {index}:",
                                          "'OUTPUT_FILE' cannot be empty")
                    self.values[key] = value
                elif key == "PERFECT":
                    if value.lower() not in {"true", "false"}:
                        raise ConfigError(f"Line {index}: 'PERFECT' must",
                                          "be 'true' or 'false'")
                    self.values[key] = value.lower() == "true"
                elif key == "SEED":
                    try:
                        int_value = int(value)
                    except ValueError:
                        raise ConfigError(f"Line {index}:",
                                          "'SEED' must be an integer")
                    self.values[key] = int_value
                elif key == "ALGORITHM":
                    if value.lower() not in VALID_ALGORITHMS:
                        raise ConfigError(f"Line {index}:",
                                          f"invalid algorithm '{value}'")
                    self.values[key] = value.lower()
                elif key == "DISPLAY_MODE":
                    if value.upper() not in VALID_DISPLAY_MODES:
                        raise ConfigError(f"Line {index}:",
                                          f"invalid display mode '{value}'")
                    self.values[key] = value.upper()

    def validate(self) -> None:
        required_keys = {"WIDTH", "HEIGHT", "ENTRY", "EXIT",
                         "OUTPUT_FILE", "PERFECT"}
        missing_keys = required_keys - self.values.keys()
        if missing_keys:
            raise ConfigError("Missing required keys:",
                              f"{', '.join(missing_keys)}")
        if self.values["ENTRY"] == self.values["EXIT"]:
            raise ConfigError("ENTRY and EXIT must be different")
        x_entry, y_entry = self.values["ENTRY"]
        x_exit, y_exit = self.values["EXIT"]
        if not (0 <= x_entry < self.values["WIDTH"]
                and 0 <= y_entry < self.values["HEIGHT"]):
            raise ConfigError("ENTRY coordinates out of bounds")
        if not (0 <= x_exit < self.values["WIDTH"]
                and 0 <= y_exit < self.values["HEIGHT"]):
            raise ConfigError("EXIT coordinates out of bounds")
        if "WIDTH" in self.values and "HEIGHT" in self.values:
            if self.values["WIDTH"] < 5 or self.values["HEIGHT"] < 5:
                raise ConfigError("'WIDTH' and 'HEIGHT' must be at least 5")
            if self.values["WIDTH"] > 1000 or self.values["HEIGHT"] > 1000:
                raise ConfigError("'WIDTH' and 'HEIGHT' must not exceed 1000")
        output_file = self.values.get("OUTPUT_FILE", "")
        if not output_file.endswith(".txt"):
            raise ConfigError("OUTPUT_FILE must end with '.txt'")

    def get_values(self) -> Config:
        return Config(
            width=self.values["WIDTH"],
            height=self.values["HEIGHT"],
            entry=self.values["ENTRY"],
            exit=self.values["EXIT"],
            output_file=self.values["OUTPUT_FILE"],
            perfect=self.values["PERFECT"],
            seed=self.values.get("SEED"),
            algorithm=self.values.get("ALGORITHM"),
            display_mode=self.values.get("DISPLAY_MODE"),
        )
