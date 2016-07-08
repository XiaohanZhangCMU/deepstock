import oauth2 as oauth
import urllib2 as urllib
from bs4 import BeautifulSoup, NavigableString
from urllib import urlopen

# See assignment1.html instructions or README for how to get these credentials

api_key = "GmNUk9I4KcmwllvLrAXd1jc3G"
api_secret = "sDa9gnHXIbTbm1SJYprb1idXYSBrl69PY7mcIUGGmXhe5zMkAz"
access_token_key = "155909132-c1yQfOMpC85AEBEnUCzGh6bgxbwHEOYSYCrTl59Q"
access_token_secret = "6zkPTtuCkEbWMUXQpgDqiUTVcIY1gdXd1nggu6q4W7oog"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://twitter.com/search?src=typd&q=facebook%20news"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  soup = BeautifulSoup(response,"html.parser")

  for section in soup.find_all('div', {"class":"js-tweet-text-container"}):
    for cell in section.findChildren():
      print cell
#  for link in soup.find_all('a'):
#    print(link.get('href'))

#for line in response:
#    print line.strip()

if __name__ == '__main__':
  fetchsamples()
