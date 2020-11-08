from flask import Flask
import RPi.GPIO as GPIO

led = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)

#Creat Object-------------
app = Flask(__name__)

#URL control---------------
@app.route("/") #url에서 엔터치면 url 접속 
def helloworld():
    return "Hello World"+" 신기방기"

@app.route("/led")
def helloword():
    return "url에 /led/on 혹은 /led/off 를 입력하세요"

        
@app.route("/led/on")
def led_on():
    GPIO.output(led, GPIO.HIGH)
    return "LED ON"

@app.route("/led/off")
def led_off():
    GPIO.output(led, GPIO.LOW)
    return "LED OFF"
    
@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEANUP"
    

#Entry code 얘가 있어야 웹서버가 가동됨.-----------------------    
if __name__ == "__main__":
    #start webserver
    app.run(host="0.0.0.0") #0.0.0.0 = local host = 자기자신
    #http://0.0.0.0:5000 =>5000은 flask의 port num.
