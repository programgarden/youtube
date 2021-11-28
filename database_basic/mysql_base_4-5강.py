import pymysql
import xlrd
import datetime
#
# conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db='world', charset='utf8')
#
# try:
#     curs = conn.cursor()
#     sql = 'SELECT * from city'
#     curs.execute(sql)
#     rs = curs.fetchall()
#     for row in rs:
#         print(row)
# finally:
#     conn.close()


sql_char = '''
CREATE TABLE `%s`
                 (ID INT NOT NULL auto_increment PRIMARY KEY,
                 날짜 VARCHAR(30) NULL,
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
                 120평선거래량 FLOAT NULL,
                 틱봉_종목명 varchar(20) NOT NULL,
                 foreign key (틱봉_종목명) references `%s_기본정보` (종목명));
'''

sql_value ='''
INSERT INTO `%s`(날짜, 시가, 고가, 저가, 종가, 
5평선,10평선, 20평선, 60평선, 120평선, 거래량, 5평선거래량, 20평선거래량,
60평선거래량, 120평선거래량,틱봉_종목명) VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

sql_base ='''
CREATE TABLE IF NOT EXISTS `%s_기본정보`(
종목코드 varchar(10),
종목명 varchar(20) primary key,
현재가 int,
등락율 varchar(10),
전일대비 varchar(10),
거래량 int,
시가 int,
고가 int,
저가 int,
유통비율 float,
시가총액 int)
'''

sql_base_value = '''
INSERT INTO `%s_기본정보`(
종목코드, 종목명, 현재가, 등락율, 전일대비, 거래량, 시가, 고가, 저가, 유통비율, 시가총액)
VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
'''

company = '삼성전자'
database = '20210310'
company_2 = [company,company]

conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', charset='utf8')
workbook = xlrd.open_workbook(company + '.xls', encoding_override='cp949')
workbook_base = xlrd.open_workbook(company + '_기본정보.xls', encoding_override='cp949')

try:
    curs = conn.cursor()
    # curs.execute('DROP DATABASE IF EXISTS `%s`', database)
    curs.execute('CREATE DATABASE IF NOT EXISTS `%s`', database)

    curs.execute('USE `%s`', database)

    curs.execute('DROP TABLE IF EXISTS `%s_기본정보`',company)
    curs.execute(sql_base,company)
    workbook_base = workbook_base.sheet_by_index(0)

    data_b_list = []
    for col in range(11):
        value = workbook_base.cell_value(1,col)
        data_b_list.append(value)

    # print(data_b_list)
    data_b_list.insert(0,company)
    curs.execute(sql_base_value, data_b_list)
    conn.commit()


    # curs.execute('DROP TABLE IF EXISTS `%s`',company)
    curs.execute(sql_char,company_2)
    curs.execute('CREATE INDEX 거래량 ON `%s`(거래량)', company)

    sheet = workbook.sheet_by_index(0)
    rows = sheet.nrows

    date_make = "" #20210310151022
    for row in range(1,rows):
        data_list = []
        for col in range(16):

            value_name = sheet.cell_value(0,col)
            values = sheet.cell_value(row,col)

            if col <=1:
                date_make += values
                if col == 1:
                    # print(date_make)
                    date = datetime.datetime.strptime(date_make, '%Y/%m/%d%H:%M:%S').strftime('%Y%m%d%H%M%S')
                    data_list.append(date)
                    date_make = ""

            elif values == '' or values == ' ':
                data_list.append(0)

            elif col > 2:
                values_int = round(values,2)
                data_list.append(values_int)

            else:
                data_list.append(values)

        # print(data_list)
        data_list.insert(0,company)
        data_list.append(company)
        # print(data_list)
        curs.execute(sql_value, data_list)
    conn.commit()

    # curs.execute('SELECT * FROM `%s`',company)
    curs.execute('SELECT LEFT(날짜,10) 종가, SUM(거래량) FROM `%s` GROUP BY LEFT(날짜,10) WITH ROLLUP', company)
    sql_row = curs.fetchall()
    for i in sql_row:
        print(i)


finally:
    conn.close()