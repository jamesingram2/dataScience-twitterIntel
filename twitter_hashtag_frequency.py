'''
Name of file: twitter_hashtag_frequency.py
Date created/updated: September 8, 2018
Created by: James Ingram
Code adapted from: Bonzanini, M. (2016). Mastering Social Media Mining with Python. Birmingham, UK: Packt Publishing Ltd. 
Purpose of program: extract the hashtags from a user's timeline and create a list and count of the most common ones
'''
# import functions, libraries, and dependencies
import sys
from collections import Counter
import json

#
def get_hashtags(tweet):
    # entities is a dictionary of URLs, hashtags, and mentions in a tweet
    entities = tweet.get('entities', {})
    # gets a list of the hashtags from the entities dictionary
    hashtags = entities.get('hashtags', [])
    # returns the text of the hashtags
    return [tag['text'].lower() for tag in hashtags]

if __name__ == '__main__':
    # argument = name of json file from which to extract json data
    fname = sys.argv[1]
    # read in json lines file
    with open(fname, 'r') as f:
        hashtags = Counter()
        for line in f:
            tweet = json.loads(line)
            hashtags_in_tweet = get_hashtags(tweet)
            hashtags.update(hashtags_in_tweet)
        # display 20 most common hashtags and their frequencies
        for tag, count in hashtags.most_common(20):
            print("{}: {}".format(tag, count))
