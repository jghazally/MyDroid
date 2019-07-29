import RPi.GPIO as GPIO
from time import sleep

GPIO.setmore(GPIO.BOARD)

Motor1 = 3

GPIO.setup(Motor1, GPIO.OUT)

print "Turning motor on"
GPIO.output(Motor1, GPIO.HIGH)

sleep(2)

print "Turning motor off"
GPIO.output(Motor1, GPIO.LOW)

GPIO.cleanup()