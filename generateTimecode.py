# !/usr/bin/env python3


__version__ = "1.2.0"

import argparse
import sys

# Move socket call inside of class
import socket


print(sys.version_info)

# Lets setup all of our command line stuffs here...
parser = argparse.ArgumentParser()
timecodeDataGroup = parser.add_argument_group("Timecode Settings", "Timecode Settings")
timecodeDataGroup.add_argument(
    "-r",
    "--framerate",
    help="The framerate for the current tiemcode generator",
    action="store",
    # choices=["24", "25", "29.97", "30"],
    choices=[24, 25, 29.97, 30],
    default=30,
)

timecodeDataGroup.add_argument(
    "-d",
    "--dropframe",
    help="Determines if a dropframe should be used",
    action="store_true",
    default=False,
)


outboundDataGroup = parser.add_argument_group("IP Settings", "IP and Port Settings")
outboundDataGroup.add_argument(
    "-D",
    "--destination",
    help="The destination IP address or hostname",
    action="store",
    default="localhost",
)
outboundDataGroup.add_argument(
    "-p", "--port", help="The destination port number", action="store", default=32830
)

startPoint = timecodeDataGroup.add_mutually_exclusive_group()
startPoint.add_argument(
    "-f", "--startFrame", help="The SMPTE frame to start from", action="store"
)
startPoint.add_argument(
    "-t", "--startTime", help="The SMPTE time to start from", action="store"
)

args = parser.parse_args()

print(args)


class Subtime(object):
    def __init__(self):
        import time

        self._millis = int(round(time.time() * 1000, 4))


class TcTime(object):
    def __init__(
        self,
        hours: int = None,
        minutes: int = None,
        seconds: int = None,
        frames: int = None,
        framerate: int = 30,
        dropframe: bool = False,
    ):
        pass

    def toFrames(self) -> int:

        return 0


class Timecode(object):
    def __init__(
        self, startFrame: int = 0, framerate: int = 30, dropframe: bool = False
    ):
        self._startFrame = startFrame
        self._framerate = framerate
        self._dropframe = dropframe
        self._currentFrame = startFrame

        self._mtcPacket = [
            0xF0,
            0x7F,
            0x7F,
            0x01,
            0b11,
            0x01,
            0x02,
            0x03,
            0x04,
            0xF7,
        ]  # the base packet to work from

        self._running = True
        self._active()
        ## End __init__

    @property
    def startFrame(self) -> int:
        return self._startFrame

    @startFrame.setter
    def startFrame(self, value: int):
        self._startFrame = value

    @property
    def framerate(self):
        return f"{self._framerate}{'d' if self._dropframe else ''}"

    def reset(self):
        """
        Resets to the start frame
        """
        self._currentFrame = self._startFrame

    def _active(self):
        while True:
            if self._running:
                
            print(self._currentFrame)


if __name__ == "__main__":
    a = Timecode(startFrame=16000, dropframe=True)
    print(a.framerate)
    print(a.startFrame)
    print(a._currentFrame)
    a.startFrame = 35
    print(a.startFrame)
    a.reset()
    print(a._currentFrame)
