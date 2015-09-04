import sys
import datetime
import math

def getFriends() :
	friends = {}
	all_users = set()
	with open(sys.argv[2], 'r') as f:
		for line in f:
			try :
				currfriends = eval(line)
				for currfriend in currfriends :
					friends[str(currfriend)] = currfriends[currfriend]
				for currfriend in currfriends :
					for friend in currfriends[currfriend] :
						all_users.add(str(friend))
			except Exception as e :
				print line, e
	return (friends, all_users)

def generateUserTweetMapping(cleanTweets) :
	users = {}
	all_users = set()
	with open(sys.argv[1], 'r') as f:
		for line in f:
			try:
				mydict = eval(line)
				if str(mydict['id']) not in cleanTweets :
					continue
				if mydict['user']['id'] not in users :
					users[str(mydict['user']['id'])] = []
					all_users.add(str(mydict['user']['id']))
					users[str(mydict['user']['id'])].append(str(mydict['id']))
				else :
					users[str(mydict['user']['id'])].append(str(mydict['id']))
			except Exception as e :
				print e
	return (users, all_users)

def main() :
	tweets = {}
	#Change the value of w in g(t - t')
	weight_factor = float(sys.argv[3])
	out_file = open("Features.txt", 'w')
	cleanTweets = set()
	in_clean_tweets_file = open(sys.argv[4], 'r')
	dataCleanTweets = in_clean_tweets_file.read()
	lines = dataCleanTweets.split('\n')
	for line in lines :
		words = line.split(' ')
		if len(words) > 2 :
			cleanTweets.add(str(words[0]))
	(users, users_tweeted) = generateUserTweetMapping(cleanTweets)
	with open(sys.argv[1], 'r') as f:
		for line in f:
			try:
				mydict = eval(line)
				if str(mydict['id']) not in cleanTweets :
					continue
				tweets[str(mydict['id'])] = {}
				tweets[str(mydict['id'])]['id'] = mydict['id']
				tweets[str(mydict['id'])]['text'] = mydict['text']
				tweets[str(mydict['id'])]['user'] = mydict['user']['id']
				tweets[str(mydict['id'])]['timestamp'] = datetime.datetime.strptime(str(mydict['created_at']), '%a %b %d %H:%M:%S +0000 %Y')
			except Exception as e :
				print e
	print "Tweets inserted"
	lda_in = open("TweetDocTopic.txt", 'r')
	data = lda_in.read()
	lines = data.split('\n')
	tweetTopicScores = {}
	for line in lines :
		terms = line.split(' ')
		i = 0
		tweetId = ''
		for term in terms :
			if i == 0 :
				tweetTopicScores[str(term)] = []
				tweetId = str(term)
			else :
				tweetTopicScores[tweetId].append(float(term))
			i += 1
	features = {}
	print "Topic Scores Extracted"
	(user_friends, users_friend) = getFriends()
	print "Friends Read"
	#Features for user who tweeted the tweet has been extracted. Neighbour's features also extracted.	
	i = 0
	print "Num users Tweeted : ", len(users_tweeted), "Num users Friend : ", len(users_friend), "Users Tweeted - Users Friend : ", len(users_tweeted - users_friend), "Users Friend - Users Tweeted : ", len(users_friend - users_tweeted)
	for user in users :
		i += 1
		if i % 100 == 0 :
			print "User", i,"'s tweet features extracted"
		for tweet in users[user] :
			features[tweet] = []
			features[tweet].append('1') #for Bias term of an user who tweeted the tweet

		for curr_tweet in users[user] :
			for topic in range(len(tweetTopicScores[curr_tweet])):
				#features for a topic of the tweet for an user
				feature = 0
				for tweet in users[user] :
					if tweet != curr_tweet :
						time_factor = math.exp(weight_factor * abs((tweets[tweet]['timestamp'] - tweets[curr_tweet]['timestamp']).total_seconds()))
						feature += (tweetTopicScores[tweet][topic] * tweetTopicScores[curr_tweet][topic] * time_factor)
				features[curr_tweet].append(feature)

				#features for a topic of the tweet for a friend of this user
				for friend in user_friends[str(user)] :
					feature = 0
					if str(friend) not in users :
						print 'No tweets found for', str(friend)
						continue
					for tweet in users[str(friend)] :
						if tweet != curr_tweet :
							time_factor = math.exp(weight_factor * abs((tweets[tweet]['timestamp'] - tweets[curr_tweet]['timestamp']).total_seconds()))
							feature += (tweetTopicScores[str(tweet)][topic] * tweetTopicScores[str(curr_tweet)][topic] * time_factor)
					features[curr_tweet].append(feature)
	print "Features Computed"
	out_file.write(str(features))

if __name__ == "__main__" :
	main()

