'''
상장되어 있는 종목들을 가져온다.
그리고 인덱스, 코덱스, 인버스 같은 상품들도 같이 불러오기 때문에
가져온 종목들 중에서 그러한 종목들을 제외되도록 직접 필터링을 직접 해줘야한다.
'''

from requests import post
import json


class 메인:
    def __init__(self):
        
        accessToken = self.로그인()
        print("접근키 확인", accessToken)

        종목들 = TR요청들().코스피코스닥(accessCode=accessToken)
        print(종목들)

    def 로그인(self) -> str:
        url = "https://openapi.ebestsec.co.kr:8080/oauth2/token"
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "appkey": "PSpDMSy",
            "appsecretkey": "uizu9MiIwM",
            "scope": "oob",
        }

        response = post(url, headers=headers, data=body)

        return response.json()["access_token"]


class TR요청들:
    def 코스피코스닥(self, accessCode):
        url = "https://openapi.ebestsec.co.kr:8080/stock/market-data"
        headers = {
            "Content-type": "application/json; charset=utf-8",
            "authorization": f"Bearer {accessCode}",
            "tr_cont": "N",
            "tr_cd": "t9945",
            "tr_cont_key": "",
        }
        body = {
            "t9945InBlock": {"gubun": "1"}}

        response = post(url, headers=headers, data=json.dumps(body))
        results: list = response.json()["t9945OutBlock"]
        return results or []


메인()
