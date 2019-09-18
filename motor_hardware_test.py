import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Motor 1 setup
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

#Motor 2 setup
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#Set up the enable pins
pwm1=GPIO.PWM(7, 100)
pwm2=GPIO.PWM(15, 100)
pwm1.start(0)
pwm2.start(0)
pwm1.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)

#Motor 1 forward
GPIO.output(3, True)
GPIO.output(5, False)

#Motor 2 forward
GPIO.output(11, True)
GPIO.output(13, False)

#Enable both motors
GPIO.output(7, True)
GPIO.output(15, True)

sleep(2)

#Disable both motors
GPIO.output(7, False)
GPIO.output(15, False)

#Motor 1 reverse
GPIO.output(3, False)
GPIO.output(5, True)

#Motor 2 reverse
GPIO.output(11, False)
GPIO.output(13, True)

#Enable both motors
GPIO.output(7, True)
GPIO.output(15, True)

sleep(3)

#Shut everything off
GPIO.output(7, False)
GPIO.output(15, False)
pwm1.stop()
pwm2.stop()
GPIO.cleanup()

