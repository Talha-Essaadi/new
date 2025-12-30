#!/usr/bin/env python3
from typing import Tuple

class Stack:
    """
    Docstring for Stack
    """
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> None:
        if not self.is_empty():
            self.items.pop()

    def peek(self) -> Tuple[int, int]:
        print(f"Peeking stack: {self.items}")
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self) -> bool:
        return len(self.items) == 0