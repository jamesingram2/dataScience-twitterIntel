'''
Name of file: twitter_get_user_timeline.py
Date created/updated: September 8, 2018
Created by: James Ingram
Code adapted from: Bonzanini, M. (2016). Mastering Social Media Mining with Python. Birmingham, UK: Packt Publishing Ltd. 
Purpose of program: uses twitter client from twitter_client.py to pull tweets from a user's timeline and store it as a jsonl file
'''
# import functions, libraries, and dependencies
import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client

if __name__ == '__main__':
    # file argument = user's twitter handle
    user = sys.argv[1]
    client = get_twitter_client()
    # uses argument in filename
    fname = "user_timeline_{}.jsonl".format(user)
    # writes twitter data to json lines file (each entry separated by new line)
    with open(fname, 'w') as f:
        # iterates through sixteen pages of 200 tweets each to retrieve a maximum of 3,200 tweets
        for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json)+"\n")
