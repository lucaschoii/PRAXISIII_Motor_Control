import time
import board
from digitalio import DigitalInOut, Direction
import analogio
import math
from Motor import Motor
from ForceSensor import ForceSensor

motor = Motor()
force_sensor = ForceSensor()

obstacles = []


def hit(action, times = 1):

    for _ in range(times):
        action()

        if force_sensor.interrupt():
            print("New obstacle detected!")
            return True 
     
    return False  


while True:
    
    if (not force_sensor.interrupt()):
        motor.move()

    else:
        
        print("Obstacle detected! Avoiding...")

        if len(obstacles) == 0:
            motor.reverse()
            motor.tank_right()
            if hit(motor.forward): 
                obstacles.append('object')
                continue
            motor.tank_left()
            if hit(motor.forward, 2):
                obstacles.append('fence')
                continue
            motor.tank_left()
            if hit(motor.forward):
                motor.tank_right()
                continue
            motor.tank_right()

        
        elif obstacles[-1] == 'object':
            print("Second obstacle detected! Adjusting route...")
            motor.reverse()
            motor.tank_right()

            # no way there is another object in the way 
            # this would mean we were boxed in and we would not 
            # have gotten here in the first place skull emoji
            motor.forward()
            motor.tank_left()

            # if hit, this is likely a corner and we should just go back the other way
            if hit(motor.forward, 2): 
                obstacles.clear()
                motor.tank_right()
                continue
            motor.tank_left()

            
            if hit(motor.forward, 2): 
                obstacles.append('fence')
                continue

            motor.tank_left()
            if hit(motor.forward): 
                motor.tank_right()
                continue

            # at this point, we have cleared the latest object
            obstacles.pop()
            motor.tank_right()

            if hit(motor.forward): 
                obstacles.append('object')
                continue

            motor.tank_left()
            if hit(motor.forward): 
                obstacles.append('fence')
                continue

            motor.tank_right()
            #now we have cleared the previous object as well
            obstacles.pop()
            continue

        elif obstacles[-1] == 'fence':  # If we hit the same object twice -> fence detected
            print("Fence detected! Reversing direction...")
            motor.reverse()
            motor.tank_right()
            motor.tank_right()
            obstacles.clear() # do not care about other objects now, just go back the other way


        






