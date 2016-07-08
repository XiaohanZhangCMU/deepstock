import oauth2 as oauth
import urllib2 as urllib
from bs4 import BeautifulSoup, NavigableString
from urllib import urlopen
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import pandas as pd
import matplotlib.pyplot as plt
import re
# See assignment1.html instructions or README for how to get these credentials

api_key = "GmNUk9I4KcmwllvLrAXd1jc3G"
api_secret = "sDa9gnHXIbTbm1SJYprb1idXYSBrl69PY7mcIUGGmXhe5zMkAz"
access_token_key = "155909132-c1yQfOMpC85AEBEnUCzGh6bgxbwHEOYSYCrTl59Q"
access_token_secret = "6zkPTtuCkEbWMUXQpgDqiUTVcIY1gdXd1nggu6q4W7oog"

consumer_key = api_key
consumer_secret = api_secret

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False



if __name__ == '__main__':
    tweets_data_path = './twitter_data.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    print len(tweets_data)

    tweets = pd.DataFrame()

    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)    


    tweets_by_lang = tweets['lang'].value_counts()

    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_xlabel('Languages', fontsize=15)
    ax.set_ylabel('Number of tweets' , fontsize=15)
    ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
    tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
    fig.savefig( 'bar-language.pdf', transparent=True)
 

    tweets['facebook'] = tweets['text'].apply(lambda tweet: word_in_text('facebook', tweet))
    tweets['capitalone'] = tweets['text'].apply(lambda tweet: word_in_text('capitalone', tweet))
    tweets['apple'] = tweets['text'].apply(lambda tweet: word_in_text('apple', tweet))
    tweets['tesla'] = tweets['text'].apply(lambda tweet: word_in_text('tesla', tweet))

    print tweets['facebook'].value_counts()[True]
    print tweets['capitalone'].value_counts()[True]
    print tweets['apple'].value_counts()[True]
    print tweets['tesla'].value_counts()[True]

    prg_langs = ['facebook', 'capitalone', 'apple','tesla']
    tweets_by_prg_lang = [tweets['facebook'].value_counts()[True], tweets['capitalone'].value_counts()[True], tweets['apple'].value_counts()[True],  tweets['tesla'].value_counts()[True]]
    
    x_pos = list(range(len(prg_langs)))
    width = 0.8
    fig, ax = plt.subplots()
    plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')
    ax.set_ylabel('Number of tweets', fontsize=15)
    ax.set_title('News: facebook vs. capitalone vs. apple vs. tesla', fontsize=10, fontweight='bold')
    ax.set_xticks([p + 0.4 * width for p in x_pos])
    ax.set_xticklabels(prg_langs)
    plt.grid()

    plt.savefig( 'bar-companies-mentioned.pdf', transparent=True)

    exit(0)

'''

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['facebook', 'capitalone', 'apple', 'tesla'])

'''
