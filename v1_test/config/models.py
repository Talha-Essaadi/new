#!/usr/bin/env python3

from typing import Tuple, Optional


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
            seed: Optional[int] = None,
            algorithm: Optional[str] = None,
            display_mode: Optional[str] = None

    ) -> None:
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self. perfect = perfect
        self.seed = seed
        self.algorithm = algorithm
        self.display_mode = display_mode
