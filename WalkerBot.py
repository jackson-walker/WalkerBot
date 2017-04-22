#!/usr/bin/env python
import tweepy, time, sys, keys.py
#4 turns 3 damage each
auth = tweepy.0AuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("damn what a test")
