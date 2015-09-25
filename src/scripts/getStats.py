import pickle
from sklearn import linear_model
import numpy as np
import sys
from extractFeatures import *

def main():

	UserTweetLinks = {}
	UserReTweetLinks = {}
		
	with open(sys.argv[1], 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserTweetLinks[key] = set(value)


	with open(sys.argv[2], 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserReTweetLinks[key] = set(value)

	# tweetFeatures = getFeatures('../../data/algeria/ValidTweets.txt', '../friendList_main.txt', -0.000004, '../../data/algeria/CleanTweets.txt', '../../data/algeria/TweetDocTopic.txt', UserTweetLinks, UserReTweetLinks)

	out_file = open('stats_val.txt', 'w')
	stats = {}
	global_stats = {}
	global_stats['users_only_negative'] = 0
	global_stats['users_only_positive'] = 0
	global_stats['users_not_retweeted'] = 0
	global_stats['users_retweeted'] = 0
	global_stats['users_both_negative_positive'] = 0
	outfile = open('../../data/algeria/UserCoeff.txt', 'w')
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
			i += 1
			#if i % 2 == 1 :
			print "User", i - 1, "done"
			if i == 200 :
				break
			global_stats['users_retweeted'] += 1
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
				#print "No Examples for user id : ", user
				continue
			UserTweets = set(UserTweets)
			#print "num Tweet Topics : ", len(tweetTopicScores)
			features = getUserTweetFeatures(UserTweets, user_id, tweetTopicScores, tweets, users, -0.000004, user_friends)

			for tweetId in tweetIdNotRetweeted:
				if tweetId in features.keys():
					if str(tweetId) not in cleanTweets :
						continue
					if len(features[tweetId]) == 0 :
						print tweetId, " has error"
					tweetVec.append(features[tweetId])
					tweetTarget.append(0)
			stats[user_id]['num_negative_examples'] = len(tweetVec)
			#print "Tweeted : ", tweetVec, tweetTarget
			# if len(tweetVec) <= 0:
			# 	continue
			tweetReVec = []
			tweetReTarget = []
			for tweetId in UserReTweetLinks[user_id]:
				if tweetId in features.keys():
					if str(tweetId) not in cleanTweets :
						continue
					if len(features[tweetId]) == 0 :
                                                print tweetId, " has error in RetweetLink"
					tweetReVec.append(features[tweetId])
					tweetReTarget.append(1)
			stats[user_id]['num_positive_examples'] = len(tweetReVec)
			#print "Retweeted : ", tweetReVec, tweetTarget
			if len(tweetReVec) <= 0 and len(tweetVec) > 0 :
				global_stats['users_only_negative'] += 1
				print "User ", user_id, "ignored as he has only negative examples"
				i -= 1
				continue
			if len(tweetReVec) > 0 and len(tweetVec) <= 0 :
				global_stats['users_only_positive'] += 1
				print "User ", user_id, "ignored as he has only	positive examples"
				i -= 1
				continue
			if len(tweetReVec) > 0 and len(tweetVec) > 0 :
				global_stats['users_both_negative_positive'] += 1 			

			tweetVec += tweetReVec
			tweetTarget += tweetReTarget

			try:
				regr = linear_model.LogisticRegression()
				regr.fit(tweetVec, tweetTarget)
				#print "Model fit"
				tempDict[user_id] = {}
				#print "Temp Dict init"
				tempDict[user_id]['coeff'] = list(regr.coef_)
				#print "List of coeff added"
				MSE = float(np.mean((regr.predict(tweetVec) - tweetTarget) ** 2))
				#print "MSE calculated"
				tempDict[user_id]['MSE'] = MSE
				if MSE > max_MSE :
					max_MSE = MSE
				#outfile.write(str(tempDict)+'\n')
			except Exception as e:
				print e
				strng = ""
				for tweet in tweetVec :
					strng += str(len(tweet)) + " , "
				print strng
				#if (len(tweetReVec) > 0 and len(tweetVec) > len(tweetReVec)) :
				#	print "Error", len(tweetVec), len(tweetTarget)
	outfile.write(str(tempDict)+'\n')
	with open('../../data/algeria/UserCoeff.pickle', 'wb') as handle:
  		pickle.dump(tempDict, handle)
		# else :
		# 	global_stats['users_only_negative'] += 1
		# 	global_stats['users_not_retweeted'] += 1
		# 	tweetVec = []
		# 	tweetTarget = []
		# 	for tweetId in tweetIDs:
		# 		if (user_id, tweetId) in tweetFeatures.keys():
		# 			tweetVec.append(tweetFeatures[(user_id, tweetId)][1:])
		# 			tweetTarget.append(-1)
		# 	stats[user_id]['num_tweets_reached'] = len(tweetIDs)
		# 	stats[user_id]['num_negative_examples'] = len(tweetVec)
		# 	try:
		# 		regr = linear_model.LinearRegression()
		# 		regr.fit(tweetVec, tweetTarget)
		# 		tempDict = {}
		# 		tempDict[user_id] = {}
		# 		tempDict[user_id]['coeff'] = list(regr.coef_)
		# 		MSE = float(np.mean((regr.predict(tweetVec) - tweetTarget)**2))
		# 		tempDict[user_id]['MSE'] = MSE
		# 		if MSE > max_MSE : 
		# 			max_MSE = MSE
		# 		outfile.write(str(tempDict)+'\n')
		# 	except Exception as e:
		# 		print e
		# 		continue

	out_file.write(str(global_stats) + '\n')
	for user_id in stats :
		out_file.write(str(user_id) + ' ' + str(stats[user_id]) + '\n')
	print "Maximum MSE : ", max_MSE

if __name__ == '__main__':
	main()
