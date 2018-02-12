# -*- coding: utf-8 -*-

import settings
import datetime
import time

from requests_oauthlib import OAuth1Session


twitter = OAuth1Session(settings.CK, settings.CS, settings.AT, settings.AS)

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

req = twitter.get(url)

limit = req.headers['x-rate-limit-remaining']
reset = req.headers['x-rate-limit-reset']
sec = int(req.headers['X-Rate-Limit-Reset']) - time.mktime(datetime.datetime.now().timetuple())

print("limit:" + limit)
print("reset:" + reset)
print("reset sec: %s" % sec)
