from time import sleep
from motor_lib import *

m = Motors()

m.set_direction(Motor.FORWARD,Motor.FORWARD)
m.go()
sleep(1)
m.stop()

m.set_direction(Motor.REVERSE,Motor.REVERSE)
m.go()
sleep(1)
m.stop()

m.set_direction(Motor.FORWARD,Motor.REVERSE)
m.go()
sleep(1)
m.stop()

m.set_direction(Motor.REVERSE,Motor.FORWARD)
m.go()
sleep(1)
m.stop()

m.cleanup()