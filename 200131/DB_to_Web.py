#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import pymysql

#초기화
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello DB!'

@app.route('/show')
def show_data():
    #mariaDB접속
    db = pymysql.connect(host='localhost', port=3306, user='root',passwd='0000',
                    db='raspiDB',
                    charset='utf8')
    cur = db.cursor()
    sql = 'select hum, temp from DHTsensor'
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)
    db.close()
    
    for item in rows:
        print(item[0], item[1])
        
    return render_template('result_list.html', result=rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=False)