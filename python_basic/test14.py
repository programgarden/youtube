# class Stock():
    # def __init__(self):
        # self.__name = None
        # self.__price = 1000
        
    # def getName(self):
        # assert self.__name is not None, "name은 None이다"
        # return self.__name
        
    # def setName(self, name):
        # self.__name = name
        
    # def getPrice(self):
        # assert self.__price > 5000, "5000 이하라서 주문 넣지마~"
        # return self.__price

# stock = Stock()
# print("주문 넣는다! %s" % stock.getPrice())


class Stock():
    def __init__(self):
        self.__price = None
        self.__high = None
        
    def setPrice(self, price):
        if self.__high is None or price > self.__high:
            self.__high = price
        
        if price > 10000:
            self.__price = price
        else:
            self.__price = 5000
     
    def getPrice(self):
        assert self.__price != None, "가격이 None에요!"
        return self.__price
        
    def getHigh(self):
        return self.__high

stock = Stock()
stock.setPrice(3000)
stock.setPrice(3000)
print("주문 넣는다, 주문가겨: %s" % stock.getPrice())
print("고가 가격: %s" % stock.getHigh())

class Stock():
    def __init__(self):
        self.__price = None
        self.__high = None
                
    @property
    def getPrice(self):
        return self.__price
        
    @getPrice.setter
    def setPrice(self, price):
        self.__price = price

stock = Stock()

