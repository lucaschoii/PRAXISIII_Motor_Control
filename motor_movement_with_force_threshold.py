# SPDX-FileCopyrightText: 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
from digitalio import DigitalInOut, Direction
import analogio
import math


# direction and step pins as outputs
DIR = DigitalInOut(board.GP16)
DIR.direction = Direction.OUTPUT
STEP = DigitalInOut(board.GP17)
STEP.direction = Direction.OUTPUT

fsr = analogio.AnalogIn(board.A2)  # GP28 = A2 in CircuitPython
def function(x):
    return 1.7321 * math.exp(0.0524 * x + 4.1219) - 127.227


# microstep mode, default is 1/16 so 16
# another ex: 1/4 microstep would be 4
microMode = 16
# full rotation multiplied by the microstep divider
steps = 40 * microMode

num = 10

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
            STEP.value = True
            time.sleep(0.001)
            STEP.value = False
            time.sleep(0.001)


    else:
        print('Too heavy')

