#!/usr/bin/env python
import tweepy, time, sys, keys, RPi.GPIO
#4 turns 3 damage each
auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status("application test")

lgtSense = 17 # pin 17 as light sense readin
GPIO.setmode(GPIO.BCM) #broadcom num scheme
GPIO.setup(lgtSense, GPIO.IN) #take in

#lets do math
#resistance is 5-10k in lights, 200k when dark
#try to make a voltage divider with a 20k and other with the photodiode
#gnd when dark and above .7 or so when light
