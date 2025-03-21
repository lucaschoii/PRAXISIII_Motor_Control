import time
import board
from digitalio import DigitalInOut, Direction

class Motor:
    def __init__(self):
        
        # microstep mode, default is 1/16 so 16
        # another ex: 1/4 microstep would be 4
        self.microMode = 16
        self.steps = 40 * self.microMode
        
        # direction and step pins as outputs
        self.DIR_RIGHT = DigitalInOut(board.GP16)
        self.DIR_RIGHT.direction = Direction.OUTPUT
        self.STEP_RIGHT = DigitalInOut(board.GP17)
        self.STEP_RIGHT.direction = Direction.OUTPUT

        self.DIR_LEFT = DigitalInOut(board.GP15)
        self.DIR_LEFT.direction = Direction.OUTPUT
        self.STEP_LEFT = DigitalInOut(board.GP14)
        self.STEP_LEFT.direction = Direction.OUTPUT

        self.DIR_RIGHT.value = True
        self.DIR_LEFT.value = True

    def _move(self, steps=None):

        if not steps:
            steps = self.steps
        else:
            steps = steps * self.microMode

        for _ in range(steps):
            self.STEP_LEFT.value = True
            self.STEP_RIGHT.value = True
            time.sleep(0.001)
            self.STEP_LEFT.value = False
            self.STEP_RIGHT.value = False
            time.sleep(0.001)

    def stop(self):
        self.STEP_LEFT.value = False
        self.STEP_RIGHT.value = False
        time.sleep(0.05)

    def forward(self):
        self.DIR_RIGHT.value = True
        self.DIR_LEFT.value = True
        time.sleep(0.05)
        self._move(1)

    def reverse(self):
        self.DIR_RIGHT.value = False
        self.DIR_LEFT.value = False
        time.sleep(0.05)
        self._move(0.5)

    def tank_left(self):
        self.DIR_RIGHT.value = True
        self.DIR_LEFT.value = False
        self._move(1)

    def tank_right(self):
        self.DIR_RIGHT.value = False
        self.DIR_LEFT.value = True
        self._move(1)
