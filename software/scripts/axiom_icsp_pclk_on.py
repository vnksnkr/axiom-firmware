#!/bin/env python3

import sys
import serial
import struct
import string
import random

from smbus import SMBus
from time import sleep
from axiom_icsp import *


tty = "/dev/ttyPS1"
ser = serial.Serial(
    port = tty,
    baudrate = 10000000,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    # interCharTimeout = 0.2,
    timeout = 1.0,
    xonxoff = False,
    rtscts = False,
    dsrdtr = False);

print(icsp_cmd(ser, b'#', 9))
print(icsp_cmd(ser, b'>', 1))
print(icsp_cmd(ser, b'P', 2))
print(icsp_cmd(ser, b'#', 9))


