import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1 = 21

GPIO.setup(Motor1, GPIO.OUT)

print "Turning motor on"
GPIO.output(Motor1, GPIO.HIGH)

sleep(2)

print "Turning motor off"
GPIO.output(Motor1, GPIO.LOW)

GPIO.cleanup()
