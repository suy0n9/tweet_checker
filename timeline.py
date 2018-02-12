# coding: utf-8

import argparse
import settings
import json
from requests_oauthlib import OAuth1Session


def execute(user, count):

    twitter = OAuth1Session(settings.CK, settings.CS, settings.AT, settings.AS)

    params = {'count': count,
              'screen_name': user,
              'exclude_replies': True,
              'include_rts': False}
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    req = twitter.get(url, params=params)
    outfile = "./outfile_{0}.txt".format(user)

    if req.status_code == 200:
        timeline = json.loads(req.text)
        with open(outfile, 'w') as f:
            for tweet in timeline:
                print(tweet["user"]["screen_name"] + '\n')
                print(tweet["text"] + '\n')
                print('----------------')

                f.write(tweet["text"] + '\n')

            limit = req.headers['x-rate-limit-remaining']
            print("API remain: " + limit)
    else:
        print("Error: %d" % req.status_code)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('user',
            help='acount name')
    parser.add_argument('count',
            help='tweet count')

    args = parser.parse_args()

    execute(args.user, args.count)
