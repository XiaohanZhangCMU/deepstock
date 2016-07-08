import oauth2 as oauth
import urllib2 as urllib
import time, re, os, datetime
from bs4 import BeautifulSoup, NavigableString
from urllib import urlopen
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self, twitter_file, stopTime):
        self.ofile = twitter_file
        self.stopTime = stopTime

    def on_data(self, data):
        if time.time() < self.stopTime:
#            print 'time = ', time.time(), ' stpTime = ', self.stopTime
            self.ofile.write(data)
            return True
        else:
            return False

    def on_error(self, status):
        print status

def collect_rumors(watch_list, dirname):

    #Bookeeping login
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
    #print 'datetime.datetime.year' , datetime.datetime.year
    timestamp = str(datetime.datetime.now().year) +'-'+str(datetime.datetime.now().month)+ '-'+ str(datetime.datetime.now().day) +'-'+str(datetime.datetime.now().hour)+ '-'+ str(datetime.datetime.now().minute)

    f = open(dirname+timestamp+'-twitter_data'+'.txt','aw')
    l = StdOutListener(f, time.time()+10)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    stream = Stream(auth, l)

    keywords= watch_list.keys()
    stream.filter(track=keywords)#, async=True)
    stream.disconnect()
    print 'exiting scrape_twitter'
    return 0
