def cal():
    print("함수다")
    
class Cal:
    print("클래스이다")
    price = 5000
    
    def a_fnc(self):
        print("a_fnc")
        print(self.price)
        
        self.name = "삼성"
        print(self.name)
        
        print(dir(self))
        
    def b_fnc(self):
        print("b_fnc")

cal = Cal()
cal.a_fnc()
cal.b_fnc()


class Method():
    def __init__(self, account_num):
        print("초기화")
        print("계좌번호 %s" % account_num)
        
        self.name = "삼성"
        self.price = 0
        self.buy_cnt = 0
        
        print(dir(self))
    
    def cal(self):
        self.price = 5000
        self.buy_cnt = 10
        result = self.price * self.buy_cnt
        print("매입금액 %s" % result)
        
method = Method("203493021")
method.cal()
        
# 종목 5개 정해서, 전일종가, 현재가를 리스트로 구성한다.
# Method 클래스를 하나 만든다.
# Method 클래스 안에 투자방식1 함수 만들고, 투자방식2 함수 만든다.
# 투자방식1에서는 현재가 순위 매긴다.
# 투자방식2에서는 현재가 상위 2종목만 10개씩 산다.
# 그러면 매수된 종목들은 무엇이고 매입금액은 얼마씩 됐는가?
        
        
# 종목 5개 정해서, 전일종가, 현재가를 딕셔너리로 구한다.
# Method 클래스를 하나 만든다.
# Method 클래스 안에 투자방식1 함수 만들고, 투자방식2 함수 만든다.
# 투자방식1에서는 등락율 순위 매긴다.
# 투자방식2에서는 등락율 상위 2종목만 10개씩 산다.
# 그러면 매수된 종목들은 무엇이고 매입금액은 얼마씩 됐는가?
# https://cafe.naver.com/programgarden/1072
dd = {종목1:{현재가:...}}

total_list = []
for key, value in dd.items():
    small_list = []
    small_list.append(key)
    for key2 in value.keys():
        sample_list.append(value[key2])

sample = [[0, 234, "wer"], [1, 12], [2, 23095]]
sample = sorted(sample, reverse=False)
print(sample)   
        
        
        

