import argparse
from dataclasses import dataclass
from importlib import metadata
from os import path
from sys import argv

try:
    import argcomplete

    comp = True
except ImportError:
    comp = False
try:
    from rich_argparse import HelpPreviewAction, RichHelpFormatter

    colourful = True
except ImportError:
    colourful = False


@dataclass
class CliArgs:
    directory: bool
    file: bool
    ordered: bool

    @property
    def all(self) -> bool:
        return self.file and self.directory

    @all.setter
    def all(self, value: bool) -> None:
        self.file = value
        self.directory = value

    def __init__(self, directory: bool, file: bool, ordered: bool, all: bool) -> None:
        self.directory = directory
        self.file = file
        self.ordered = ordered
        if all:
            self.all = all


def get_args() -> CliArgs:
    prog_name = path.basename(path.dirname(__file__))
    if colourful:
        parser = argparse.ArgumentParser(
            prog=prog_name, formatter_class=RichHelpFormatter
        )
    else:
        parser = argparse.ArgumentParser(prog=prog_name)

    type_options = parser.add_argument_group("Type")
    type_options.add_argument(
        "-f",
        "--file",
        dest="file",
        action="store_true",
        default=False,
        help="list files",
    )
    type_options.add_argument(
        "-d",
        "--dir",
        "--directory",
        dest="directory",
        action="store_true",
        default=False,
        help="list directories",
    )
    type_options.add_argument(
        "-a",
        "--all",
        dest="all",
        action="store_true",
        default=False,
        help="list files and directories",
    )

    appearance_options = parser.add_argument_group("Appearance")
    appearance_options.add_argument(
        "-s",
        "--sorted",
        dest="ordered",
        action="store_true",
        default=False,
        help="sort in descending order",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{prog_name} v{metadata.version(prog_name)}",
    )

    if colourful:
        if "--make-help-preview" in argv:
            parser.add_argument(
                "--make-help-preview",
                action=HelpPreviewAction,
                path=f".{path.sep}img{path.sep}help.svg",
            )

    if comp:
        argcomplete.autocomplete(parser)

    return CliArgs(**vars(parser.parse_args()))
