import pandas as pd
import tweepy
import jsonpickle
import os

os.chdir('week-04/')

from twitter_keys import api_key, api_secret

auth=tweepy.AppAuthHandler(api_key, api_secret)

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def auth(key, secret):
    auth=tweepy.AppAuthHandler(key, secret)
    api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    if not api:
        print "no"
    else:
