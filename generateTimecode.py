# !/usr/bin/env python3


__version__ = "1.2.0"

import argparse
import socket


parser = argparse.ArgumentParser()
parser.add_argument(
    "-r",
    "--frameRate",
    help="The framerate for the current tiemcode generator",
    action="store",
    choices=["24", "25", "29.97", "29.97d", "30", "30d"],
    default="30",
)
parser.add_argument(
    "-d",
    "--destination",
    help="The destination IP address or hostname",
    action="store",
    default="localhost",
)
parser.add_argument(
    "-p", "--port", help="The destination port number", action="store", default=32830
)

args = parser.parse_args()

print(args)


class Timecode(object):
    def __init__(self):
        print("open for business")


if __name__ == "__main__":
    a = Timecode()
