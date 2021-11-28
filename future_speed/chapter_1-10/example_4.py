###################
##### 함수
###################
def future():
    print("선물 관련 함수 입니다.")
future()

def short_position(stock_name):
    print(stock_name)
short_position("항생")

def short_position(stock_name="콘"):
    print(stock_name)
short_position(stock_name="금")

def short_position(stock_name="콘", order_current="현재가격"):
    print("상품: %s, 가격: %s" % (stock_name, order_current))
short_position(stock_name="항생", order_current="23949")

###
def calculation():
    print("투자방식을 계산한다")

def short_position(stock_name="콘", order_current="현재가격", portfolio_fnc=None):
    print("상품: %s, 가격: %s" % (stock_name, order_current))
    portfolio_fnc()
short_position(order_current="12312", portfolio_fnc=calculation)
###

###
def calculation():
    return "매매한다."

계산결과 = calculation()
print(계산결과)

def calculation():
    return "매매한다.", 5000
계산결과 = calculation()
print(계산결과)

계산결과, 가격 = calculation()
print("계산결과: %s, 가격: %s" % (계산결과, 가격))
###

######################
### 클래스
######################
class Future():
    가격 = 5000

선물클래스 = Future()
print(선물클래스.가격)

class Future():
    가격 = 5000

    def __init__(self):
        print(dir(self))

        self.종목명 = "오일"
        self.오일가격 = 3000
        print(dir(self))

fu = Future()
fu.오일가격 = 7000
print(fu.오일가격)

##
class Future():
    가격 = 5000

    def __init__(self):
        self.종목명 = "오일"
        self.종목명두번째 = "옥수수"

    def test_def(self):
        print(self.종목명)
        print(self.종목명두번째)

fu = Future()
fu.test_def()
##

##
class Future():
    종목종류 = ["오일", "금"]

    def __init__(self):
        self.종목가격 = [1000, 5000]

fu = Future()
print(fu.종목종류)
print(fu.종목가격)

Future.종목종류.append("옥수수")
print(Future.종목종류)

# Future.종목가격.append(2039523)
# print(Future.종목가격)
##

##
class Future():
    종목종류 = ["오일", "금"]

    def __init__(self):
        self.종목가격 = [1000, 5000]


class Calculator():

    def __init__(self):
        print("계산!!")

        fu = Future()
        print("종목 %s 가격에 매매 " % fu.종목가격[0]) # <- 에러
        Future.종목종류.append("옥수수")
        print(Future.종목종류)

Calculator()
###

### 상속
class Parent():
    def __init__(self):
        print("부모입니다.")

        self.가격 = 5000000

    def stock(self):
        return "항생"

class ChildA(Parent):
    def __init__(self):
        print("자식A")

        # print("%s를 받았습니다." % self.가격)
        print("%s를 받았습니다." % self.stock())

class ChildB(Parent):
    def __init__(self):
        super().__init__()
        print("자식B")

        print("가격 %s" % self.가격)
        print("%s을 받았습니다." % self.stock())


ChildA()
ChildB()