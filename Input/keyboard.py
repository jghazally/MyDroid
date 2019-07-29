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
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoYPIN, GPIO.OUT)
GPIO.setup(servoXPIN, GPIO.OUT)

y = GPIO.PWM(servoYPIN, 50) # GPIO 17 for PWM with 50Hz
y.start(5) # Initialization

x = GPIO.PWM(servoXPIN, 50) # GPIO 17 for PWM with 50Hz
x.start(5) # Initialization

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
            x.ChangeDutyCycle(5)
        if (user_input == right) :
            print("Go right")
            x.ChangeDutyCycle(10)
        if (user_input == up) :
            print("Go up")
            y.ChangeDutyCycle(10)
        if (user_input == down) :
            print("Go down")
            y.ChangeDutyCycle(5)

        time.sleep(.1)

except KeyboardInterrupt:
  x.stop()
  y.stop()
  GPIO.cleanup()