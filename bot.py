# import dependencies
import tweepy
import os
from dotenv import load_dotenv
from stream import StreamListener
import time
import logging

# load our .env file to make use of the environment variables
load_dotenv()

# import and assign our environment variables
API_KEY = os.getenv('twitter_api_key')
API_SECRET = os.getenv('twitter_api_secret')
ACCESS_TOKEN = os.getenv('twitter_access_token')
TOKEN_SECRET = os.getenv('twitter_access_token_secret')

# instantiate oauth handler and set access token
twitter_oauth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twitter_oauth.set_access_token(ACCESS_TOKEN, TOKEN_SECRET)

# instantiate tweepy api object using the authentication handler object
api = tweepy.API(twitter_oauth, wait_on_rate_limit=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# print(api.rate_limit_status())

# attempt credential verification. prints exception if something is wrong
try:
    # print(twitter_api.verify_credentials())
    print("Successfully logged in as", logger)
except tweepy.TweepError as e:
    print(e)
except Exception as e:
    print(e)

my_tags = ["Tech", "Python", "Uganda Tech", "AfroBoyUg", "Octachart", "NFT", "Fintechs"]


# Retweet Tweets
def retweet():
    for tag in my_tags:
        for tweet in api.search_tweets(q=tag, lang="en", count=20):
            status = api.get_status(tweet.id, tweet_mode='extended')
            if not status.retweeted:  # Check if Retweet
                try:
                    api.retweet(tweet.id)
                except Exception as e:
                    logger.error("Error on retweet", exc_info=True)



# Liking  Tweets
def favorite():
    for tag in my_tags:
        for tweet in api.search_tweets(q=tag, lang="en", count=20):
            status = api.get_status(tweet.id, tweet_mode='extended')
            if not status.favorited:  # Check if Retweet
                try:
                    api.create_favorite(tweet.id)
                except Exception as e:
                    logger.error("Error on retweet", exc_info=True)


while True:
    favorite()
    retweet()
    time.sleep(900)



"""
# Avoid Repeated Tweets
FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
  file_read = open(FILE_NAME,'r')
  last_seen_id = int(file_read.read().strip())
  file_read.close()
  return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
  file_write = open(FILE_NAME,'w')
  file_write.write(str(last_seen_id))
  file_write.close()
  return

# Reply Tweets
def reply():
  tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode = 'extended')

  for tweet in reversed(tweets):
    if 'brazil' in tweet.full_text.lower():
      api.update_status("@" + tweet.user.screen_name + " In brazilian portuguese we don't say foreign we say GRINGO and I think that is beautiful!", tweet.id)
      store_last_seen(FILE_NAME, tweet.id)
"""

""""  
# instantiate a StreamListener object
# tweets_listener = StreamListener(twitter_api)
twitter_api.update_status('bot tweeting live test 3!')

# instantiate a tweepy.Stream object
tweet_stream = tweepy.Stream(API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET)


# Use the filter method
my_tags = ["#100DaysOfCode", "UCC", "AfroBoyUg", "Python", "Tech In Uganda"]
tweet_stream.filter(track=my_tags, languages=["en"])
"""
