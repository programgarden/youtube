import pymongo
import xlrd
import datetime

client = pymongo.MongoClient("mongodb+srv://pythontest:0000@cluster0.74y0v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# mydb = client["test_database"]
# mycol = mydb['test_collection']

# name = {"_id": 0, "name": "기계동산", "part": "H.W."}
# mycol.insert_one(name)

# for i in client.list_databases():
#     print(i)

# print(mycol.find())

# client.drop_database(database)
# mydb.drop_collection("%s" % company)
# mycol.delete_many({})

company = 'LG'
database = '20210310'

mydb = client[database]
mycol = mydb[company]

result = mycol.find({"%s(기본정보)_id" % company: company})

print(result)

for i in result:
    print(i)


class mongodb_test():

    def company_base(self):
        mydb = client[database]
        mycol = mydb['%s(기본정보)' % company]

        workbook_base = xlrd.open_workbook(company + '_기본정보' + '.xls', encoding_override='cp949')
        worksheet_base = workbook_base.sheet_by_index(0)

        data_base = {}
        for col in range(11):
            name = worksheet_base.cell_value(0, col)
            if name == '종목명':
                name = '_id'
            value = worksheet_base.cell_value(1, col)
            data_base.update({name: value})
        print(data_base)

        mycol.insert_one(data_base)

        print('성공_기본정보')

        # for i in mycol.find():
        #     print(i)

    def company_value(self):
        mydb = client[database]
        mycol = mydb[company]

        workbook = xlrd.open_workbook(company + ".xls", encoding_override='cp949')

        worksheet = workbook.sheet_by_index(0)
        rows = worksheet.nrows

        for row_num in range(1, rows):
            data = []
            date_make = ""
            data.insert(0, company)

            for col in range(16):
                value_name = worksheet.cell_value(0, col)
                values = worksheet.cell_value(row_num, col)

                if col <= 1:
                    date_make += values
                    if col == 1:

                        date = datetime.datetime.strptime(date_make, '%Y/%m/%d%H:%M:%S').strftime('%Y%m%d%H%M%S')
                        data.append(date)

                else:

                    if values == '' or values == ' ':
                        data.append(0)
                    else:
                        values_int = round(values,2)
                        data.append(values_int)

            sql = {
                "%s(기본정보)_id" % data[0]: data[0],
                "날짜": data[1],
                "시가": data[2],
                "고가": data[3],
                "저가": data[4],
                "종가": data[5],
                "5일평선": data[6],
                "10일평선": data[7],
                "20일평선": data[8],
                "60일평선": data[9],
                "120일평선": data[10],
                "거래량": data[11],
                "5평선거래량": data[12],
                "20평선거래량": data[13],
                "60평선거래량": data[14],
                "120평선거래량": data[15]
            }

            mycol.insert_one(sql)

        print("성공_틱봉")

# mongodb_test().company_base()
# mongodb_test().company_value()

# mongodb_test().company_value()
# pymongo.errors.ConfigurationError: The "dnspython" module must be installed to use mongodb+srv:// URIs
#In order to use mongo+srv protocol, you need to install pymongo-srv Launch this command to do it with python 3:
#
# pip3 install pymongo[srv]
# or this one for other versions:
#
# pip install pymongo[srv]