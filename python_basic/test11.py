# class Main():
    # def A_fnc(self):
        # print(self)
        # print(dir(self))
        # print("A함수")
    # def B_fnc(self):
        # print("B함수")
        # self.A_fnc()
        
# price = 5000
# Main(price)

# main = Main()
# print(main)
# main.A_fnc()
# main.B_fnc()


# class MySample:
    # def __init__(self, price, name):
        # print("초기화")
        # print("받은가격 %s" % price)
        # print("받은이름 %s" % name)
        
        # self.price:int = price
        # self.name:str = name
        # print("self의 price %s" % self.price)
        # print("self의 name %s" % self.name)
        
        # drate:float = None
        # print(dir(self))
        
    # def cal_fnc(self):
        # print(self.price)
        
# mySample = MySample()
# mySample.cal_fnc()

# price = 5000
# name = "삼성"
# mySample = MySample(price, name)
# mySample.cal_fnc()



current_price = 593024
next_price = 672304
name = "삼성"

class Main():
    def __init__(self, var1, var2, var3):
        self.cal_fnc(var1, var2, var3)
    
    def cal_fnc(self, c_price, n_price, name):
        drate = (n_price - c_price) / c_price * 100
        drate = round(drate, 2)
        print("%s의 등락율 %s%s" % (name, drate, "%"))
Main(current_price, next_price, name)

# Main이라는 클래스를 만들고 위 변수 3개를 던져주세요.
# Main 클래스 안에는 cal_fnc함수가 있다. cal_fnc에서 등락율을
# 구하고 있다. 등락율의 종목명(name)을 print로 출력해봐라~
# 출력 예) "삼성의 등락율 oo.o%"

1. Main클래스 만들기
2. Main 클래스 안에는 등락율 구하는 함수 만들고
3. 등락율이 3.0% 이상이면 매수하는 함수 만들고
4. 증권사hts에서 코스피 종목 삼성, LG, 카카오, 네이버의 
                                전일종가와 현재가를 활용

















