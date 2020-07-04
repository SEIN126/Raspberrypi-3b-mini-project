#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

led_pin = 4 #led pin 부여 

GPIO.setwarnings(False) #warning message 무시 

GPIO.setmode(GPIO.BCM) ##GPIO 핀을 BCM으로 핀 취급. =>physical핀으로 취급하려면 BOARD로 선언.

GPIO.setup(led_pin, GPIO.OUT) #led_pin을 out으로 취급. GPIO.setup(pin_num(pin_name), GIPO.OUT)

for i in range(10):
    GPIO.output(led_pin,1)
    time.sleep(1) #1초 대기
    GPIO.output(led_pin,0)
    time.sleep(1)
GPIO.cleanup()
