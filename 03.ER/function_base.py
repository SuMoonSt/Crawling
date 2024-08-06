import requests
import json

class function_Base:
    def CheckAPIKey(self): # API 키가 정상작동하는지 확인하는 함수
        url = "https://open-api.bser.io/v1/data/hash"

        response = requests.get(url, headers=self.api_key)
        if(response.status_code == 200):
            print("올바른 API Key입니다.")
        else:
            raise Exception("올바른 API Key를 입력해주세요.")

    def __init__(self, api_key): # 생성자, 생성과정에서 API 키를 점검함
        self.api_key = {"x-api-key" : api_key}
        self.CheckAPIKey()

    def PrintAPIKey(self): # API 키를 출력하는 함수
        print(self.api_key['x-api-key'])

    def CheckStatus(self, response): # Response 상태를 점검하는 함수
        data = response.json()
        if response.status_code == 200:
            match data['code']:
                case 200:
                    return data
                case _:
                    raise Exception("정보를 불러오는 데 실패했습니다. " + str(data['code']) + ": " + data['message'])
        else:
            raise Exception("잘못된 URL 주소를 입력했습니다.")


    def Request(self, to_url): # 당장 급하게 response의 text를 확인할 때 쓰는 함수
        url = "https://open-api.bser.io/" + to_url

        response = requests.get(url, headers=self.api_key)
        self.CheckStatus(response)

        print(response.text)