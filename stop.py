import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.cleanup()
