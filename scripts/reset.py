#!/usr/bin/python
import RPi.GPIO as GPIO
import os

reset_pin = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(reset_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        GPIO.wait_for_edge(reset_pin, GPIO.FALLING)
        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

        for pid in pids:
            try:
                commandpath = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
                if commandpath[0:24] == '/opt/retropie/emulators/':
                    os.system('kill -QUIT %s' % pid)
            except IOError:
                continue
except KeyboardInterrupt:
    GPIO.cleanup()
