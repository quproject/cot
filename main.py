#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-

"""
Documentation, main docstring
"""

import sys
import os

from typing import Any
import argparse


# App version
__author__  = "idealtitude"
__version__ = "0.1.0"
__license__ = "ISC"

# Constants
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
APP_PATH = os.path.dirname(os.path.realpath(__file__))
APP_CWD = os.getcwd()


def fictive_function(num: int) -> bool:
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    num : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    """
    pass


# Command line arguments
def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="", description="", epilog="Help and documentation at "
    )

    parser.add_argument("", nargs=1, help="")
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    return parser.parse_args()


# Entry point
def main(args: list[str]) -> int:
    """Entry point, main function."""
    print(args)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main(sys.argv))
