import asyncio
import websockets

async def 실시간틱():

    async with websockets.connect(
        "wss://openapi.ebestsec.co.kr:9443/websocket"
    ) as websocket:
        str = {
            "header": {
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz",
                "tr_type": "3",
            },
            "body": {"tr_cd": "S3", "tr_key": "005930"},
        }
        await websocket.send(str)

        while True:
            data = await websocket.recv()
            print(data)


async def 실시간호가():
    async with websockets.connect(
        "wss://openapi.ebestsec.co.kr:9443/websocket"
    ) as websocket:
        str = {
            "header": {
                "token": "eyJ0eXAiOiJKV1QiLC",
                "tr_type": "3",
            },
            "body": {"tr_cd": "H1_", "tr_key": "005930"},
        }
        await websocket.send(str)

        while True:
            data = await websocket.recv()
            print(data)


async def main():

    asyncio.create_task(실시간틱())
    asyncio.create_task(실시간호가())

    while True:
        await asyncio.sleep(1)


asyncio.run(main())
