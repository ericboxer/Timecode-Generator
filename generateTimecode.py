#!/usr/bin/env python3

"""
Sends an MTC packet of timecode to a given address.
MTC calculated based on https://en.wikipedia.org/wiki/MIDI_timecode
Qurater-frames are not handled.
"""

__version__ = "0.2.1"


import argparse
import math
import time


# Handle the arguments
parser = argparse.ArgumentParser()
timecodeArgs = parser.add_argument_group("Timecode")
ipArgs = parser.add_argument_group("IP")
timecodeArgs.add_argument(
    "-f",
    "--startFrame",
    type=int,
    help="The frame to start on",
    action="store",
    default=0,
)
timecodeArgs.add_argument(
    "-r",
    "--framerate",
    type=int,
    help="what framerate to use",
    action="store",
    choices=[24, 25, 30],
    default=30,
)

timecodeArgs.add_argument(
    "-e",
    "--endFrame",
    type=int,
    help="The last frame in the timecode sequence",
    action="store",
    default=None,
)

timecodeArgs.add_argument(
    "-R",
    "--rollover",
    help="Determines if the code should rollover when end frame is hit",
    action="store_true",
    default=False,
)


ipArgs.add_argument(
    "-a",
    "--ipAddress",
    help="The IP Address to send to. Defaults to localhost",
    action="store",
    default="127.0.0.1",
)

ipArgs.add_argument(
    "-p", "--port", help="The port to send to.", action="store", default=5005
)
args = parser.parse_args()


# TODO: Might want to make this a class so its easier to work with

# Now that we've got our arguments sorted lets do something with them
frame = args.startFrame
frameRate = args.framerate

# If the end frame is set use that othewise use the calculated end of the 24 hours
# TODO: Set a check to make sure this falls within an actual usable range...
endFrame = args.endFrame if args.endFrame else (frameRate * 60 * 60 * 24)

mtcPacket = [
    0xF0,  # Message Start
    0x7F,  # Universal Message
    0x7F,  # Global Broadcast
    0x01,  # Timecode Message
    0b11,  # Framerate (though the article says this indicates a full-frame message...)
    0x00,  # Hours
    0x00,  # Minutes
    0x00,  # Seconds
    0x00,  # Frames
    0xF7,  # EoE message
]


def incrementFrame():
    """
    Increments the current frame.
    It's a hard job, but someone needs to do it...
    """

    global frame
    frame += 1


# TODO: Decide on a better name for the function
def frameToTime(frames, framerate, showCode=False):
    """Converts the current frame to time based on the selected framerate
    
    Arguments:
        frames {int} -- The frame to be coverted
        framerate {int} -- the framerate to be used
    
    Keyword Arguments:
        showCode {bool} -- Prints the data to the screen. (default: {False})
    
    Returns:
        list -- THe final packet data
    """

    packet = mtcPacket
    second = round(frameRate)
    minute = second * 60
    hour = minute * 60

    # Set the framerate byte. Defaults to 30
    if framerate == 24:
        fr = 0b00
    elif framerate == 25:
        fr = 0b01
    # TODO: Make dropframe math more gooder
    # 29.97 Needs a bit more work to actually be correct
    # elif framerate == 29.97:
    #     fr = 0b10
    #     frames = round(frames * 1.001)  # Adjust framerate
    else:
        fr = 0b11
    hours = math.floor(frames / hour)
    minFrames = frames - (hour * hours)
    minutes = math.floor(minFrames / minute)
    secFrames = minFrames - (minute * minutes)
    seconds = math.floor(secFrames / second)
    frameFrames = secFrames - (second * seconds)
    if showCode == True:
        # TODO: F-string this for clarity
        print(
            str(hours).zfill(2),
            str(minutes).zfill(2),
            str(seconds).zfill(2),
            str(frameFrames).zfill(2),
        )
        print(frames)

    packet[4] = fr
    packet[5] = hours
    packet[6] = minutes
    packet[7] = seconds
    packet[8] = frameFrames

    return packet


if __name__ == "__main__":
    import socket

    # Send the data over UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        # s.sendto(bytearray(frameToTime(frame, frameRate, True)), ("10.0.1.201", 5007))
        s.sendto(
            bytearray(frameToTime(frame, frameRate, True)), (args.ipAddress, args.port)
        )
        print("---")

        if frame == endFrame:
            if args.rollover:
                frame = args.startFrame
                print("Rollover")
                print("---")
            else:
                print("Fisnished Rolling Code")
                exit(0)
        now = time.time()
        # time.sleep() is too slow. Genereate speed based off of the frameRate
        while True:
            newNow = time.time()
            if newNow >= now + 1 / frameRate:
                break
        incrementFrame()

