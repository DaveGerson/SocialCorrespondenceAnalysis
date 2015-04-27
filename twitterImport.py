# -*- coding: utf-8 -*-
__author__ = 'gerson64'
import urllib
import urllib2
import json
import oauth2 as oauth


def getTweets(keyword):
    twitter_token = "*****"
    twitter_secret = "*****"
    access_token = "*****"
    access_secret = "*****"
    consumer = oauth.Consumer(key=twitter_token, secret=twitter_secret)
    access_token = oauth.Token(key=access_token, secret=access_secret)
    client = oauth.Client(consumer, access_token)
    url = 'https://api.twitter.com/1.1/search/tweets.json?count=100&q=' + keyword \
    #      + '&geocode=32.7830556,-96.8066667,40mi'
    response, data = client.request(url)
    return json.loads(data)




