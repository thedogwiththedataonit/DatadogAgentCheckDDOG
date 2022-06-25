import requests
import json
from checks import AgentCheck
import logging
import sys
import datetime

logger = logging.getLogger()
fileHandler = logging.FileHandler("/opt/datadog-agent/etc/checks.d/logfile.log")
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class ddogMetric(AgentCheck):
def check(self, instance):
now = datetime.datetime.now()
if (now.hour > 9) and (now.hour < 16):
url = "https://financialmodelingprep.com/api/v3/quote/DDOG?apikey=dafde2e9a09c57318b3a0eca1cb5ad8a"
response = requests.request("GET", url)
data = response.json()
self.gauge('ddog.stockPrice', data[0]['price'])
self.gauge('ddog.dayLow', data[0]['dayLow'])
self.gauge('ddog.dayHigh', data[0]['dayHigh'])
self.gauge('ddog.volume', data[0]['volume'])
self.gauge('ddog.marketCap', data[0]['marketCap'])
self.gauge('ddog.open', data[0]['open'])
self.gauge('ddog.previousClose', data[0]['previousClose'])
self.gauge('ddog.sharesOutstanding', data[0]['sharesOutstanding'])
self.gauge('ddog.eps', data[0]['eps'])
self.gauge('ddog.pe', data[0]['pe'])
self.gauge('ddog.changesPercentage', data[0]['changesPercentage'])
self.gauge('ddog.marketStatus', 1)
logger.info('Datadog Stock Price: ' + str(data[0]['price']) + ' -- Percentage Change: ' + str(data[0]['changesPercentage']) + " timestamp: " $
else:
self.gauge('ddog.marketStatus', 0)