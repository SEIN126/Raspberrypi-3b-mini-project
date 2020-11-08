#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

PRI_PIN = 4
red = 19
green = 26

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(PRI_PIN, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

#while 1:
for i in range(1,20):
    if GPIO.input(PRI_PIN) == 1:
        GPIO.output(red,GPIO.input(PRI_PIN))
        GPIO.output(green,0)
        print("motion detected")
        time.sleep(0.2)
    else :
        GPIO.output(red,GPIO.input(PRI_PIN))
        GPIO.output(green,1)
        print("motion undetected")
        time.sleep(0.2)
    time.sleep(1)

GPIO.cleanup()
