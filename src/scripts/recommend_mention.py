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

tweetTopicScores = {}
cleanTweets = []
tweets = []
user_friends = {}
users = []
coeffs = {}
user_ids = []
vectorizer = None 
def getCoeffs(dict) :
	dicts = {}
	user_ids = []
	for key in dict :
		dicts[int(key)] = (dict[key]['coeff'])
		user_ids.append(int(key))
	return (dicts, user_ids)	

def write_everything_one():
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
	with open('../../data/algeria/master.pickle', 'wb') as handle:
  		pickle.dump(master, handle)
	return


def read_everything():
	master = {}		
	with open('../../data/algeria/master.pickle', 'rb') as handle:
		master = pickle.load(handle)
	tweetTopicScores = master["tweetTopicScores"]
	cleanTweets = master["cleanTweets"]
	tweets = master["tweets"] 
	user_friends = master["user_friends"]
	users = master["users"]
 	return tweetTopicScores, cleanTweets, tweets, user_friends, users

def read_topic_word():
	topic_word = []
        with open('../../data/algeria/tweetTopic.pickle', 'rb') as handle:
                topic_word = pickle.load(handle)
	return topic_word


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
	with open('../../data/algeria/tweetTopic.pickle', 'wb') as handle:
                pickle.dump(topic_word, handle)

def init():
 	global tweetTopicScores, cleanTweets, tweets, user_friends, users, coeffs, user_ids, topic_word, vectorizer
	print "Initializing"
	topic_word = read_topic_word()
	vectorizer = joblib.load('../../data/algeria/vec_count.joblib')
	coeffs, user_ids = getCoeffs(data_tempDict)
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
	pickle_topic_word()
