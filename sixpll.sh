#!/usr/bin/python
# Tool for bg7tbl 6-PLL
# written 2021 by Ralf Jardon
# cosmicos at gmx.net
#
# License: GPLv3
#

import sys
import argparse
from bg7tbl import SixPLL
from serial import SerialException

# first USB-Port in Linux
PORT = "/dev/ttyUSB0"
parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", default=PORT, type=str, help="Serial port where 6-PLL is connected")
parser.add_argument("-l", "--list", help="List frequencies from EEPROM", action="store_true")
parser.add_argument("-w", "--write", help="Write frequency to EEPROM. Format: OUT1:010000000", type=str)
args = parser.parse_args()

print("BG7TBL 6-PLL tool")

try:
    if args.port:
        port = args.port
    else:
        port = PORT

# write frequency to EEPROM else read and print frequencies from EEPROM
    if args.write:
        myPLL = SixPLL(port, args.write)
        myPLL.write()
        myPLL.print()
    else:
        if args.list:
            myPLL = SixPLL(port, args.write)
            myPLL.print()

    while True:
        sys.exit()

except SerialException:
    print('Serial port error!')

except KeyboardInterrupt:
    print('Aborting!')
    sys.exit()
