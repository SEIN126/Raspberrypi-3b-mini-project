#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spidev #spi 라이브러리 임포트
import time
import RPi_I2C_driver
import RPi.GPIO as GPIO

delay = 0.5

# LED GPIO###############################
led_pin = 4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
##################################

# SENSOR spi
ldr_channel = 0 #mcp3008 채널중 센서에 연결한 채널 설정
spi = spidev.SpiDev() #spi 인스턴스 spi생성
spi.open(0,0) #spi 통신 시작, open(bus, device)
spi.max_speed_hz = 100000 #spi 통신 속도 설정 
##############################################

print("waiting for signal coming to sensor")

lcd = RPi_I2C_driver.lcd(0x27) #lcd 객체

#lcd 설정#####################
lcd.print("waiting for signal")
time.sleep(1)
for i in range(3):
    lcd.scrollDisplayLeft()
    time.sleep(0.15)
lcd.clear()
lcd.setCursor(0, 1)
lcd.print("coming to sensor")
time.sleep(1)
lcd.setCursor(0,0)
time.sleep(2)
###############################

#0~7까지 8개의 채널에서 SPI 데이터를 읽어옴. 
def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum<< 4, 0])  
    #xfer2(list of values[, speed_hz, delay_usec, bits_per_word])
    #8 + adcnum<< 4 => d2,d1,d0가 0,0,0 됨 => 0번 채널 의미
    data = ((r[1] & 3) << 8 ) + r[2]
    return data


while True:
    lcd.clear()
    ldr_value = readadc(ldr_channel)
    print("------------------s------------------------")
    print("LDR Value: %d"%ldr_value)
    lcd.print("LDR Value: %d"%ldr_value)
    
    
    if ldr_value < 400:
        GPIO.output(led_pin, 1)
    else:
        GPIO.output(led_pin, 0)

    time.sleep(delay)   
