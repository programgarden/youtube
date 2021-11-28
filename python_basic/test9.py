def test():
    print("test 함수다")

test()
sample = test
sample()

def price_cal():
    return 5000

var_1 = price_cal
print(var_1)
print(var_1())
var_2 = price_cal()
print(var_2)



def stock_names():
    return "삼성", "LG"
var_3 = stock_names
print(var_3)
var_4 = var_3()
print(var_4)

var_5, var_6 = var_3()
print("%s %s" % (var_5, var_6))


# 현재 코스피의 등락율을 찾고(인터넷 검색)
# def kospi_fnc() 라는 함수를 만들고
# 그 안에서 코스프의 등락율보다 높은 코스피의 종목 3개(아무거나)를 골라서
# 딕셔너리 형태로 만들고 -> {종목명:{현재가:데이터, 등락율:데이터}}
# 그 중에서 현재가가 5만원 이상인 종목의 종목명과, 현재가, 등락율을
# return (리턴 총 3개)해라. 함수 안에서 사용하는 제어문(for과 if)
# 그리고 print로 출력

def kospi_fnc():
    kospi_number = 0.48
    stock_dict = {"셀트리온": {"현재가": 372000, "등락율": 22.5},
            "하나투어": {"현재가": 52600, "등락율": 6.71},
            "삼성중공우": {"현재가": 559000, "등락율": 9.61},
            "DB하이텍": {"현재가": 9400, "등락율": 5.28}}
    for name in stock_dict.keys():
        sd = stock_dict[name] # {"현재가"...}
        if 50000 <= sd["현재가"]:
            return name, sd["현재가"], sd["등락율"]
            
result = kospi_fnc()
print("%s %s %s" % result)


def price_fnc(current):
    print(current)
price_fnc(5000)

def price_fnc(high, low):
    print("고가: %s, 저가: %s" % (high, low))
price_fnc(5000, 3000)

def price_fnc(high, low, current, drate):
    print("%s" % high)
price_fnc(drate=0.3, high=2000, low=1000, current=1500)

def price_fnc(high=0, low=0, current=0, drate=None):
    print("%s" % current)
price_fnc(drate=0.3, high=2000)

def price_fnc(high:int=0, low:int=0, current:int=0, drate:float=None):
    print("%s" % current)
price_fnc(drate=0.3, high=2000)



# def cal_stock() 함수를 하나 만들고
# 함수에 하나투어와 하나투어 가격과 비교할 5만원을 전달해주고 
# 5만원보다 크면 True를 반환하고 작으면 False를 반환한다.
# *함수에 전달되어야하는 인자는 "하나투어" 그리고 5만원이다.

def cal_stock(stock_name=None, limit_price=None):
    stock_dict = {"셀트리온": {"현재가": 372000, "등락율": 22.5},
        "하나투어": {"현재가": 52600, "등락율": 6.71},
        "삼성중공우": {"현재가": 559000, "등락율": 9.61},
        "DB하이텍": {"현재가": 9400, "등락율": 5.28}}
        
    if stock_dict[stock_name]["현재가"] > limit_price:
        return True
    else:
        return False
        
result = cal_stock(stock_name="하나투어", limit_price=50000)
print(result)
    


stock_dict = {"셀트리온": {"현재가": 372000, "등락율": 22.5},
    "하나투어": {"현재가": 52600, "등락율": 6.71},
    "삼성중공우": {"현재가": 559000, "등락율": 9.61},
    "DB하이텍": {"현재가": 9400, "등락율": 5.28}}

1. cal_stock 함수를 만들고 그 함수에서 stock_dict을 전달해 준다.
2. 전달받은 cal_stock에는 등락율이 6%이상인 종목들만 return으로 던져준다.
3. 그리고 return으로 나온 종목들을 매수한다.
4. 매수된 종목을 medo_cal_stock 함수에 전달한다.
5. 전달받은 medo_cal_stock에서 현재가 기준 호가단위를 확인해서 등락율27%이상인 가격에서 매도한다.
6. 이때 print로 출력해야할 데이터는, 종목명, 등락율27%의 가격,
7. while문 활용












