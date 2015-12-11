import pickle
import sys
import re
import lda
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from extractFeatures import *
from sklearn.externals import joblib
from serializer import *

# Global variables that need to be initialized using init() once the server is initialized.
tweetTopicScores = {}
cleanTweets = []
tweets = []
user_friends = {}
users = []
coeffs = {}
user_ids = []
vectorizer = None 

def getCoeffs():
	coeff_dict = deserialize("UserCoeff")
	coeffs = {}
	user_ids = []
	for key in coeff_dict :
		coeffs[int(key)] = (coeff_dict[key]['coeff'])
		user_ids.append(int(key))
	return (coeffs, user_ids)	

def read_everything():
	master = deserialize("master")
	tweetTopicScores = master["tweetTopicScores"]
	cleanTweets = master["cleanTweets"]
	tweets = master["tweets"] 
	user_friends = master["user_friends"]
	users = master["users"]
 	return tweetTopicScores, cleanTweets, tweets, user_friends, users

def read_tweets():
	master = deserialize("master")
	tweets = master["tweets"]
	return tweets

def pickle_topic_word():
	topic_word = []
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
    serialize(topic_word,"tweetTopic")

def pickle_everything_once():
	tweetTopicScores = getTweetScores("../../data/algeria/TweetDocTopic.txt")
	print "Topic Scores Retrieved"
	cleanTweets = getCleanTweets('../../data/algeria/CleanTweets.txt')
	tweets = getTweets(cleanTweets, '../../data/algeria/ValidTweets.txt')
	print "Tweets extracted"
	user_friends = getFriends('../friendList_main.txt')
	print "Friends extracted"
	users = generateUserTweetMapping(cleanTweets, '../../data/algeria/ValidTweets.txt')
	print "User Tweet mapping created"
	master = {}
	master["tweetTopicScores"]= tweetTopicScores
	master["cleanTweets"] = cleanTweets
	master["tweets"] = tweets
	master["user_friends"] = user_friends
	master["users"] = users
  	serialize(master,"master")
  	pickle_topic_word()
	return

# Initialize the global variables
def init():
 	global tweetTopicScores, cleanTweets, tweets, user_friends, users, coeffs, user_ids, topic_word, vectorizer
	print "Initializing"
	coeffs, user_ids = getCoeffs()
	topic_word = deserialize("tweetTopic")
	vectorizer = joblib.load('../../data/algeria/vec_count.joblib')
	tweetTopicScores, cleanTweets, tweets, user_friends, users = read_everything()
	print "Initialized"

def recommend_mention(tweet): 
	print "Generating recommendation."
 	global tweetTopicScores, cleanTweets, tweets, user_friends, users, coeffs, user_ids, topic_word, vectorizer
	predictCleanTweets = []
	predictCleanTweets.append(tweet)
	
	tweetPredictDataFeatures = vectorizer.transform(predictCleanTweets)
	tweetPredictDataFeatures = tweetPredictDataFeatures.toarray()
	topic_pred = []	
	for i in xrange(0, len(predictCleanTweets)):
		cumsum = 0.0
		for topic_dist in topic_word:
			sum = 0.0
			for p in xrange(0,len(topic_dist)):
				sum += topic_dist[p]*tweetPredictDataFeatures[i][p]	
			sum+=1
			cumsum += sum
			topic_pred.append(sum)
			
		for i in xrange(0, len(topic_pred)):
			topic_pred[i] /= cumsum
		break	
	
	recommend = {}

	for user_id in user_ids:
		features = getTweetFeatures(user_id, tweetTopicScores, tweets, users,  -0.000004, user_friends, topic_pred)
		coeff = coeffs[user_id]
		prod = []
		for i in range(len(coeff)) :
			prod.append(features[i] * coeff[i])
		_sum = 0
		for i in prod:
			_sum += i
		prob = 1.0/(1+math.exp(-float(_sum)))
		recommend[user_id] = -_sum

	return recommend


if __name__ == '__main__':
	# Run this code independently to pickle all the files.
	pickle_everything_once()