## 왜ㅣ인지 모르겠는데 led 상태가 뜨지않는다.

from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

led = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT, initial = GPIO.LOW)

#Creat Object-------------
app = Flask(__name__)

#URL control---------------
@app.route("/") #url에서 엔터치면 url 접속 
def home():
    return render_template("index.html")
        
@app.route("/led/on")
def led_on():
    try:
        GPIO.output(led, GPIO.HIGH)
        return "Ok"
    except expression as identifier:
        return "fail"

@app.route("/led/off")
def led_off():
    try:
        GPIO.output(led, GPIO.LOW)
        return "Ok"
    except expression as identifier:
        return "fail"
    


#Entry code 얘가 있어야 웹서버가 가동됨.-----------------------    
if __name__ == "__main__":
    #start webserver
    app.run(host="0.0.0.0") #0.0.0.0 = local host = 자기자신
    #http://0.0.0.0:5000 =>5000은 flask의 port num.

