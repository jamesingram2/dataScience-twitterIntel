'''
Name of file: twitter_hashtag_stats.py
Date created/updated: September 8, 2018
Created by: James Ingram
Code adapted from: Bonzanini, M. (2016). Mastering Social Media Mining with Python. Birmingham, UK: Packt Publishing Ltd. 
Purpose of program: counts the number of hashtags used in a user's tweets and calculates the frequencies of the different hashtag counts
'''
# import function, libraries, and dependencies
import sys
from collections import defaultdict
import json

def get_hashtags(tweet):
    # entities is a dictionary of URLs, hashtags, and mentions in a tweet
    entities = tweet.get('entities', {})
    # gets a list of the hashtags from the entities dictionary
    hashtags = entities.get('hashtags', [])
    # returns the text of the hashtags
    return [tag['text'].lower() for tag in hashtags]

def usage():
    print("Usage:")
    print("python {} <filename.jsonl>".format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    fname = sys.argv[1]
    # open jsonl file specified by command line argument
    with open(fname, 'r') as f:
        hashtag_count = defaultdict(int)
        for line in f:
            # read in each line of file and assign to tweet
            tweet = json.loads(line)
            # for each tweet, retrieve the hashtags
            hashtags_in_tweet = get_hashtags(tweet)
            # count the number of hashtags in each tweet
            num_of_hashtags = len(hashtags_in_tweet)
            # add to the count of each hashtag count
            hashtag_count[num_of_hashtags] += 1
        # calculate number of tweets containing hashtags
        tweets_with_hashtags = sum([count for num_of_tags, count in hashtag_count.items() if num_of_tags > 0])
        # caluclate number of tweets without hashtags
        tweets_no_hashtags = hashtag_count[0]
        # calculate total number of tweets
        tweets_total = tweets_no_hashtags + tweets_with_hashtags
        # calculate percentage of tweets with hashtags
        tweets_with_hashtags_percent = "%.2f" % (tweets_with_hashtags / tweets_total * 100)
        # calculate percentage of tweets without hashtags
        tweets_no_hashtags_percent = "%.2f" % (tweets_no_hashtags / tweets_total * 100)
        # assign values to variables
        notags = "{} tweets without hashtags ({}%)".format(tweets_no_hashtags, tweets_no_hashtags_percent)
        withtags = "{} (elite) tweets with at least one hashtag ({}%)".format(tweets_with_hashtags, tweets_with_hashtags_percent)
        # display results
        print("Use of hashtags:")
        print(notags)
        print(withtags)
        print("\nNumber of hashtags used:")
        # display frequencies and percentages of various hashtag counts
        for tag_count, tweet_count in hashtag_count.items():
            if tag_count > 0:
                percent_total = "%.2f" % (tweet_count / tweets_total * 100)
                percent_elite = "%.2f" % (tweet_count / tweets_with_hashtags * 100)
                print("{} tweets with {} hashtags ({}% total, {}% elite)".format(tweet_count, tag_count, percent_total, percent_elite))
