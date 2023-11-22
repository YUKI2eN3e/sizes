from dataclasses import dataclass
from functools import total_ordering
from os import path

from sizes._util import has_var
from sizes.colours import Colours
from sizes.utils import convert_size


@total_ordering
@dataclass
class File:
    size: int
    name: str

    def __repr__(self) -> str:
        size_str = convert_size(self.size)
        size_colour = (
            Colours.LIGHT_RED
            if "G" in size_str
            else (
                Colours.YELLOW
                if "M" in size_str
                else (Colours.LIGHT_GREEN if "K" in size_str else Colours.LIGHT_BLUE)
            )
        )
        indent = "\t\t" if len(size_str) < 8 else "\t"
        name_colour = (
            Colours.DARK_GRAY
            if list(self.name.split(path.sep)[-1])[0] == "."
            else Colours.BOLD
        )
        return f"{size_colour}{size_str}{Colours.RESET}{indent}{name_colour}{self.name}{Colours.RESET}"

    def __eq__(self, other: object) -> bool:
        if has_var(other, "size"):
            return self.size == other.size  # type: ignore
        else:
            raise TypeError

    def __lt__(self, other: object) -> bool:
        if has_var(other, "size"):
            return self.size < other.size  # type: ignore
        else:
            raise TypeError
