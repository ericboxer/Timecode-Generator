# Python Timecode Generator

A simple python script to generate timecode and spit it out over UDP in a pseudo MTC format

## Usage

Help

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
