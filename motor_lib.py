import RPi.GPIO as GPIO
from time import sleep


class Motors:
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.left=Motor(3,5,7)
        self.right=Motor(11,13,15)
        
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
        self.left.cleanup()
        self.right.cleanup()
        GPIO.cleanup()


class Motor:
    
    FORWARD=(True,False)
    REVERSE=(False,True)
    
    def __init__(self, ctrl_pin_0, ctrl_pin_1, enable_pin):
        self.ctrl_pin_0=ctrl_pin_0
        self.ctrl_pin_1=ctrl_pin_1
        self.enable_pin=enable_pin
        GPIO.setup(self.ctrl_pin_0, GPIO.OUT)
        GPIO.setup(self.ctrl_pin_1, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        self.pwm=GPIO.PWM(enable_pin, 100)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(100)

    def set_direction(self, direction):
        GPIO.output(self.ctrl_pin_0, direction[0])
        GPIO.output(self.ctrl_pin_1, direction[1])
        
    def go(self):
        GPIO.output(self.enable_pin, True)
        
    def stop(self):
        GPIO.output(self.enable_pin, False)
        
    def cleanup(self):
        self.pwm.stop()