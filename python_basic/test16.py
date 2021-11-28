import threading
import time
import multiprocessing

class Main():

    def __init__(self):
        print("메인 동작")

        self.종목 = "삼성"
        self.가격 = 5000

        sub = SubMain()
        th = threading.Thread(target=sub.thread_fnc, args=(self,))
        th.start()

        sub.thread_stop = True

        while True:
            print(sub.getData())

class SubMain():
    def __init__(self):
        print("서브메인 동작")
        self.thread_stop = False
        self.stock_name = None

    def thread_fnc(self, main의self:Main):
        while self.thread_stop is False:
            time.sleep(1)
            print("종목명: %s, 가격: %s" % (main의self.종목, main의self.가격))
            self.stock_name = "LG"

    def getData(self):
        return self.stock_name

if __name__ == "__main__":
    Main()