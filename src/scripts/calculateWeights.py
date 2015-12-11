import pickle
from serializer import *

cleanTweets = []
tweets = []
user_friends = {}
users = []

def get_tweet_and_retweet_links(tweetfile, retweetfile):
	UserTweetLinks = {}
	UserReTweetLinks = {}		

	with open(tweetfile, 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserTweetLinks[key] = set(value)

	with open(retweetfile, 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserReTweetLinks[key] = set(value)

	return UserTweetLinks,UserReTweetLinks

def read_everything():
	master = deserialize("master")
	cleanTweets = master["cleanTweets"]
	tweets = master["tweets"] 
	user_friends = master["user_friends"]
	users = master["users"]
 	return cleanTweets, tweets, user_friends, users

def main():
	UserTweetLinks,UserReTweetLinks = get_tweet_and_retweet_links("../../data/algeria/UserTweetLinks.txt","../../data/algeria/UserReTweetLinks.txt")

	weightMatrix = {}
	for user in users:
		weightMatrix[user] = {}
		for userFriend in user_friends:
			numReached = 0
			numRetweeted = 0
			tweetSet = set()
			for tweet in UserTweetLinks:
				if tweet in users[user]:
					numReached += 1
					tweetSet.add(tweet)
			for tweet in UserReTweetLinks:
				if tweet in tweetSet:
					numRetweeted += 1
			if numReached != 0:
				weightMatrix[user][userFriend] = float(numRetweeted)/numReached
	print weightMatrix


if __name__ == "__main__":
	main()