#DHT sensor를 통해 받은 데이터를 DB에 입력하기

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Adafruit_DHT
import time
import pymysql

DHT_PIN = 26 #bcm
DHT_TYPE = Adafruit_DHT.DHT11

#database에 접근
db=pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    passwd='0000',
                    db='raspiDB',
                    charset='utf8')

cursor= db.cursor()
"""
sql=CREATE TABLE DHTsensor(
        idx INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        hum VARCHAR(256) NOT NULL,
        temp VARCHAR(256) NOT NULL,
        time INT UNSIGNED NOT NULL
        );
cursor.execute(sql)
db.commit()

"""
while True:
    hum, temp = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
        
    if hum is not None and temp is not None :
        print("Temp={0:0.1f}*C Humidity = {1:0.1f}%".format(temp,hum)) 
        sql_insert = """insert into DHTsensor(hum, temp, time) values(%s, %s, now())"""
        print(sql_insert)
        cursor.execute(sql_insert, (hum,temp))
        db.commit()
        
        sql_select = """select * FROM DHTsensor"""    
        cursor.execute(sql_select)
        """
        result = cursor.fetchall()
        print('result =>',result)
        for row in result:
            print(row)        
        """
    else:
        print('Failed to get reading. Try again!')


db.close()


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
