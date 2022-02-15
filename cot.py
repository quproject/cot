#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cot, a simple, fast, leightweight and easy to use
colors toolbox for designers and developers.
"""

import sys
import os

from typing import Any
import argparse

from cotlib import colors


# App version
__author__  = "idealtitude"
__version__ = "0.1.0"
__license__ = "MT108"

# Constants
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
APP_PATH = os.path.dirname(os.path.realpath(__file__))
APP_CWD = os.getcwd()


# Command line arguments
def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="", description="", epilog="Help and documentation at https://github.com/quproject/cot"
    )

    parser.add_argument("action", nargs='?', help="Action to perform: color picker, colors contrast")
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    return parser.parse_args()


# Entry point
def main() -> int:
    """Entry point, main function."""
    args: argparse.Namespace = get_args()

    if args.action:
        color = colors.Color(args.action)
        print(color.color.color_datas.color_string)
        if color.color.color_datas.color_format is not None:
            print(color.color.color_datas.color_format)
            print(color.color.color_datas.components)
        else:
            print(f"Can't recognize color string format: {args.action}; exit...")
            return EXIT_FAILURE
    else:
        print("No argument provided...")

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
