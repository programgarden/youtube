# class OrderClass:
    # buysell_count = 0
    
    # @staticmethod
    # def order_fnc(code):
        # print("주문을 넣는다: %s" % code)
        
# class method1():
    # def calcul(self, code):
        # print("계산 막 한다~~~")        
        # OrderClass.order_fnc(code)
            
# class method2():
    # def calcul(self, code):
        # print("계산 막 한다~~~")       
        # OrderClass.order_fnc(code)
    
# class method3():
    # def calcul(self, code):
        # print("계산 막 한다~~~")      
        # OrderClass.order_fnc(code)
        
        

# 문제
# sample_dict = {"삼성":{"현재가":6000}, "LG":{"현재가":3000}, "카카오":{"현재가":5000}}
# sample_dict를 get set으로 바꿔라.
# 그리고 get set으로 바꾼 데이터를 Stock 클래스의 calcul 함수에 던지세요.
# 조건에 맞으면은 Orders 클래스의 buy_order 함수로 매수를 진행한다.

class Stock():
    def calcul(self, sample_dict):
        for name in sample_dict:
            sample_obj = sample_dict[name]
            if sample_obj.getPrice > 5000:
                Orders.buy_order(name)
            
class Orders():
    @staticmethod
    def buy_order(code):
        print("매수주문: %s" % code)
        
class Sample:
    def __init__(self):
        self.__price = None
                
    @property
    def getPrice(self):
        return self.__price
        
    @getPrice.setter
    def setPrice(self, price):
        self.__price = price

stock1 = Sample()
stock1.setPrice = 6000
stock2 = Sample()
stock2.setPrice = 3000
stock3 = Sample()
stock3.setPrice = 5000

sample_dict = {"삼성":stock1, "LG":stock2, "카카오":stock3}
stock = Stock()
stock.calcul(sample_dict)


