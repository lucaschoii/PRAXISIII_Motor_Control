# SPDX-FileCopyrightText: 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
from digitalio import DigitalInOut, Direction
import analogio
import math


# direction and step pins as outputs
DIR1 = DigitalInOut(board.GP16)
DIR1.direction = Direction.OUTPUT
STEP1 = DigitalInOut(board.GP17)
STEP1.direction = Direction.OUTPUT

DIR2 = DigitalInOut(board.GP15)
DIR2.direction = Direction.OUTPUT
STEP2 = DigitalInOut(board.GP14)
STEP2.direction = Direction.OUTPUT

fsr = analogio.AnalogIn(board.A2)  # GP28 = A2 in CircuitPython
def function(x):
    return 1.7321 * math.exp(0.0524 * x + 4.1219) - 127.227


# microstep mode, default is 1/16 so 16
# another ex: 1/4 microstep would be 4
microMode = 16
# full rotation multiplied by the microstep divider
steps = 40 * microMode

num = 10
DIR1.value = True

DIR2.value = False

while True:
    sum = 0

    # take average of {{ num }} readings over 1 second
    for i in range(num):
        sum += fsr.value
        time.sleep(0.05 / num)

    mass_grams = function(sum / num / 64)


    print(mass_grams)
    if (mass_grams < 500):
        for i in range(steps):
            STEP1.value = True
            STEP2.value = True
            time.sleep(0.001)
            STEP1.value = False
            STEP2.value = False
            time.sleep(0.001)


    else:
        print('Too heavy')



