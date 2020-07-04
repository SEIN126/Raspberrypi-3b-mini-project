#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

ina = 19
inb = 26

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(ina, GPIO.OUT)
GPIO.setup(inb, GPIO.OUT)

while 1:
    k = input("a,b,s중 하나를 입력하세요")
    if k == "a":
        print("a방향")
        GPIO.output(ina, 1)
        GPIO.output(inb, 0)

    elif k == 'b':
        print("b방향")
        GPIO.output(ina, 0)
        GPIO.output(inb, 1)
            
    elif k =='s':
        print("stop")
        GPIO.output(ina, 0)
        GPIO.output(inb, 0)

    else:
        print("다시 입력하세요")
GPIO.cleanup()
