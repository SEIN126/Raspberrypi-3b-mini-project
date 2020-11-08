#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)

p.start(0)


while 1:
    for dc in range(0,101,10):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)

    
    for dc in range(100,-1,-5):
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    p.stop()
    break


----------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 100)

freq = [262, 294, 330, 349, 392, 440, 493, 523]
song = [392, 392, 440, 440, 392, 392, 330, 392, 392, 330, 330, 294]
speed = 0.5

p.start(10)

while 1:
    for fr in freq:
        p.ChangeFrequency(fr)
        time.sleep(speed)
        
    for i in range(7,-1,-1):
        p.ChangeFrequency(freq[i])
        time.sleep(speed)
        
    for fr in song:
        p.ChangeFrequency(fr)
        time.sleep(speed)
    p.stop()
    break

---------------------------------------------------------------------------------------------

#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


GPIO.setup(servo_pin, GPIO.OUT)

p = GPIO.PWM(servo_pin, 50)

p.start(0)

try:
    while 1:
        p.ChangeDutyCycle(7.5)
        print("90도")
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        print("180도")
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        print("0도")
        time.sleep(1)
        
        for i in range(0,25,1):
            p.ChangeDutyCycle(i/2)
            time.sleep(1)
        
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
