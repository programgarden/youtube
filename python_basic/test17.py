import time

start = time.time()
def sync_fnc():
    for i in range(10):
        time.sleep(0.5)
        print(i)
sync_fnc()
end = time.time()
print(end - start)


import asyncio
import time

start = time.time()
async def myFnc():
    for i in range(10):
        await asyncio.sleep(0.5) # 이벤트루프를 블락하지 않음
        print(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(myFnc())
loop.close()
end = time.time()
print(end - start)


import time

start = time.time()
def sync_fnc():
    for i in range(10):
        time.sleep(0.5)
        print(i)

sync_fnc()
sync_fnc()
sync_fnc()

end = time.time()
print(end - start)

import asyncio
import time

start = time.time()
async def myFnc():
    for i in range(10):
        await asyncio.sleep(0.5) # 이벤트루프를 블락하지 않음
        print(i)

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.gather(myFnc(), myFnc(), myFnc()))
loop.close()
end = time.time()
print(end - start)

import asyncio
import time

start = time.time()
async def myFnc():
    for i in range(10):
        await asyncio.sleep(0.5) # 이벤트루프를 블락하지 않음
        print(i)
    return "Test"

loop = asyncio.get_event_loop()

dd = asyncio.ensure_future(myFnc())
loop.run_until_complete(asyncio.gather(
    dd, asyncio.ensure_future(myFnc()), asyncio.ensure_future(myFnc())
))
loop.close()
end = time.time()
print(end - start)
print(dd.result())