#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql

#database에 접근
db=pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    passwd='0000',
                    db='raspiDB',
                    charset='utf8')

#특정 데이터베이스 사용위한 커서(진입점)
cursor=db.cursor()

#sql = 'alter table test_table drop nick;' #nick column 삭제 
#sql = 'alter table test_table add new_name varchar(10) not null;' #column 추가
sql = """alter table DHTsensor change time1 time varchar(256);""" # column 변경

cursor.execute(sql)
db.commit()

#Database 닫기
db.close()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
