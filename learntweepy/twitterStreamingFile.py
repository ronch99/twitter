# Reference: socialmedia-class.org/twittertutorial.html
# @author Ziru Chen

try:
	import json
except ImportError:
	import simplejson as json
	
import tweepy

# User credentials
ACCESS_TOKEN = "822036044962902018-u61Vncw4ylohHr9WDe6fQFXT0d67hVa"
ACCESS_SECRET = "SZiSJlrw9493tIM3rud3WHBrMfHdIutX0fwESVdXsb0Ji"
CONSUMER_KEY = "Jr7FMGc2kTprNW5zy7sDcOh6v"
CONSUMER_SECRET = "IAd80cz1CsQykOgCU7pdzuKVMvN3P2VuWxp6nAW9Tk3OOG9hPO"

# Setup tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api and output file
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
output = open("stream083119.txt", "a")

for status in tweepy.Cursor(api.home_timeline).items(100):
	output.write(json.dumps(status._json)) #encode JSON
	output.write("\n")
