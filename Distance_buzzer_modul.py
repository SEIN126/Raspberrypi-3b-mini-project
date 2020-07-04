#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)


echo = 19
trigger = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 100)



GPIO.setup(echo, GPIO.IN)
GPIO.setup(trigger, GPIO.OUT)

GPIO.output(trigger, 0)
print("waiting fo sensor to settle")
time.sleep(2)

while 1:
    p.start(1)
    GPIO.output(trigger, 1)
    time.sleep(0.00001)
    GPIO.output(trigger, 0)  #trigger에 펄스신호 인가 -> 탐지시작
    
    while GPIO.input(echo) == 0:
        start1 = time.time()
    while GPIO.input(echo) == 1:
        stop = time.time()
        
    check_time = stop - start1
    distance = check_time*34300/2 #거리계산
    print("Distance: %.1fcm" %distance)
  
    if distance < 20 and distance >=15 :
        p.ChangeFrequency(262)
        time.sleep(0.5)
    
    elif distance < 15 and distance >=10 :
        p.ChangeFrequency(330)
        time.sleep(0.5)
        
    elif distance < 10 and distance >=5 :
        p.ChangeFrequency(392)
        time.sleep(0.5)

    elif distance < 5 and distance > 0:
        p.ChangeFrequency(493)
        time.sleep(0.5)
    
    else :
        p.stop()
        time.sleep(0.5)
    
    time.sleep(0.4)  
    
