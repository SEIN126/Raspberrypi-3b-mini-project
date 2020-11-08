#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import RPi_I2C_driver

lcd = RPi_I2C_driver.lcd(0x27)

echo = 19
trigger = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(echo, GPIO.IN)
GPIO.setup(trigger, GPIO.OUT)

GPIO.output(trigger, 0)
print("waiting fo sensor to settle")
lcd.print("waiting fo sensor to settle")
time.sleep(2)

while 1:
    lcd.clear()
    GPIO.output(trigger, 1)
    time.sleep(0.00001)
    GPIO.output(trigger, 0)  #trigger에 펄스신호 인가 -> 탐지시작
    
    while GPIO.input(echo) == 0:
        start = time.time()
    while GPIO.input(echo) == 1:
        stop = time.time()
        
    check_time = stop - start
    distance = check_time*34300/2
    print("Distance: %.1fcm" %distance)
    lcd.print("Distance: %.1fcm" %distance)
    time.sleep(0.4)

