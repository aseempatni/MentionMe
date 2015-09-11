import sys
import datetime
import math

def getFriends(friendListFile) :
	friends = {}
	all_users = set()
	with open(friendListFile, 'r') as f:
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

def generateUserTweetMapping(cleanTweets, tweetFile) :
	users = {}
	all_users = set()
	with open(tweetFile, 'r') as f:
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

def getTweets() :
	 with open(tweetFile, 'r') as f:
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

def getTweetScores() :
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

def getFeatures(tweetFile, friendListFile, w_score, cleenTweetFile, tweetDocTopicFile, UserTweetLinks, UserRetweetLinks) :
	tweets = {}
	#Change the value of w in g(t - t')
	weight_factor = float(w_score)
	cleanTweets = set()
	in_clean_tweets_file = open(cleenTweetFile, 'r')
	dataCleanTweets = in_clean_tweets_file.read()
	lines = dataCleanTweets.split('\n')
	for line in lines :
		words = line.split(' ')
		if len(words) > 2 :
			cleanTweets.add(str(words[0]))
	(users, users_tweeted) = generateUserTweetMapping(cleanTweets, tweetFile)

	print "Tweets inserted"
	lda_in = open(tweetDocTopicFile, 'r')
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
	(user_friends, users_friend) = getFriends(friendListFile)
	print "Friends Read"
	#Features for user who tweeted the tweet has been extracted. Neighbour's features also extracted.	
	i = 0
	print "Num users Tweeted : ", len(users_tweeted), "Num users Friend : ", len(users_friend), "Users Tweeted - Users Friend : ", len(users_tweeted - users_friend), "Users Friend - Users Tweeted : ", len(users_friend - users_tweeted)
	num_pairs = 0
	for user in users :
		i += 1
		if i % 50 == 0 :
			print "User", i,"'s tweet features extracted"
		if i == 50 :
			break
		UserTweets = []
		if int(user) in UserTweetLinks.keys() :
			UserTweets = list(UserTweetLinks[int(user)])
		if int(user) in UserRetweetLinks.keys() :
			if len(UserTweets) == 0 :
				UserTweets = list(UserRetweetLinks[int(user)])
			else :
				UserTweets += UserRetweetLinks[int(user)]
		if len(UserTweets) == 0 :
			#print "No Examples for user id : ", user
			continue
		UserTweets = set(UserTweets)
		num_pairs += len(UserTweets)
		for tweet in UserTweets :
			features[(int(user), tweet)] = []
			features[(int(user), tweet)].append('1') #for Bias term of an user who tweeted the tweet

		prev = 0
		j = 0
		for curr_tweet in UserTweets :
			if str(curr_tweet) not in tweets :
				#print "Tweet Id not present : ", curr_tweet
				continue
			for topic in range(len(tweetTopicScores[str(curr_tweet)])):
				#features for a topic of the tweet for an user
				feature = 0
				for tweet in users[user] :
					time_factor = math.exp(weight_factor * float(abs((tweets[tweet]['timestamp'] - tweets[str(curr_tweet)]['timestamp']).total_seconds())))
					feature += (tweetTopicScores[tweet][topic] * tweetTopicScores[str(curr_tweet)][topic] * time_factor)
				features[(int(user), curr_tweet)].append(feature)

				#features for a topic of the tweet for a friend of this user
				for friend in user_friends[str(user)] :
					feature = 0
					if str(friend) not in users :
						#print 'No tweets found for', str(friend)
						continue
					for tweet in users[str(friend)] :
						time_factor = math.exp(weight_factor * float(abs((tweets[tweet]['timestamp'] - tweets[str(curr_tweet)]['timestamp']).total_seconds())))
						feature += (tweetTopicScores[str(tweet)][topic] * tweetTopicScores[str(curr_tweet)][topic] * time_factor)
					features[(int(user), curr_tweet)].append(feature)
			if j == 0 :
				prev = len(features[(int(user), curr_tweet)])
			else :
				curr = len(features[(int(user), curr_tweet)])
				if curr != prev :
					print "Error in Feature Extraction : Curr : ", curr, ", Prev : ", prev
			j += 1
	print "Features Computed", num_pairs
	outFeaturesFile = open("Featuresv2.txt", "w")
	for user_tweet in features.keys() :
		tempDict = {}
		tempDict[user_tweet] = features[user_tweet]
		outFeaturesFile.write(str(tempDict) + '\n')
	print "Features printed in Featuresv2.txt"
	return features

