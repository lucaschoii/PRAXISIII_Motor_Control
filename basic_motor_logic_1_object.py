from Motor import Motor
from ForceSensor import ForceSensor

operation_stack = []
    
motor = Motor()
force_sensor = ForceSensor()


while True:
    
    if (not force_sensor.interrupt()):
        motor.move()

    else:
        
        print('Too heavy, avoiding object...')

        operation_stack.append('RR')
        motor.reverse()   
        motor.tank_right()
        motor.forward()
        motor.tank_left()
        motor.forward()
        motor.tank_left()
        motor.forward()
        motor.tank_right()
        motor.forward()

        
        




        






