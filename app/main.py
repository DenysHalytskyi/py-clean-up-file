import os
import traceback
from typing import Optional, Type


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[traceback]) -> None:
        if exc_type is not None:
            print(f"Виникло виключення: {exc_type}, {exc_val}")

        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"Файл {self.filename} був видалений.")
