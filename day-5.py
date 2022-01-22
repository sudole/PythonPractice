import configparser
import json
import requests
from bs4 import BeautifulSoup

# read config file
config = configparser.ConfigParser()
config.read('ddutto-config.ini')

# check config file section
# config.sections()

class LottoManager:
    def __init__(self):
        self.lottoNum = []
        self.roundJson = {}
        self.resultArray = []
        self.recentRound = 0

    # inquire the most recent round
    def inquireRecentRound(self):
        recent_round_url = config.get(section='LOTTO', option='recent-round-url')
        req = requests.get(recent_round_url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        self.recentRound = soup.select_one('div[class=win_result] > h4 > strong')
        self.recentRound = self.recentRound.get_text().replace('회','')

        return self.recentRound
    
    # inquire the winning number of the requested round
    def inquireWinningNum(self, startRound, endRound):
        winning_num_url_by_round = config.get(section='LOTTO', option='winning-num-url-by-round')
        
        for round in range(startRound, endRound+1):
            print('============================')
            print('>>> ', round)
            print('----------------------------')
            # search the winning number 
            # from the start round number to the end round number
            req = requests.get(winning_num_url_by_round + str(round))
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            
            for ball in soup.findAll('span', {'class','ball_645'}):
                ballNum = ball.get_text()
                self.lottoNum.append(ballNum)

            print(self.lottoNum)
            self.roundJson = {'Round': round, 'WinningNumbers': self.lottoNum}
            self.resultArray.append(json.dumps(self.roundJson))
            # clear lottoNum value
            self.lottoNum = []
            print('============================')
        return self.resultArray


lottoMng = LottoManager()
lastNum = int(lottoMng.inquireRecentRound())
lottoResults = lottoMng.inquireWinningNum(lastNum-9, lastNum)
# for result in lottoResults:
#     print(result)