# Class for bg7tbl 6-PLL
# written 2021 by Ralf Jardon
# cosmicos at gmx.net
#
# License: GPLv3
#
import sys
import serial   # pySerial!

# Serial port settings for 6-PLL
BAUD_RATE = 9600
BITS = serial.EIGHTBITS
PARITY = serial.PARITY_NONE
STOP_BITS = serial.STOPBITS_ONE
TIMEOUT = 1

# End of line signature
EOL = b'\x0D\x0A'

# Command to let 6-PLL send its frequency values stored in EEPROM
READ_CMD = b'\x24\x52\x44\x2A'

# Command to let 6-PLL await new frequencies
WRITE_CMD = b'\x24\x57\x45'

# Separator between frequencies while write to EEPROM
SEPARATOR = b'\x2C'

# End Of Data signature after after writing six frequencies to EEPROM
EOD = b'\x2a'

# Length of data block for each frequency
# Format is: 'OUT1:010000000\CR\LF'
RAW_DATA_LENGTH = 16

# 6 Channels in 6-PLL (OUT1... OUT6)
CHANNELS = 6


class SixPLL(object):
    def __init__(self, port, frequency):
        self.port = port
        self.frequency = frequency
        self.ser = serial.Serial(self.port, BAUD_RATE, BITS, PARITY, STOP_BITS, TIMEOUT)
        self.ser.setDTR(True)
        self.ser.setRTS(False)
        self.sixpllDict = {}

    def write(self):
        if self.is_data_valid(self.frequency):
            print("Writing frequencies to EEPROM")
            print("-----------------------------")
        else:
            print("Channel or Frequency mismatch. Aborting...")
            sys.exit(1)

        self.__sendReadCmd__()
        # filling dictionary
        for c in "OUT1:", "OUT2:", "OUT3:", "OUT4:", "OUT5:", "OUT6:":
            rawdata = self.ser.read_until(EOL, RAW_DATA_LENGTH)
            rawstr = str(rawdata)[2:RAW_DATA_LENGTH]
            if rawstr[0:5] == self.frequency[0:5]:
                print("NEW: " + self.frequency)
                item = {c: self.frequency[5:14]}
                self.sixpllDict.update(item)
            else:
                item = {c: rawstr[5:14]}
                self.sixpllDict.update(item)

        self.__sendWriteCmd__()
        # program EEPROM
        for key, value in self.sixpllDict.items():
            valuebytes = bytes(value, encoding='utf-8')
            self.ser.write(valuebytes)
            self.ser.write(SEPARATOR)
        self.ser.write(EOD)
        print()

    def print(self):
        self.__sendReadCmd__()
        print("Frequencies stored in EEPROM")
        print("----------------------------")
        print("PLL   Mhz kHz Hz")
        c = 0
        while c < CHANNELS:
            rawdata = self.ser.read_until(EOL, RAW_DATA_LENGTH)
            rawstr = str(rawdata)[2:RAW_DATA_LENGTH]
            print(rawstr[0:5] + " " + rawstr[5:8] + "." + rawstr[8:11] + "." + rawstr[11:] + "Hz")
            c = c+1
        print()
        print("That's it...")

    def __sendReadCmd__(self):
        self.ser.reset_input_buffer()
        self.ser.write(READ_CMD)

    def __sendWriteCmd__(self):
        self.ser.reset_output_buffer()
        self.ser.write(WRITE_CMD)

    def is_data_valid(self, raw_data):
        # check data length
        if len(raw_data) != RAW_DATA_LENGTH-2:
            return False

        # check channel descriptor
        if raw_data[0:3] != 'OUT' or raw_data[4] != ':':
            return False

        # check Frequency
        if not raw_data[5:].isdecimal():
            return False

        return True

    def __del__(self):
        if hasattr(self, 'ser'):
            self.ser.close()
            print("Port closed")
