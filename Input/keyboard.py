#!/usr/bin/python3
# -*- coding: UTF-8 -*-

left = 106
right = 108
up = 105
down = 107

import curses, time
import RPi.GPIO as GPIO
import time

servoYPIN = 17
servoXPIN = 4
xPos = 7.5
yPos = 7.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoYPIN, GPIO.OUT)
GPIO.setup(servoXPIN, GPIO.OUT)

y = GPIO.PWM(servoYPIN, 50) # GPIO 17 for PWM with 50Hz
y.start(yPos) # Initialization

x = GPIO.PWM(servoXPIN, 50) # GPIO 17 for PWM with 50Hz
x.start(xPos) # Initialization


def main(stdscr):
    """checking for keypress"""
    stdscr.nodelay(True)  # do not wait for input when calling getch

    return stdscr.getch()

try:
    while True:
        # print("key:", curses.wrapper(main)) # prints: 'key: 97' for 'a' pressed
                                            # '-1' on no presses

        user_input = curses.wrapper(main)
        print(user_input, left)
        if (user_input == left) :
            print("Go left")
            if (xPos < 12.5) :
                xPos += .5
                x.ChangeDutyCycle(xPos)
        if (user_input == right) :
            print("Go right")
            if (xPos > 2.5) :
                xPos -= .5
                x.ChangeDutyCycle(xPos)
        if (user_input == up) :
            print("Go up")
            if (yPos < 12.5) :
                yPos += .5
                y.ChangeDutyCycle(yPos)
        if (user_input == down) :
            print("Go down")
            if (yPos > 2.5) :
                yPos -= .5
                y.ChangeDutyCycle(yPos)

        time.sleep(.1)

except KeyboardInterrupt:
  x.stop()
  y.stop()
  GPIO.cleanup()
