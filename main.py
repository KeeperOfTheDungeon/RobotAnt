#!/usr/bin/env python
import argparse

from ant import Ant
from AntView.AntView import AntView


def main(do_gui: bool, do_cli: bool):
    ant = Ant()
    if do_gui:
        _ant_viewer = AntView(ant)
    if do_cli:
        ant.run()


def parse_args():
    parser = argparse.ArgumentParser(description='GUI/CLI for the Ant robot from HsKa.')
    parser.add_argument('--gui', action=argparse.BooleanOptionalAction)
    parser.add_argument('--cli', action=argparse.BooleanOptionalAction)
    parser.set_defaults(gui=True, cli=False)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.gui, args.cli)
    print("Shutting down!")
