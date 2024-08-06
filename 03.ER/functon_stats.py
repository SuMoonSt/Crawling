import requests
import json
from function_base import function_Base

class function_stats(function_Base):
    def __init__(self, api_key):
        super().__init__(api_key)

    def GetNickNum(self, nick):
        url = "https://open-api.bser.io/v1/user/nickname?query=%s"%(nick)

        response = requests.get(url, headers=self.api_key)
        data = self.CheckStatus(response)

        user_id = data['user']['userNum']
        return user_id

    #유저 id로 닉네임, mmr, 랭킹 출력
    """
    UserNum : 유저의 고유번호
    season : 검색할 시즌의 id
    getinfo : 받아올 정보, 기본값은 3개 모두 받아옴. 1 : 닉네임만 / 2 : mmr만 / 3 : 랭킹만
    Team : 솔로/듀오/스쿼드. 현재는 스쿼드 모드만 존재하므로, 별도의 값을 입력하지 않으면 3으로 설정
    """
    def GetUserRank(self, UserNum, season, getinfo = 0, Team = 3):
        
        url = "https://open-api.bser.io/v1/rank/%d/%d/%d"%(UserNum, season, Team)

        response = requests.get(url, headers = self.api_key)

        data = self.CheckStatus(response)
        user_rank = data['userRank']
        user = user_rank.get('nickname')
        mmr = user_rank.get('mmr')
        rank = user_rank.get('rank')

        match getinfo:
            case 0:
                return user, mmr, rank
            case 1:
                return user
            case 2:
                return mmr
            case 3:
                return rank
            case _:
                print("getinfo값은 0~3 사이의 값이어야 합니다.")


    #유저 통계 획득(통계가 매우 기므로 주의)
    def GetUserStats(self, userNum):
        url = "https://open-api.bser.io/v1/user/games/%d"%(userNum)
        
        response = requests.get(url, headers = self.api_key)
        data = self.CheckStatus(response)
        print(json.dumps(data, ensure_ascii=False, indent=3))

    #시즌 번호, 매칭 모드(솔로,듀오, 스쿼드) 입력하고 탑 1000 확인
    def GetTopRankers(self, season, team = 3):
        url = "https://open-api.bser.io/v1/rank/top/%d/%d"%(season, team)

        response = requests.get(url, headers= self.api_key)
        data = self.CheckStatus(response)
        print(json.dumps(data, ensure_ascii=False, indent=3))