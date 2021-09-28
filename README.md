# BG7TBL-6-PLL
Linux command line tool to program the 6-Channel Frequency Adjustable Conversion Board from BG7TBL

Usage:

./sixpll.sh -h

usage: sixpll.sh [-h] [-p PORT] [-l] [-w WRITE]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial port where 6-PLL is connected
  -l, --list            List frequencies from EEPROM
  -w WRITE, --write WRITE
                        Write frequency to EEPROM. Format: OUT1:010000000


EXAMPLE: List all frequencies:

./sixpll.sh -l

BG7TPL 6-PLL tool
Frequencies stored in EEPROM
----------------------------
PLL   Mhz kHz Hz
OUT1: 010.000.000Hz
OUT2: 020.000.000Hz
OUT3: 030.000.000Hz
OUT4: 040.000.000Hz
OUT5: 050.000.000Hz
OUT6: 060.000.000Hz

That's it...
Port closed

EXAMPLE: Write a frequency

./sixpll.sh -w OUT1:016000000

BG7TPL 6-PLL tool

Writing frequencies to EEPROM
-----------------------------
WRITE: OUT1: 016000000
WRITE: OUT2: 020000000
WRITE: OUT3: 030000000
WRITE: OUT4: 040000000
WRITE: OUT5: 050000000
WRITE: OUT6: 060000000

Frequencies stored in EEPROM
----------------------------
PLL   Mhz kHz Hz
OUT1: 016.000.000Hz
OUT2: 020.000.000Hz
OUT3: 030.000.000Hz
OUT4: 040.000.000Hz
OUT5: 050.000.000Hz
OUT6: 060.000.000Hz

That's it...
Port closed

