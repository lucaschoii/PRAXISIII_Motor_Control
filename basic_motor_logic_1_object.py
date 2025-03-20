import time
import board
from digitalio import DigitalInOut, Direction
import analogio
import math
from Motor import Motor
from ForceSensor import ForceSensor

operation_stack = []
    
motor = Motor()
force_sensor = ForceSensor()


while True:
    mass_grams = force_sensor.read_force()

    print(mass_grams)
    if (mass_grams < 500):
        motor.move()

    else:
        print('Too heavy, avoiding object...')
        motor.reverse()   
        motor.tank_right()
        motor.forward()
        motor.tank_left()
        motor.forward()
        motor.tank_left()
        motor.forward()
        motor.tank_right()
        motor.forward()
        




        






