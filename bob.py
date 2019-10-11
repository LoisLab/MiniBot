from motor_lib import *
import random

class ActionSpace:
    
    actions = [(Motor.FORWARD, Motor.REVERSE, 0.15),
               (Motor.FORWARD, Motor.REVERSE, 0.30),
               (Motor.REVERSE, Motor.FORWARD, 0.15),
               (Motor.REVERSE, Motor.FORWARD, 0.30),
               (Motor.FORWARD, Motor.FORWARD, 0.25),
               (Motor.FORWARD, Motor.FORWARD, 0.50),
               (Motor.REVERSE, Motor.REVERSE, 0.25),
               (Motor.REVERSE, Motor.REVERSE, 0.50)]
             
    def sample():
        return ActionSpace.actions[random.randint(1,len(ActionSpace.actions))]

class Bob:
    
    def __init__(self, speed=1):
        self.action_space = ActionSpace
        self.motors = Motors()
        self.speed = speed
        
    def step(self, action):
        print(action)
        self.motors.set_direction(action[0],action[1])
        self.motors.go()
        sleep(action[2]*self.speed)
        self.motors.stop()
        
    def listen(self, message):
        tokens = message.split('=')
        if len(tokens)==2 and tokens[0]=='action':
            self.step(ActionSpace.actions[int(tokens[1])])
        elif len(tokens)==2 and tokens[0]=='speed':
            self.speed = float(tokens[1])
            print('speed set to:', self.speed)
        else:
            raise ValueError('Unknown command: ' + message)
   
    def shutdown(self):
        self.motors.stop()
        GPIO.cleanup()
        
        
    