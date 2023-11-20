'''
모든 증권 시스템의 시작은 로그인이다.
RestAPI에서는 아이디와 패스워드를 입력하지 않고 
appkey와 secret key를 이용해서 증권사에 고객이라는 것을 알려준다.
그리고 반환 받은 토큰으로 데이터를 요청하면 된다.
'''

from requests import post

class 메인:
    def __init__(self):
        accessToken = self.로그인()
        print("접근키 확인", accessToken)

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
        
메인()
