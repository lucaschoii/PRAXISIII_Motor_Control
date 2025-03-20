import time
import board
import analogio
import math

fsr = analogio.AnalogIn(board.A2)  # GP28 = A2 in CircuitPython

def function(x):
    return 1.7321 * math.exp(0.0524 * x + 4.1219) - 133.227

num = 100
while True:
    sum = 0

    # take average of {{ num }} readings over 1 second
    for i in range(num):
        sum += fsr.value
        time.sleep(1 / num)

    mass_grams = function(sum / num / 64)

    print(mass_grams)
