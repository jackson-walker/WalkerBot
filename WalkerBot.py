#!/usr/bin/env python
import tweepy, time, sys, keys
#4 turns 3 damage each
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("application test")
