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


def hit(action):
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
            if hit(motor.tank_left): continue
            if hit(motor.forward): continue
        
        elif obstacles[-1] == 'object':
            print("Second obstacle detected! Adjusting route...")
            motor.reverse()
            motor.tank_right()

            # no way there is another object in the way 
            # this would mean we were boxed in and we would not 
            # have gotten here in the first place skull emoji
            motor.forward()
            motor.tank_left()
            if hit(motor.forward): 
                obstacles.append('fence')
                continue
            motor.tank_left()
            if hit(motor.forward): 
                obstacles.append('fence')
                continue
            motor.tank_left()
            if hit(motor.forward): 
                obstacles.append('fence')
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


        






