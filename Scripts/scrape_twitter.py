import oauth2 as oauth
import urllib2 as urllib
from bs4 import BeautifulSoup, NavigableString
from urllib import urlopen
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re
import os

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, twitter_file):
        self.ofile = twitter_file

    def on_data(self, data):
        self.ofile.write(data)
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


def collect_rumors(watch_list, dirname):

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

    #This handles Twitter authetification and the connection to Twitter Streaming API

    f = open(dirname+'twitter_data.txt','aw')
    l = StdOutListener(f)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    keywords= watch_list.keys()
#    stream.filter(track=['facebook', 'capitalone', 'apple', 'tesla'])
    stream.filter(track=keywords, async=True)
    
    
