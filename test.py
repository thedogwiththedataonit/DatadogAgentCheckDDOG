import requests
import json
import logging
import sys
import datetime

#check if its a weekday
#if it is a weekday, check if its past 9:30am
#if it is past 9:30am, check if its past 4pm
#if it is past 4pm, check if its past 5pm

now = datetime.datetime.now()
print(now.weekday())
