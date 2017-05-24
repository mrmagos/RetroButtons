#!/usr/bin/python
import RPi.GPIO as GPIO
import os

power_pin = 5
fan_pin = 0 # Set if you have a fan

GPIO.setwarnings(False) #Suppress warning for power_pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(power_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
if fan_pin > 0: #Turn on fan
    GPIO.setup(fan_pin, GPIO.OUT)
    GPIO.output(fan_pin, GPIO.HIGH)
else:
    pass

try:
    GPIO.wait_for_edge(power_pin, GPIO.FALLING)
    os.system("poweroff")
except KeyboardInterrupt:
    GPIO.cleanup()
