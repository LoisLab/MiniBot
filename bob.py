from motor_lib import *
import random

class ActionSpace:
    
    actions = [(Motor.FORWARD, Motor.REVERSE, 0.25),
               (Motor.FORWARD, Motor.REVERSE, 0.50),
               (Motor.REVERSE, Motor.FORWARD, 0.25),
               (Motor.REVERSE, Motor.FORWARD, 0.50),
               (Motor.FORWARD, Motor.FORWARD, 0.25),
               (Motor.FORWARD, Motor.FORWARD, 0.50),
               (Motor.REVERSE, Motor.REVERSE, 0.25),
               (Motor.FORWARD, Motor.REVERSE, 0.50)]
             
    def sample():
        return ActionSpace.actions[random.randint(1,len(ActionSpace.actions))]

class Bob:
    
    def __init__(self):
        self.action_space = ActionSpace
        self.motors = Motors()
        
    def step(self, action):
        print(action)
        self.motors.set_direction(action[0],action[1])
        self.motors.go()
        sleep(action[2])
        self.motors.stop()
        
    def listen(self, message):
        tokens = message.split('=')
        if len(tokens)==2 and tokens[0]=='action':
            self.step(ActionSpace.actions[int(tokens[1])])
        else:
            raise ValueError('Unknown command: ' + message)
   
    def shutdown(self):
        self.motors.stop()
        GPIO.cleanup()
        
        
    