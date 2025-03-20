import time
import board
from digitalio import DigitalInOut, Direction
import analogio
import math

class ForceSensor:
    def __init__(self, num = 10):
        fsr = analogio.AnalogIn(board.A2)  # GP28 = A2 in CircuitPython
        self.num = num

    def calibrate(self, x):
        return 1.7321 * math.exp(0.0524 * x + 4.1219) - 127.227
    
    def read_force(self):
        sum = 0

        # take average of {{ num }} readings over 1 second
        for i in range(self.num):
            sum += self.fsr.value
            time.sleep(0.05 / self.num)

        return function(sum / self.num / 64)