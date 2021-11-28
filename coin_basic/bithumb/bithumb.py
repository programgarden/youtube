from secret import *
'''
python 3.6 이상

1. websockets 설치
2. asyncio 설치
3. json 설치
4. pycurl 설치
5. urllib 설치

base 64 이해
https://devuna.tistory.com/41

비동기 이해
https://blog.humminglab.io/python-coroutine-programming-1/
https://blog.humminglab.io/python-coroutine-programming-2/

동시성 처리와 이벤트 루프 웹소켓 서버
https://docs.python.org/ko/3.7/howto/sockets.html
https://www.python2.net/questions-212620.htm
https://tech.ssut.me/python-3-play-with-asyncio/
https://sjquant.tistory.com/15?category=797018
https://stackoverflow.com/questions/49858021/listen-to-multiple-socket-with-websockets-and-asyncio
https://medium.com/@maxtortime_88708/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%93%B0%EB%A0%88%EB%93%9C-aiohttp-%EC%BD%94%EB%A3%A8%ED%8B%B4-%EA%B3%B5%EB%B6%80-f1e073df071a
https://ichi.pro/ko/pythongwa-hamkke-web-sokes-sayong-74315371198182
https://stackoverflow.com/questions/53331127/python-websockets-send-to-client-and-keep-connection-alive
https://stackoverflow.com/questions/59182741/python-websockets-lib-client-persistent-connection-with-class-implementation
https://stackoverflow.com/questions/37369849/how-can-i-implement-asyncio-websockets-in-a-class

'''

# import pycurl
# from io import BytesIO
# import time
# import json
# import urllib.parse
#
# #######  빗썸 단일 요청
# def publicRq(endpoint, rgParams, rgParams2):
#
#     url = "https://api.bithumb.com" + endpoint + "/" + rgParams["order_currency"] + "_" + rgParams["payment_currency"]
#     if rgParams2 is not None:
#         str_data = urllib.parse.urlencode(rgParams2)  # post 방식으로 전송하기 위한 데이터 변환
#         url += "?" + str_data
#
#     curl_handle = pycurl.Curl()
#     curl_handle.setopt(pycurl.SSL_VERIFYPEER, False)
#     curl_handle.setopt(pycurl.VERBOSE, 0)  # vervose mode :: 1 => True, 0 => False
#     curl_handle.setopt(pycurl.HTTPGET, 1)  # 헤더 옵션 설정
#     curl_handle.setopt(pycurl.URL, url)
#
#     buffer = BytesIO()
#     curl_handle.setopt(curl_handle.WRITEDATA, buffer)
#     curl_handle.perform()
#     status = curl_handle.getinfo(curl_handle.RESPONSE_CODE)
#
#     assert status == 200, "bithumb access error %s" % status
#
#     string_body = buffer.getvalue().decode('utf-8')
#     res = json.loads(string_body)
#     print(res)
#
#     curl_handle.close()
#
# publicRq("/public/ticker",
#          {"order_currency" : "ALL", "payment_currency" : "KRW"},
#          None
#         )


# import pycurl
# import hmac, hashlib
# import time
# import json
# import base64
# import urllib.parse
# import math
# from io import BytesIO
#
# # private 요청
# def privateRq(endpoint, rgParams):
#     endpoint_item_array = {
#         "endpoint": endpoint
#     }
#     uri_array = dict(endpoint_item_array, **rgParams)  # Concatenate the two arrays.
#     str_data = urllib.parse.urlencode(uri_array)  # post 방식으로 전송하기 위한 데이터 변환
#
#     mt = '%f %d' % math.modf(time.time()) # modf 는 정수와 소수 분리
#     mt_array = mt.split(" ")[:2]
#     usecTime = mt_array[1] + mt_array[0][2:5]
#     nonce = usecTime
#
#     data = endpoint + chr(0) + str_data + chr(0) + nonce
#     utf8_data = data.encode('utf-8')  # 컴퓨터 프로세스 처리가 가능하도록 가변 변환
#
#     key = api_secret_key
#     utf8_key = key.encode('utf-8')
#
#     h = hmac.new(bytes(utf8_key), utf8_data, hashlib.sha512)  # 안전 메세지 인증을 위한 512bits 키 해싱
#     hex_output = h.hexdigest()
#     utf8_hex_output = hex_output.encode('utf-8')
#
#     api_sign = base64.b64encode(utf8_hex_output)  # 바이너리 데이터 손실을 막기 위해 64비트로 변환
#     utf8_api_sign = api_sign.decode('utf-8')
#
#     url = "https://api.bithumb.com" + endpoint
#
#     curl_handle = pycurl.Curl()
#     curl_handle.setopt(pycurl.POST, 1)  # 헤더 옵션 설정
#     # curl_handle.setopt(pycurl.VERBOSE, 1); # vervose mode :: 1 => True, 0 => False
#     curl_handle.setopt(pycurl.POSTFIELDS, str_data)
#     curl_handle.setopt(curl_handle.HTTPHEADER, ['Api-Key: ' + api_connect_key, 'Api-Sign: ' + utf8_api_sign, 'Api-Nonce: ' + nonce])
#     curl_handle.setopt(pycurl.SSL_VERIFYPEER, False)
#     curl_handle.setopt(curl_handle.URL, url)
#
#     buffer = BytesIO()
#     curl_handle.setopt(curl_handle.WRITEDATA, buffer)
#
#     curl_handle.perform()
#
#     status = curl_handle.getinfo(pycurl.RESPONSE_CODE)
#
#     assert status == 200, "bithumb access error %s" % status
#
#     string_body = buffer.getvalue().decode('utf-8')
#     res = json.loads(string_body)
#     print(res)
#
# privateRq(
#         "/info/balance",
#         {"currency":"ALL"}
#         )


# import websockets
# import asyncio
# import json
#
# async def my_connect():
#     async with websockets.connect("wss://pubwss.bithumb.com/pub/ws", ping_interval=None) as ws:
#         dd = {"type": "transaction", "symbols": ["BTC_KRW", "ETH_KRW"]}
#         dd = json.dumps(dd)
#         await ws.send(dd)
#
#         while True:
#             result = await ws.recv()
#             print(result)
#
# test = asyncio.get_event_loop()
# test.run_until_complete(my_connect())
# asyncio.close()

# import websockets
# import asyncio
#
# async def bithumb_websocket():
#     async with websockets.connect("wss://pubwss.bithumb.com/pub/ws", ping_interval=None) as wb:
#         await wb.send('{"type":"ticker", "symbols": ["BTC_KRW", "ETH_KRW"], "tickTypes": ["30M", "1H", "12H", "24H", "MID" ]}')
#
#         while True:
#             result = await wb.recv()
#             print(result)
#
# async def bithumb_websocket3():
#     async with websockets.connect("wss://pubwss.bithumb.com/pub/ws", ping_interval=None) as wb:
#         await wb.send('{"type":"transaction", "symbols":["BTC_KRW" , "ETH_KRW"]}')
#
#         while True:
#             result = await wb.recv()
#             print(result)
#
# async def bithumb_websocket2():
#     async with websockets.connect("wss://pubwss.bithumb.com/pub/ws", ping_interval=None) as wb:
#         await wb.send('{"type":"orderbookdepth", "symbols":["BTC_KRW" , "ETH_KRW"]}')
#
#         while True:
#             result = await wb.recv()
#             print(result)
#
#
# loop = asyncio.get_event_loop()
# asyncio.ensure_future(bithumb_websocket())
# asyncio.ensure_future(bithumb_websocket2())
# asyncio.ensure_future(bithumb_websocket3())
# loop.run_forever()



# from decimal import Decimal
# print(0.0015 - 0.00155)
# print(Decimal("0.0015") - Decimal("0.00155"))



# import datetime
# date = datetime.datetime.fromtimestamp(1417141032622 / 1000.0)
# date = date.strftime('%Y-%m-%d %H:%M:%S.%f')[:-7]
# date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
# print(date)
# print(type(date))