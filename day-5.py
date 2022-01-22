import configparser
import json
import statistics
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

    def statisticsNumber(self, lottoResults):
        statistics = {}
        for result in lottoResults:
            jsonResult = json.loads(result)
            for num in jsonResult['WinningNumbers']:
                print(num)
                if is_json_key_present(statistics, num):
                    count = statistics[num]
                    statistics[num] = int(count) + 1
                else:
                    statistics[num] = 1
        print(json.dumps(statistics, sort_keys=True, indent=4))
        return statistics

    def maxNumber(self, statistics):
        max = 0
        maxNumber = 0
        for n in statistics:
            if statistics[n] > max:
                max = statistics[n]
                maxNumber = n
        print('max number >>> ', maxNumber)
        return maxNumber

    def minNumber(self, statistics):
        min = 9999999
        minNumber = 0
        for n in statistics:
            if statistics[n] < min:
                min = statistics[n]
                minNumber = n
        print('min number >>> ', minNumber)
        return minNumber

def is_json_key_present(jsonObj, key):
    try:
        buf = jsonObj[key]
    except KeyError:
        return False
    else:
        pass
    return True


lottoMng = LottoManager()
lastNum = int(lottoMng.inquireRecentRound())
lottoResults = lottoMng.inquireWinningNum(lastNum-9, lastNum)
# for result in lottoResults:
#     print(result)

lottoStat = lottoMng.statisticsNumber(lottoResults)
maxNumber = lottoMng.maxNumber(lottoStat)
minNumber = lottoMng.minNumber(lottoStat)