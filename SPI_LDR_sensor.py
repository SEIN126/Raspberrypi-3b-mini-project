#!/usr/bin/env python
# -*- coding: utf-8 -*-
import spidev #spi 라이브러리 임포트
import time

delay = 0.5
ldr_channel = 0 #mcp3008 채널중 센서에 연결한 채널 설정

spi = spidev.SpiDev() #spi 인스턴스 spi생성
spi.open(0,0) #spi 통신 시작, open(bus, device)
spi.max_speed_hz = 100000 #spi 통신 속도 설정 

#0~7까지 8개의 채널에서 SPI 데이터를 읽어옴. 
def readadc(adcnum):
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum<< 4, 0])  
    #xfer2(list of values[, speed_hz, delay_usec, bits_per_word])
    #8 + adcnum<< 4 => d2,d1,d0가 0,0,0 됨 => 0번 채널 의미
    #http://tightdev.net/SpiDev_doc.pdf
    #https://cdn-shop.adafruit.com/datasheets/MCP3008.pdf
    data = ((r[1] & 3) << 8 ) + r[2]
    return data
    
while True:
    ldr_value = readadc(ldr_channel)
    print("------------------------------------------")
    print("LDR Value: %d"%ldr_value)
    time.sleep(delay)
