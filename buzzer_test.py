#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

buzzer_pin = 4

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(buzzer_pin, GPIO.OUT)

for i in range(10):
    GPIO.output(buzzer_pin,1)
    time.sleep(1)
    GPIO.output(buzzer_pin,0)
    time.sleep(1)

GPIO.cleanup()
