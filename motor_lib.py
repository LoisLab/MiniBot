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
    
    FORWARD=(GPIO.HIGH,GPIO.LOW)
    REVERSE=(GPIO.LOW,GPIO.HIGH)
    
    def __init__(self, pins):
        self.pins=pins
        GPIO.setup(self.pins[0], GPIO.OUT)
        GPIO.setup(self.pins[1], GPIO.OUT)
        GPIO.setup(self.pins[2], GPIO.OUT)
        GPIO.output(self.pins[2], GPIO.LOW)

    def set_direction(self, direction):
        GPIO.output(self.pins[0], direction[0])
        GPIO.output(self.pins[1], direction[1])
        
    def go(self):
        GPIO.output(self.pins[2], GPIO.HIGH)
        
    def stop(self):
        GPIO.output(self.pins[2], GPIO.LOW)
