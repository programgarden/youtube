from itertools import islice
import os
from datetime import datetime

file_list = os.listdir("csv_files")

def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))

    if len(result) == n:
        yield result

    for elem in it:
        result = result[1:] + (elem,)
        yield result


import csv

매매일자 = datetime.strptime("2020/01/01", "%Y/%m/%d")

for name in file_list:
    # print(name)
    f = open("C:/Users/somet/PycharmProjects/youtube/csv_files/"+name, newline='')
    spamreder = csv.reader(f)
    temp_list = []
    for idx, row in enumerate(spamreder):
        if idx == 0:
            continue
        temp_list.append(row)

    temp_list.reverse()
    result = window(seq=temp_list)

    손익_횟수 = 0
    손절_횟수 = 0
    for row in result:
        날짜_0 = row[0][0]

        try:
            날짜_0 = datetime.strptime(날짜_0, "%Y/%m/%d")
        except:
            날짜_0 = datetime.strptime(날짜_0, "%Y-%m-%d")

        시가_0 = int(row[0][1])
        고가_0 = int(row[0][2])
        저가_0 = int(row[0][3])
        종가_0 = int(row[0][4])

        날짜_1 = row[1][0]
        try:
            날짜_1 = datetime.strptime(날짜_1, "%Y/%m/%d")
        except:
            날짜_1 = datetime.strptime(날짜_1, "%Y-%m-%d")
        시가_1 = int(row[1][1])
        고가_1 = int(row[1][2])
        저가_1 = int(row[1][3])
        종가_1 = int(row[1][4])

        if 종가_0 == 0 or 종가_1 == 0:
            continue

        '''
        패턴 계산하는 영역
        '''
        등락율_0 = (종가_0 - 시가_0) / 시가_0 * 100
        등락율_0 = round(등락율_0, 2)

        갭0투1 = (시가_1 - 고가_0) / 고가_0 * 100
        갭0투1 = round(갭0투1, 2)

        등락율_1 = (종가_1 - 종가_0) / 종가_0 * 100
        등락율_1 = round(등락율_1, 2)

        if 날짜_0 <= 매매일자:
            continue

        if 등락율_0 > 5:
        # if 등락율_0 > 29 and 고가_0 == 종가_0 \
        #         and 갭0투1 > 10 \
        #         and 등락율_1 > 29 and 고가_1 == 종가_1:
            # print("----- 찾은날짜: %s" % 날짜_1)
            ''' 매수시점 '''
            매수가격 = 종가_1

            for data in temp_list:
                try:
                    바라보는_날짜 = datetime.strptime(data[0], "%Y/%m/%d")
                except:
                    바라보는_날짜 = datetime.strptime(data[0], "%Y-%m-%d")

                if 바라보는_날짜 < 날짜_1:
                    continue

                바라보는_종가 = int(data[4])

                바라보는_등락율 = (바라보는_종가 - 매수가격) / 매수가격 * 100
                바라보는_등락율 = round(바라보는_등락율, 2)

                if 바라보는_등락율 >= 20.0:
                    # print("매수시점으로부터 20.0%% 이상 오름: %s" % 바라보는_등락율)
                    # print("매도날짜: %s\n" % 바라보는_날짜)
                    손익_횟수 += 1
                    break
                elif 바라보는_등락율 <= -30.0:
                    # print("매수시점으로부터 -30.0%% 이하로 떨어짐: %s" % 바라보는_등락율)
                    # print("매도날짜: %s\n" % 바라보는_날짜)
                    손절_횟수 += 1
                    break
                # else:
                #     print("지금까지 보유상태: %s\n" % 바라보는_등락율)

    try:
        익절비 = 손익_횟수 / (손익_횟수+손절_횟수)
        익절비 = round(익절비, 2)
        print("종목: %s, 손익 횟수: %s, 손절 횟수: %s, 익절비: %s" % (name, 손익_횟수, 손절_횟수, 익절비))
    except ZeroDivisionError:
        pass

    f.close()