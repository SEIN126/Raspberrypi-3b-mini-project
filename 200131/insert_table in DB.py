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
sql="""INSERT INTO test_table(name, nick)
        VALUES('test_name', 'test_nickname');"""

#SQL query 실행
cursor.execute(sql)

#데이터 변화적용
db.commit()

#SQL query 작성 및 실행
sql = """select * FROM test_table"""
cursor.execute(sql)

result = cursor.fetchall()
print('result =>',result)
for row in result:
    print(row)
    
#Database 닫기
db.close()


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
