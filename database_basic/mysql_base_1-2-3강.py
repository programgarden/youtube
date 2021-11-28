import pymysql
import xlrd

conn = pymysql.connect(host='127.0.0.1' , user='root' , password='0000', db='world', charset='utf8')

try:
    curs = conn.cursor()
    sql = 'SELECT * from city'
    curs.execute(sql)
    rs = curs.fetchall()
    for row in rs:
        print(row)
finally:
    conn.close()
sql_char = '''
CREATE TABLE 삼성전자
                 (ID INT NOT NULL PRIMARY KEY,
                 날짜 VARCHAR(30) NULL,
                 시간 VARCHAR(30) NULL,
                 시가 INT NULL,
                 고가 INT NULL,
                 저가 INT NULL,
                 종가 INT NULL,
                 5평선 FLOAT NULL,
                 10평선 FLOAT NULL,
                 20평선 FLOAT NULL,
                 60평선 FLOAT NULL,
                 120평선 FLOAT NULL,
                 거래량 INT NULL,
                 5평선거래량 FLOAT NULL,
                 20평선거래량 FLOAT NULL,
                 60평선거래량 FLOAT NULL,
                 120평선거래량 FLOAT NULL)
'''
sql_value ='''
INSERT INTO 삼성전자(ID, 날짜, 시간, 시가, 고가, 저가, 종가, 
5평선,10평선, 20평선, 60평선, 120평선, 거래량, 5평선거래량, 20평선거래량,
60평선거래량, 120평선거래량) VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', charset='utf8')
workbook = xlrd.open_workbook('삼성전자.xls', encoding_override='cp949')

try:
    curs = conn.cursor()
    curs.execute('DROP DATABASE IF EXISTS 틱봉')
    curs.execute('CREATE DATABASE 틱봉')
    conn.select_db('틱봉')
    curs.execute(sql_char)

    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows

    for row in range(1,rows):
        data_list = []
        for col in range(16):
            value_name = sheet.cell_value(0,col)
            values = sheet.cell_value(row,col)

            if col == 0:
                data_list.append(row)

            if values == '' or values == ' ':
                data_list.append(0)

            elif col > 2:
                values_int = round(values,2)
                data_list.append(values_int)
            else:
                data_list.append(values)
        # print(data_list)

        curs.execute(sql_value, data_list)
    conn.commit()

    curs.execute('SELECT * FROM 삼성전자')
    sql_row = curs.fetchall()
    for i in sql_row:
        print(i)

finally:
    conn.close()