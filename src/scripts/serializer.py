import pickle
from extractFeatures import *

def serialize(data,file):
	with open('../../data/algeria/'+file+'.pickle', 'wb') as handle:
  		pickle.dump(data, handle)

def deserialize(file):
	with open('../../data/algeria/'+file+'.pickle', 'rb') as handle:
		return pickle.load(handle)

def serialize_everything():
	tweetTopicScores = getTweetScores("../../data/algeria/TweetDocTopic.txt")
	serialize(tweetTopicScores,"TweetTopicScores")

	cleanTweets = getCleanTweets('../../data/algeria/CleanTweets.txt')
	serialize(cleanTweets,"CleanTweets")

	tweets = getTweets(cleanTweets, '../../data/algeria/ValidTweets.txt')
	serialize(tweets,"Tweets")

	user_friends = getFriends('../friendList_main.txt')
	serialize(user_friends,"User_friends")

	users = generateUserTweetMapping(cleanTweets, '../../data/algeria/ValidTweets.txt')
	serialize(users,"Users")

	return

if __name__ == '__main__':
	serialize_everything()