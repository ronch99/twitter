# Reference: socialmedia-class.org/twittertutorial.html
# @author Ziru Chen

try:
	import json
except ImportError:
	import simplejson as json
	
import tweepy

# User credentials
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
CONSUMER_KEY = ""
CONSUMER_SECRET = ""

# Setup tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api and output file
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
output = open("stream083119.txt", "a")

for status in tweepy.Cursor(api.home_timeline).items(100):
	output.write(json.dumps(status._json)) #encode JSON
	output.write("\n")
output.close()
