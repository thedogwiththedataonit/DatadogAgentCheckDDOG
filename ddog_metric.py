import requests
import json
from checks import AgentCheck
import logging
import sys
import datetime

logger = logging.getLogger()
fileHandler = logging.FileHandler("/etc/dataog-agent/checks.d/logfile.log")
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)


class ddogMetric(AgentCheck):
    def check(self, instance):
        now = datetime.datetime.now()
        #if the time is not greater than 9:30am or less than 4pm
        if now.hour > 9 and now.hour < 16:
            url = "https://financialmodelingprep.com/api/v3/quote/DDOG?apikey=dafde2e9a09c57318b3a0eca1cb5ad8a"
            response = requests.request("GET", url)
            data = response.json()
            self.gauge('ddog.stockPrice', data[0]['price'])
            self.gauge('ddog.dayLow', data[0]['dayLow'])
            self.gauge('ddog.dayHigh', data[0]['dayHigh'])
            self.gauge('ddog.marketCap', data[0]['marketCap'])
            self.gauge('ddog.volume', data[0]['volume'])
            self.gauge('ddog.open', data[0]['open'])
            self.gauge('ddog.previousClose', data[0]['previousClose'])
            self.gauge('ddog.sharesOutstanding', data[0]['sharesOutstanding'])
            self.gauge('ddog.eps', data[0]['eps'])
            self.gauge('ddog.pe', data[0]['pe'])
            self.gauge('ddog.marketStatus', 'Open')

            logger.info('Datadog Stock Price: ' + str(data[0]['price']) + ' -- Percentage Change: ' + str(data[0]['changesPercentage']) + " timestamp: " + str(data[0]['timestamp']))

        else:
            self.gauge('ddog.marketStatus', 'Closed')
        