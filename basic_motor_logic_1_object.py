# SPDX-FileCopyrightText: 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
from digitalio import DigitalInOut, Direction
import analogio
import math

operation_stack = []

def move():
    for i in range(steps):
        STEP_LEFT.value = True
        STEP_RIGHT.value = True
        time.sleep(0.001)
        STEP_LEFT.value = False
        STEP_RIGHT.value = False
        time.sleep(0.001)

def stop():
    STEP_LEFT.value = False
    STEP_RIGHT.value = False
    time.sleep(0.05)

def forward():
    DIR_RIGHT.value = True
    DIR_LEFT.value = True
    time.sleep(0.05)
    move()

def reverse():
    DIR_RIGHT.value = False
    DIR_LEFT.value = False
    time.sleep(0.05)
    move()

def tank_left():
    DIR_RIGHT.value = True
    DIR_LEFT.value = False
    move()

def tank_right():
    DIR_RIGHT.value = False
    DIR_LEFT.value = True
    move()

def read_force(num):
    sum = 0

    # take average of {{ num }} readings over 1 second
    for i in range(num):
        sum += fsr.value
        time.sleep(0.05 / num)

    return function(sum / num / 64)

# direction and step pins as outputs
DIR_RIGHT = DigitalInOut(board.GP16)
DIR_RIGHT.direction = Direction.OUTPUT
STEP_RIGHT = DigitalInOut(board.GP17)
STEP_RIGHT.direction = Direction.OUTPUT

DIR_LEFT = DigitalInOut(board.GP15)
DIR_LEFT.direction = Direction.OUTPUT
STEP_LEFT = DigitalInOut(board.GP14)
STEP_LEFT.direction = Direction.OUTPUT

fsr = analogio.AnalogIn(board.A2)  # GP28 = A2 in CircuitPython
def function(x):
    return 1.7321 * math.exp(0.0524 * x + 4.1219) - 127.227


# microstep mode, default is 1/16 so 16
# another ex: 1/4 microstep would be 4
microMode = 16
# full rotation multiplied by the microstep divider
steps = 40 * microMode

num = 10
DIR_RIGHT.value = True
DIR_LEFT.value = True

while True:
    mass_grams = read_force(num)

    print(mass_grams)
    if (mass_grams < 500):
        move()


    else:
        print('Too heavy, avoiding object...')
        reverse()   
        tank_right()
        forward()
        tank_left()
        forward()
        tank_left()
        forward()
        tank_right()
        forward()
        




        






