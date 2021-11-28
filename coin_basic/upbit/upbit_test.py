'''
파이썬 버전

python 3.6 이상

필요 모듈
websockets 설치
asyncio 설치
json 설치
PyJWT설치
urllib 설치
​

참조문서 모음
https://docs.upbit.com/docs/create-authorization-request
https://pyjwt.readthedocs.io/en/stable/usage.html
https://websockets.readthedocs.io/en/stable/faq.html?highlight=ping_timeout#how-do-i-keep-idle-connections-open
https://sdr1982.tistory.com/269

'''

import requests

url = "https://api.upbit.com/v1/market/all"
querystring = {"isDetails":"false"}
response = requests.request("GET", url, params=querystring)

print(response.text)

from secret import upbit_access_key, upbit_secret_key

import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests
import threading
import time

def account_loop():

    while True:

        time.sleep(1)

        access_key = upbit_access_key
        secret_key = upbit_secret_key
        server_url = "https://api.upbit.com"

        payload = {
            'access_key': access_key,
            'nonce': str(uuid.uuid4()),
        }

        jwt_token = jwt.encode(payload, secret_key)
        authorize_token = 'Bearer {}'.format(jwt_token)
        headers = {"Authorization": authorize_token}

        res = requests.get(server_url + "/v1/accounts", headers=headers)

        print(res.json())

threading.Thread(target=account_loop).start()

while True:
    time.sleep(1)
    print("이후 코딩 실행, 실시간 틱봉 수신")

import websockets
import asyncio
import json

async def upbit_websocket():

    async with websockets.connect("wss://api.upbit.com/websocket/v1", ping_interval=None) as wb:
        await wb.send('[{"ticket":"test"},{"type":"trade","codes":["KRW-BTC","BTC-BCH"]},{"format":"SIMPLE"}]')

        while True:
            result = await wb.recv()
            result = json.loads(result)
            print(result)

loop = asyncio.get_event_loop()
asyncio.ensure_future(upbit_websocket())
loop.run_forever()

import websockets
import asyncio
import json

async def upbit_websocket():
    wb = await websockets.connect("wss://api.upbit.com/websocket/v1", ping_interval=None)
    await wb.send(json.dumps([{"ticket":"test"},{"type":"trade","codes":["KRW-BTC","BTC-BCH","KRW-AQT"]},{"format":"SIMPLE"}]))

    while True:
        if wb.open:
            result = await wb.recv()
            result = json.loads(result)
            print(result)
        else:
            print("연결 안됨! 또는 연결 끊김")

loop = asyncio.get_event_loop()
asyncio.ensure_future(upbit_websocket())
loop.run_forever()



