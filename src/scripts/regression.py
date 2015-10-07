import pickle
from sklearn import linear_model
import numpy as np
import sys
from extractFeatures import *
from serializer import *

# read input data from files
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

def run_regression():
	UserTweetLinks,UserReTweetLinks = get_tweet_and_retweet_links("../../data/algeria/UserTweetLinks.txt","../../data/algeria/UserReTweetLinks.txt")

	stats = {}
	max_MSE = -10000000.05

	tweetTopicScores = getTweetScores("../../data/algeria/TweetDocTopic.txt")
	print "Topic Scores Retrieved"
	cleanTweets = getCleanTweets('../../data/algeria/CleanTweets.txt')
	tweets = getTweets(cleanTweets, '../../data/algeria/ValidTweets.txt')
	print "Tweets extracted"
	user_friends = getFriends('../friendList_main.txt')
	print "Friends extracted"
	users = generateUserTweetMapping(cleanTweets, '../../data/algeria/ValidTweets.txt')
	print "User Tweet mapping created"

	i = 0
	tempDict = {}
	for user_id in UserTweetLinks.keys():
		tweetIDs = UserTweetLinks[user_id]
		if user_id not in stats :
			stats[user_id] = {}
		if user_id in UserReTweetLinks.keys():
			if str(user_id) in user_friends :
				if len(user_friends[str(user_id)]) >= 1000 :
					print "Num Friends of User", i - 1, user_id, len(user_friends[str(user_id)])
					continue
			print "User", i, "done"
			if i == 200 :
				break
			stats[user_id]['num_tweets_reached'] = len(tweetIDs)
			stats[user_id]['num_Retweeted'] = len(UserReTweetLinks[user_id])
			tweetIdNotRetweeted = tweetIDs - UserReTweetLinks[user_id]
			stats[user_id]['num_tweets_notRetweeted'] = len(tweetIdNotRetweeted)
			tweetVec = []
			tweetTarget = []

			UserTweets = []
			if user_id in UserTweetLinks.keys() :
				UserTweets = list(UserTweetLinks[user_id])
			if user_id in UserReTweetLinks.keys() :
				if len(UserTweets) == 0 :
					UserTweets = list(UserReTweetLinks[user_id])
				else :
					UserTweets += UserReTweetLinks[user_id]
			if len(UserTweets) == 0 :
				# No Examples for user
				continue
			UserTweets = set(UserTweets)
			features = getUserTweetFeatures(UserTweets, user_id, tweetTopicScores, tweets, users, -0.000004, user_friends)

			for tweetId in tweetIdNotRetweeted:
				if tweetId in features.keys():
					if str(tweetId) not in cleanTweets :
						continue
					if len(features[tweetId]) == 0 :
						print tweetId, " has error"
					else:
						tweetVec.append(features[tweetId])
						tweetTarget.append(0)
			stats[user_id]['num_negative_examples'] = len(tweetVec)
			tweetReVec = []
			tweetReTarget = []
			for tweetId in UserReTweetLinks[user_id]:
				if tweetId in features.keys():
					if str(tweetId) not in cleanTweets :
						continue
					if len(features[tweetId]) == 0 :
                                                print tweetId, " has error in RetweetLink"
					else:
						tweetReVec.append(features[tweetId])
						tweetReTarget.append(1)
			stats[user_id]['num_positive_examples'] = len(tweetReVec)

			tweetVec += tweetReVec
			tweetTarget += tweetReTarget

			try:
				regr = linear_model.LogisticRegression()
				regr.fit(tweetVec, tweetTarget)
				tempDict[user_id] = {}
				print regr.coef_
				tempDict[user_id]['coeff'] = regr.coef_[0]
				MSE = float(np.mean((regr.predict(tweetVec) - tweetTarget) ** 2))
				tempDict[user_id]['MSE'] = MSE
				if MSE > max_MSE :
					max_MSE = MSE
				print "user " ,i, "actually done."
				i+=1
			except Exception as e:
				print e
				strng = ""
				for tweet in tweetVec :
					strng += str(len(tweet)) + " , "
				print strng

  	serialize(tempDict,"UserCoeff")

	print "Maximum MSE : ", max_MSE

if __name__ == '__main__':
	run_regression()
