# Reference: socialmedia-class.org/twittertutorial.html
# Reference: developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
# @author Ziru Chen
	
import tweepy

# User credentials
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

# Setup tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# Read the data file
data = open("data/searchJ.txt", "r")
dataSet = set()
for line in data:
	if len(line) > 0:
		dataSet.add(line)
data.close()

#output to the data file
output = open("data/searchJ.txt", "a")

for tweet in tweepy.Cursor(api.search, q='"偽中国語"').items(0):
	# Filter empty and repeated tweets
	if len(tweet.text) > 0 and (tweet.text not in dataSet): 
		dataSet.add(tweet.text);
		output.write(tweet.text + "\n" + "\n")	
output.close()
