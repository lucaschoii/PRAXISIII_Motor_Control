import time
import board
import analogio
import math

class ForceSensor:
    def __init__(self, threshold = 500, num = 10):
        self.fsr = analogio.AnalogIn(board.A2)  # GP28 = A2 in CircuitPython
        self.num = num
        self.threshold = threshold

    def _calibrate(self, x):
        return 1.7321 * math.exp(0.0524 * x + 4.1219) - 127.227
    
    def _read_force(self):
        sum = 0

        # take average of {{ num }} readings over ~0.05 seconds
        for _ in range(self.num):
            sum += self.fsr.value
            time.sleep(0.05 / self.num)

        return self._calibrate(sum / self.num / 64)
    
    def interrupt(self):
        mass_grams = self._read_force()
        if (mass_grams < self.threshold):
            return False
        else:
            return True