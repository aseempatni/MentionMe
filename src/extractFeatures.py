import sys
import datetime
import math

def main() :
		tweets = {}
		user_tweet_in_file = open('UserTweetMapping.txt', 'r')
		data = user_tweet_in_file.read()
		users = eval(data)
		#Change the value of w in g(t - t')
		weight_factor = -0.0004

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
		#Currently features for user who tweeted the tweet has been extracted. Neighbour's features to be extracted.
		for user in users :
			for tweet in users[user] :
				features[tweet] = []
				features[tweet].append('1')
			for curr_tweet in users[user] :
				feature = 0
				for topic in range(len(tweetTopicScores[curr_tweet]))
					for tweet in users[user] :
						if tweet != curr_tweet :
							time_factor = math.exp(weight_factor * abs(tweets[tweet]['timestamp'].total_seconds() - tweets[curr_tweet]['timestamp'].total_seconds())
							feature += (tweetTopicScores[tweet][topic] * tweetTopicScores[curr_tweet][topic] * time_factor)
				features[curr_tweet].append(feature)