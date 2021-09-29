# BG7TBL 10M-6-PLL
Linux tool (command line and GUI) to program the 6-Channel Frequency Adjustable Conversion Board from BG7TBL

Usage:

ralf@T3610:~/PycharmProjects/bg7tpl$ ./sixpll.sh -h
usage: sixpll.sh [-h] [-p PORT] [-l] [-w WRITE] [-g]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial port where 6-PLL is connected
  -l, --list            List frequencies from EEPROM
  -w WRITE, --write WRITE
                        Write frequency to EEPROM. Format: OUT1:010000000
  -g, --gui             Graphical User Interface

Change one frequency:
---------------------
./sixpll.sh -w OUT1:010000000

List frequenies:
----------------
./sixpll.sh -l

Change multiple frequencies:
----------------------------
./sixpll.sh -g
