# 단일 동작
def example_fnc():
    print("단일 동작")
    
example_fnc()



# # 멀티 쓰레드, 하지만 단일 쓰레드로 스위칭하면서 진행되는거
# #일반 작업
import time

def no_thread():
    start = time.time()

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
       for e in range(10000000):
           if i == 1000000:
               print()

    end = time.time()

    print("Speed check %s" % (end-start))

no_thread()



#멀티 작업
import threading
import time

def thread(cnt):
    sum = 0

    for i in range(cnt):
        sum += i

        if i == 1000000:
            print(threading.active_count())

    return



if __name__ == "__main__":

    start = time.time()


    threa_j = list()

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        th = threading.Thread(target=thread, args=(10000000,))

        threa_j.append(th)
        th.start()

    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        threa_j[i].join()

    end = time.time()

    print("Speed check %s" % (end-start))


#corutine, async
