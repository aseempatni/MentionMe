import sys
import datetime
import math

def generateUserTweetMapping() :
	users = {}
	with open(sys.argv[1], 'r') as f:
		for line in f:
			try:
				mydict = eval(line)
				if mydict['user']['id'] not in users :
					users[mydict['user']['id']] = []
					users[mydict['user']['id']].append(mydict['id'])
				else :
					users[mydict['user']['id']].append(mydict['id'])
			except Exception as e :
				print e
	return users

def main() :
	tweets = {}
	users = generateUserTweetMapping()
	#Change the value of w in g(t - t')
	weight_factor = sys.argv[3]

	with open(sys.argv[1], 'r') as f:
		for line in f:
			try:
				mydict = eval(line)
				tweets[mydict['id']] = {}
				tweets[mydict['id']]['id'] = mydict['id']
				tweets[mydict['id']]['text'] = mydict['text']
				tweets[mydict['id']]['user'] = mydict['user']['id']
				tweets[mydict['id']]['timestamp'] = datetime.strptime(mydict['created_at'], ,'%a %b %d %H:%M:%S %z %Y')
	lda_in = open('docTopicFile.txt', 'r')
	data = lda_in.read()
	lines = data.split('\n')
	tweetTopicScores = {}
	for line in lines :
		terms = line.split(' ')
		i = 0
		tweetId = ''
		for term in terms :
			if i == 0 :
				tweetTopicScores[term] = []
				tweetId = term
			else :
				tweetTopicScores[tweetId].append(term)
			i += 1
	features = {}
	in_friends_file = open(sys.argv[2], 'r')
	user_friends = eval(in_friends_file.read())

	#Features for user who tweeted the tweet has been extracted. Neighbour's features also extracted.	
	for user in users :
		for tweet in users[user] :
			features[tweet] = []
			features[tweet].append('1') #for Bias term of an user who tweeted the tweet

		for curr_tweet in users[user] :
			for topic in range(len(tweetTopicScores[curr_tweet]))
				#features for a topic of the tweet for an user
				feature = 0
				for tweet in users[user] :
					if tweet != curr_tweet :
						time_factor = math.exp(weight_factor * abs(tweets[tweet]['timestamp'].total_seconds() - tweets[curr_tweet]['timestamp'].total_seconds()))
						feature += (tweetTopicScores[tweet][topic] * tweetTopicScores[curr_tweet][topic] * time_factor)
				features[curr_tweet].append(feature)

				#features for a topic of the tweet for a friend of this user
				for friend in user_friends[user] :
					feature = 0
					for tweet in users[friend] :
						if tweet != curr_tweet :
							time_factor = math.exp(weight_factor * abs(tweets[tweet]['timestamp'].total_seconds() - tweets[curr_tweet]['timestamp'].total_seconds()))
							feature += (tweetTopicScores[tweet][topic] * tweetTopicScores[curr_tweet][topic] * time_factor)
					features[curr_tweet].append(feature)

if __name__ == "__main__" :
	main()