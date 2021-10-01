# BG7TBL 10M-6-PLL
Linux tool (command line and GUI) to program the 6-Channel Frequency Adjustable Conversion Board from BG7TBL.

Usage:
------
sixpll.sh [-h] [-p PORT] [-l] [-w WRITE] [-g]

optional arguments:

-h, --help            show this help message and exit

-p PORT, --port PORT  Serial port where 6-PLL is connected

-l, --list            List frequencies from EEPROM

-w WRITE, --write WRITE Write frequency to EEPROM. Format: OUT1:010000000

GUI support at master branch only!
----------------------------------
-g, --gui             Graphical User Interface

List frequenies:
----------------
./sixpll.sh -l

Change a frequency:
---------------------
./sixpll.sh -w OUT1:010000000

Change multiple frequencies:
----------------------------
./sixpll.sh -g
