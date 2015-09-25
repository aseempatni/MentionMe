import pickle
import sys
import re
import lda
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from extractFeatures import *
from sklearn.externals import joblib

data_tempDict = {}
with open('../../data/algeria/UserCoeff.pickle', 'rb') as handle:
  	data_tempDict = pickle.load(handle)

def getCoeffs(dict) :
	dicts = {}
	user_ids = []
	for key in dict :
		dicts[int(key)] = dict[key]['coeff']
		user_ids.append(int(key))
	print len(dicts)
	return (dicts, user_ids)	

def recommend_mention(tweet): 
	predictCleanTweets = []
	predictCleanTweets.append(tweet)
	topic_word = []
	# with open(sys.argv[1], 'r') as f:
	with open('../../data/algeria/TweetTopicTerm_V2.txt', 'r') as f:	
		for line in f:
			try:
				tweetParts = line.strip('\n').strip().split(' ', 1)
				tweetId = tweetParts[0]
				tweetParts = tweetParts[1:][0].split(" ")
				tweetprob = [float(x) for x in tweetParts]
				topic_word.append(tweetprob)
			except Exception as e:
				print e
				exit()
	
	# vectorizer = joblib.load(sys.argv[2])
	vectorizer = joblib.load('../../data/algeria/vec_count.joblib')
	tweetPredictDataFeatures = vectorizer.transform(predictCleanTweets)
	tweetPredictDataFeatures = tweetPredictDataFeatures.toarray()
	print tweetPredictDataFeatures.shape
	print tweetPredictDataFeatures[0]
	topic_pred = []	
	for i in xrange(0, len(predictCleanTweets)):
		cumsum = 0.0
		for topic_dist in topic_word:
			sum = 0.0
			for p in xrange(0,len(topic_dist)):
				sum += topic_dist[p]*tweetPredictDataFeatures[i][p]	
			cumsum += sum
			topic_pred.append(sum)
			
		for i in xrange(0, len(topic_pred)):
			topic_pred[i] /= cumsum
		break	
	
	recommend = {}
	tweetTopicScores = getTweetScores("../../data/algeria/TweetDocTopic.txt")
	print "Topic Scores Retrieved"
	cleanTweets = getCleanTweets('../../data/algeria/CleanTweets.txt')
	tweets = getTweets(cleanTweets, '../../data/algeria/ValidTweets.txt')
	print "Tweets extracted"
	user_friends = getFriends('../friendList_main.txt')
	print "Friends extracted"
	users = generateUserTweetMapping(cleanTweets, '../../data/algeria/ValidTweets.txt')
	print "User Tweet mapping created"
	(coeffs, user_ids) = getCoeffs(data_tempDict)

	for user_id in user_ids:
		features = getTweetFeatures(user_id, tweetTopicScores, tweets, users, weight_factor, user_friends, topic_pred)
		coeff = coeffs[user_id]
		prod = features*coeff
		_sum = 0
		for i in prod:
			_sum += i
		prob = 1.0/(1+math.exp(-_sum))
		recommend[user_id] = prob

	return recommend



if __name__ == '__main__':
	main()
