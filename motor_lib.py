import RPi.GPIO as GPIO
from time import sleep


class Motors:
    
    def __init__(self, left_pins=(3,5,7), right_pins=(11,13,15)):
        GPIO.setmode(GPIO.BOARD)
        self.left=Motor(left_pins)
        self.right=Motor(right_pins)
        
    def set_direction(self,left_dir,right_dir):
        self.left.set_direction(left_dir)
        self.right.set_direction(right_dir)
        
    def go(self):
        self.left.go()
        self.right.go()
        
    def stop(self):
        self.left.stop()
        self.right.stop()

    def cleanup(self):
        self.stop()
        GPIO.cleanup()


class Motor:
    
    FORWARD=(True,False)
    REVERSE=(False,True)
    
    def __init__(self, pins):
        self.ctrl_pin_0=pins[0]
        self.ctrl_pin_1=pins[1]
        self.enable_pin=pins[2]
        GPIO.setup(self.ctrl_pin_0, GPIO.OUT)
        GPIO.setup(self.ctrl_pin_1, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.output(self.enable_pin, False)
        #self.pwm=GPIO.PWM(self.enable_pin, 100)
        #self.pwm.start(0)
        #self.pwm.ChangeDutyCycle(100)

    def set_direction(self, direction):
        GPIO.output(self.ctrl_pin_0, direction[0])
        GPIO.output(self.ctrl_pin_1, direction[1])
        
    def go(self):
        GPIO.output(self.enable_pin, True)
        
    def stop(self):
        GPIO.output(self.enable_pin, False)
