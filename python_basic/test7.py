
# for문 확장문제

price_list = (5000, 2000, 1500, 200, 10000)

# 크기 순서대로 다른 리스트에 넣어라!
rank_list = []
for price in price_list:
    rank_list.append(price)
rank_list.sort(reverse=True)
print(rank_list)


price_list = (5000, 2000, 1500, 200, 10000)
# 크기 순서대로 다른 리스트에 넣어라! 
# sort 쓰지말고

stock_dict = {"삼성전자":{"현재가":50000, "등락율":3.2},
                "카카오":{"현재가":20000, "등락율":1.0},
                "LG전자":{"현재가":35000, "등락율":-1.0},
                "현대차":{"현재가":180000, "등락율":5.0},
                "애플":{"현재가":1000000, "등락율":0.25}
                }

# 현재가 100000원 이하는 딕셔너리에서 지운다.
# 남은 종목들을 매수한다.
# 매수했으면은 등락율이 3.0 이상은 다시 매도한다.
# 매도한 종목만 새로운 딕셔너리에 담아서 출력한다.



rank_list = []
for stock_name in stock_dict.keys():
    current = stock_dict[stock_name]["현재가"]
    sam = (stock_name, current)
    
    change_idx = None    
    for idx, tup in enumerate(rank_list):
        if current > tup[1]:
            change_idx = idx
            break

    if change_idx is not None:
        rank_list.insert(change_idx, sam)
    elif change_idx is None:
        rank_list.append(sam)
    
    
    
print("%s " % rank_list)

# ~~~~~ 좀 더 쉬운 문제 ~~~~~
# 리스트로 담는데요~ 현재가 높은 순으로 담으세요~
# 담는 형태는 자유예요!
# ~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~문제~~~~~
# for, if
# 종목들 중에서 현재가가 20000원 초과인 종목을 고르고
# 그 종목들 중에서 등락율 순위를 매겨서 순서대로 출력
# ~~~~~~~~~~~~~
                
rank_list = []
for stock_name in stock_dict.keys():
    current = stock_dict[stock_name]["현재가"]
    drate = stock_dict[stock_name]["등락율"]
    
    if current > 20000:
        sam = (stock_name, drate)
                
        change_idx = None
        for idx, tup in enumerate(rank_list):
            if drate > tup[1]:
                change_idx = idx
                break
        if change_idx is not None:
            rank_list.insert(change_idx, sam)
        else:
            rank_list.append(sam)
# print(rank_list)
        