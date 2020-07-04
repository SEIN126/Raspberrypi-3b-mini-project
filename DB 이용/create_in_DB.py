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

#SQL query 작성
sql="""CREATE TABLE test_table(
        idx INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        nick VARCHAR(256) NOT NULL
        );"""

#SQL query 실행
cursor.execute(sql)

#데이터 변화적용
#CREATE 혹은 DROP, DELETE, UPDATE, INSERT와 같이
#Database 내부의 데이터에 영향을 주는 함수의 경우 commit()해야함
db.commit()

#Database 닫기
db.close()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
