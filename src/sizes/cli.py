import argparse
from dataclasses import dataclass
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


def get_args() -> CliArgs:
    if colourful:
        parser = argparse.ArgumentParser(
            prog="sizes", formatter_class=RichHelpFormatter
        )
    else:
        parser = argparse.ArgumentParser(prog="sizes")

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

    appearance_options = parser.add_argument_group("Appearance")
    appearance_options.add_argument(
        "-s",
        "--sorted",
        dest="ordered",
        action="store_true",
        default=False,
        help="sort from descending order",
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
