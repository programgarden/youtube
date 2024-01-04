'''
1. 폴더 안에 파일 존재 여부를 체크한다.
'''

# import os
# import csv

# file_list = os.listdir("C:/Users/somet/PycharmProjects/youtube/csv_files")
# print("파일들 확인: %s" % file_list)
#
# for name in file_list:
#     f = open("C:/Users/somet/PycharmProjects/youtube/csv_files/"+name, newline='')
#     spamreader = csv.reader(f)
#     for idx, row in enumerate(spamreader):
#         print("파일:%s, idx: %s, row:%s" % (name, idx, row))
#     f.close()

from itertools import islice

def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))

    if len(result) == n:
        yield result

    for elem in it:
        result = result[1:] + (elem,)
        print(result)
        yield result

sample = ["20210101", "20210102", "20210103", "20210104", "20210105", "20200106"]
result = window(sample)
for i in result:
    pass
