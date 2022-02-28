'''
Name of file: twitter_client.py
Date created/updated: September 8, 2018
Created by: James Ingram
Code adapted from: Bonzanini, M. (2016). Mastering Social Media Mining with Python. Birmingham, UK: Packt Publishing Ltd. 
Purpose of program: create a function to setup and authenticate a twitter API client and return a twitter.API object 
'''
# import functions, libraries, and dependencies
import os
import sys
from tweepy import API
from tweepy import OAuthHandler

# Setup twitter authentication; return tweepy.OAuthHandler object
def get_twitter_auth():
    # assigns twitter API authentication data stored in local environment to variables
    try:
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret = os.environ['TWITTER_ACCESS_SECRET']
    # returns key error if unable to load authentication data
    except:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

# Setup twitter API client; return tweepy.API object
def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client
