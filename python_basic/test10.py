# def cal_fnc(stock_name:str=None, price:int=None, quan:int=None):
    # money = price * quan
    # return money
    
# cal_fnc(stock_name="삼성", price=200000, quan=5)
# mCalFnc = cal_fnc
# result = mCalFnc(stock_name="LG", price=5000, quan=10)

# mCalFnc = cal_fnc
# stock_dict = {"삼성":mCalFnc}
# print(stock_dict)

# mCalFnc_2 = cal_fnc
# stock_dict["LG"] = mCalFnc_2
# print(stock_dict)


# def cal_fnc_2(deposit=500000, price=5000):
    # result = deposit - price
    # print(result)
    # if result == 0:
        # return
    # cal_fnc_2(deposit=result)
# cal_fnc_2()

# 코스닥 지수가 884.62포인트<- 이걸 0으로 0.01포인트씩 올리면 된다.
# 그러면 등락율이 30%이상이려면 몇 포인트가 되어야 할까?


def cal_fnc_3(point=885, add=5, current_point=885):
    add_point = current_point + add
    drate = (add_point - point) / point * 100
    drate = round(drate, 2)
    if drate > 30.0:
        return add_point
    cal_fnc_3(point=point, current_point=add_point)
print(cal_fnc_3())
    
   
