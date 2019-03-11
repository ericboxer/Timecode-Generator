# Python Timecode Generator

A simple python script to generate timecode and spit it out over UDP in a pseudo MTC format

## Installation

Nothing fancy here. You should probably have [Python 3][1] (3.7+) installed.  
I recommend using a virtual environment. If you want to feel fancy use [Pipenv][2]:

```bash
pipenv install
```

## A note about MTC and quarter frames

While this format is strangely familiar to [MTC][3] it only uses the full frame format. I can't take credit though. This was meant to work with a [KISSBOX TC2TR][4].

Essentially you can send the output directly to the unit and it will generate an LTC timecode output.

Because of the speed and bandwidth at which even a slow network works the need for quarter frames is not needed.

## Usage

Getting help

```bash
python3 generateTimecode.py -h

usage: generateTimecode.py [-h] [-f STARTFRAME] [-r {24,25,30}] [-e ENDFRAME]
                           [-R] [-a IPADDRESS] [-p PORT]

optional arguments:
  -h, --help            show this help message and exit

Timecode:
  -f STARTFRAME, --startFrame STARTFRAME
                        The frame to start on
  -r {24,25,30}, --framerate {24,25,30}
                        what framerate to use
  -e ENDFRAME, --endFrame ENDFRAME
                        The last frame in the timecode sequence
  -R, --rollover        Determines if the code should rollover when end frame
                        is hit

IP:
  -a IPADDRESS, --ipAddress IPADDRESS
                        The IP Address to send to. Defaults to localhost
  -p PORT, --port PORT  The port to send to.

```

Just start rolling code from 0 at 30 frames

```bash
python3 generateTimecode.py
# 00 00 00 00
# 0
# ---
```

Start at a specific frame

```bash
python3 generateTimecode.py -f 400
# 00 00 13 10
# 400
# ---
```

[1]: https://www.python.org/downloads/
[2]: https://pipenv.readthedocs.io/en/latest/
[3]: https://bxhd.me/2UtcYr9
[4]: https://bxhd.me/2UtFRU3
