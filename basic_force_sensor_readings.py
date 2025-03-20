import time
import board
import analogio

fsr = analogio.AnalogIn(board.A2)  # GP28 = A2 in CircuitPython
num = 100

while True:
    sum = 0

    # take average of {{ num }} readings over 4 seconds
    for i in range(num):
        sum += fsr.value
        time.sleep(4 / num)

    # normalize to values 0 to 1032
    print(sum / num / 64)
