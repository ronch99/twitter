# Reference: socialmedia-class.org/twittertutorial.html

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

# Create the api
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

count = 0
for tweet in tweepy.Cursor(api.home_timeline).items(50):
	if len(tweet.text) > 0:
		print("Tweet  #" + str(count) + "\n" + tweet.text)
		print("Tweet ID: " + str(tweet.id) + "  Created at: " + str(tweet.created_at) + "  Lang: " + tweet.lang + "\n")
		print("User ID: " + tweet.user.id_str)
		print("Name: " + tweet.user.name + " (" + tweet.user.screen_name + ") " + "\n")
		print("Entities: ")
		if (len(tweet.entities["hashtags"]) > 0):
			print("Hashtags: ",tweet.entities["hashtags"])
		elif (len(tweet.entities["user_mentions"]) > 0):
			print("Mentions: ", tweet.entities["user_mentions"])
		else:
			print("Null")
		print()
		count = count + 1
		
