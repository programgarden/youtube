# if
stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    print(name)


stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    if name == "삼성전자":
        print(name)
    elif name != "카카오":
        print("카카오 제외하고 %s" % name)

stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    if name == "삼성전자":
        print("매수 %s" % name)
        break
    print("나머지 %s" % name)
print("break 밖으로 나옴")


stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    if name == "삼성전자":
        print("조건 계산 막~~~")
        break

stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    if name == "삼성전자":
        print("%s 조건 계산 막~" % name)
    print("나머지들 계산 %s" % name)

stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    if name == "카카오":
        continue
    print("샘플 나머지 %s" % name)

stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    if name == "카카오":
        continue
    elif name == "네이버":
        continue
    
    print("나머지들 %s" % name)
    
stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    print("컨티뉴 실행전 %s" % name)
    continue
    print("컨티뉴 실행후 %s" % name)
    
stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]
for name in stock_list:
    if name == "카카오":
        print("name이 카카오랑 같다")
        continue
        print("카카오랑 같은거 확인되었고 이후 동작")
    print("name: %s 이 카카오랑 같지 않다" % name)
    
stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]    
for idx, name in enumerate(stock_list):
    print("%s %s" % (idx, name))
    
    
stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]    
cnt = 0
for name in stock_list:
    print("enumerate 안 쓰고 %s %s" % (cnt, name))
    cnt += 1 # cnt = cnt + 1
    
stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]    
cnt = 0
for name in stock_list:
    cnt += 1
    if cnt == 2:
        print("그만 돌림")
        break

stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]    
length_stock = len(stock_list)
print(length_stock)
ran_stock = range(length_stock)
print(ran_stock)
for i in ran_stock:
    print(i)

stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]    
for i in range(len(stock_list)):
    print("한번에 %s" % i)

for idx in range(1, 10):
    print("삼성전자 * %s" % idx)

# 구구단 출력
# 1*1
# 1*2
# ...
# 2*1
# ...
# 9*9

for i in range(0, 10):
    for x in range(0, 10):
        print("구구단 %s * %s" % (i, x))

stock_list = ["삼성전자", "카카오", "네이버", "현대약품"]    
for name in stock_list:
    if name == "삼성전자":
        for i in range(0, 10):
            print("%s * %s" % (name, i))
        break
# 삼성전자 * 카카오 * 1 * 1
# 삼성전자 * 카카오 * 1 * 2
...
# 삼성전자 * 카카오 * 9 * 9

# 삼성전자 * 카카오 * 2
# 카카오 * 네이버 * 4
# 네이버 * 현대약품 * 8


# 삼성전자를 처음엔 1개, 2개, 3개, 4개 ... 9개
# 삼성전자 * 갯수
# 삼성전자 * 1
# 삼성전자 * 2






    




    
    