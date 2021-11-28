# class Stock():
    # def __init__(self):
        # print("Stock class 실행")
        
        # self.price:int = None # 현재가
        # self.drate:float = None # 등락율
        # self.high:int = None # 고가
      
# stock = Stock()
# stock.price = 5000
# stock.drate = 3.9
# stock.high = 5500
# print("현재가: %s" % stock.price)

# stock_dict = {}
# stock_dict["삼성전자"] = stock
# print(stock_dict)

# stock:Stock = stock_dict["삼성전자"]
# price = stock.price
# print("클래스에서 꺼내온 삼성전자 가격: %s" % price)


class Stock():
    def __init__(self):
        print("Stock class 실행")
        
        self.name:str = None # 종목명
        self.price:int = None # 현재가
        self.drate:float = None # 등락율
        self.high:int = None # 고가
        self.start:int = None # 시가
        self.low:int = None # 저가


stock_dict = {}

stock = Stock()
stock.name = "삼성전자"
stock.price = 5000
stock.drate = 3.9
stock.high = 5500
stock.start = 4500
stock.low = 4000

stock_dict[stock.name] = stock
# print(stock_dict)

# stock = Stock()
# stock.name = "LG"
# stock.price = 10000
# stock.drate = 5.9
# stock.high = 11000
# stock.start = 7000
# stock.low = 6000

# stock_dict[stock.name] = stock
# print(stock_dict)

# --- 문제 ---
# Stock이라는 클래스를 만들고
# 종목별로 현재가, 등락율, 고가, 시가, 저가 변수를 만들고
# 딕셔너리에 종목 3개만 생성한다.
# 생성이 됐으면 현재가가 가장 높은 종목명만 출력한다.

# class Stock():
    # def __init__(self):
        # self.price:int = None # 현재가
        # self.drate:float = None # 등락율
        # self.high:int = None # 고가
        # self.start:int = None # 시가
        # self.low:int = None # 저가

# stock_dict = {}
# name_list = ["삼성전자", "LG", "카카오"]
# for name in name_list:
    # if name not in stock_dict.keys():
        # stock = Stock()
        # stock_dict[name] = stock
    
    # if name == "삼성전자":
        # price = 10000
        # drate = 3.9
        # high = 15000
        # start = 9000
        # low = 8000
    # elif name == "LG":
        # price = 15000
        # drate = 1.9
        # high = 20000
        # start = 9000
        # low = 8000
    # elif name == "카카오":
        # price = 7000
        # drate = 5.9
        # high = 9000
        # start = 6000
        # low = 5000
 
    # stock:Stock = stock_dict[name]
    # stock.price = price
    # stock.drate = drate
    # stock.high = high
    # stock.start = start
    # stock.low = low
 
# top_stock_name = None
# top_price = 0
# for name in stock_dict.keys():
    # stock:Stock = stock_dict[name]
    # if stock.price > top_price:
        # top_price = stock.price
        # top_stock_name = name

# print("가장 높은 현재가를 가진 종목: %s"  % top_stock_name)


# --- 문제 ---
# stock_list = ["삼성", "LG", "카카오", "네이버", "유튜브"]
# 삼성은 5000원, LG는 10000원, 카카오는 4000원, 네이버는 7000원 유튜브는 100000원
# 위에서 정한 가격을 Stock이라는 클래스를 만들어서 저장한다.
# stock_list의 순서대로 Stock 클래스를 sample_list에 append 해준다.
# ex) sample_list = []

# sample_list에 다 담겼으면 가격이 가장 높은 순서대로 종목명과 가격을 출력해라.

# ex) 유튜브 100000원
# LG 10000원
# ...

# class Stock():
    # def __init__(self):
        # self.name:str = None
        # self.price:int = None
        
# sample_list = []
# stock_list = ["삼성", "LG", "카카오", "네이버", "유튜브"]
# for name in stock_list:
    # stock = Stock()
    # if name == "삼성":
        # stock.name = name
        # stock.price = 5000
    # elif name == "LG":
        # stock.name = name
        # stock.price = 10000
    # elif name == "카카오":
        # stock.name = name
        # stock.price = 4000
    # elif name == "네이버":
        # stock.name = name
        # stock.price = 7000
    # elif name == "유튜브":
        # stock.name = name
        # stock.price = 100000
        
    # sample_list.append(stock)

# rank_list = []
# for stock in sample_list:
    # if len(rank_list) == 0:
        # rank_list.append(stock)
    # else:
        # for index, stock2 in enumerate(rank_list):
            # if stock.price > stock2.price:
                # rank_list.insert(index, stock)
                # break
            
# for stock3 in rank_list:
    # print("종목: %s, 가격: %s" % (stock3.name, stock3.price))
    


# 1. Stock 클래스 
# 2. 삼성전자, LG
# 3. 가격과 종목명 담아서
# 4. 딕셔너리에 넣기
# 5. 삼성전자 가격이 LG 가격보다 큰가?


class Stock():
    def __init__(self):
        self.name = None
        self.price = None
        self.value_dict = {}
        
    def get_key(self):
        self.value_dict["종목명"] = self.name
        self.value_dict["가격"] = self.price
        
        return self.value_dict
        
stock = Stock()
stock.name = "삼성"
stock.price = 5000

stock_dict = {}
stock_dict["삼성"] = stock
for name in stock_dict.keys():
    stock:Stock = stock_dict[name]
    print(stock)

    for key in stock.get_key().keys():
        value = stock.get_key()[key]
        print("키: %s, 값: %s" % (key, value))

    