from bob import *

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(7, GPIO.LOW)
GPIO.setup(15, GPIO.LOW)
GPIO.cleanup()
