import sys

def main() :
	validTweetsFile = open(sys.argv[1], 'r')
	userTweetIds = {}
	userTweetLinks = {}
	userReTweetIds = {}
	
	i = 0
	for line in validTweetsFile :
		line = line.strip('\n').strip()
		i += 1
		if(i % 1000 == 0) :
			print (i / 1000), "done"
		try :
			if len(line) > 0 :
				mydict = eval(line)
				tweet_id = mydict['id']
				tweeting_user_id = mydict['user']['id']
				if tweeting_user_id not in userTweetIds.keys():
					userTweetIds[tweeting_user_id] = []
				userTweetIds[tweeting_user_id].append(tweet_id)

				if 'retweeted_status' in mydict : 
					orig_user_id = mydict['retweeted_status']['user']['id']
					if tweeting_user_id not in userReTweetIds.keys():
						userReTweetIds[tweeting_user_id] = []
					userReTweetIds[tweeting_user_id].append(mydict['retweeted_status']['id'])
				else:
					orig_user_id = ''

				for user_mention in mydict['entities']['user_mentions'] :
					user_id = user_mention['id']
					if user_id != orig_user_id and user_id != tweeting_user_id:
						if user_id not in userTweetLinks.keys():
							userTweetLinks[user_id] = []
						userTweetLinks[user_id].append(tweet_id)

		except Exception as e :	
			continue

	validTweetsFile.close()

	i = 0
	friendListFile = open(sys.argv[2], 'r')
	for line in friendListFile:
		i += 1
		if i%10 == 0:
			print i, "done"
		friendJson = eval(line.strip().strip('\n').strip())
		for key,friends in friendJson.items():
			user_id = int(key)
			for friend in friends:
				if user_id not in userTweetLinks.keys():
					userTweetLinks[user_id] = []
				if friend in userTweetIds.keys():
					userTweetLinks[user_id] += userTweetIds[friend]
	friendListFile.close()

	outputFile = open(sys.argv[3], 'w')
	#print userTweetLinks
	
	for user_id,tweetIds  in userTweetLinks.items():
		tweetIdsSet = set(tweetIds)
		if len(tweetIdsSet) > 0:
			tempDict = {}
			tempDict[user_id] = list(tweetIdsSet)
			outputFile.write(str(tempDict)+'\n')

	outputFile.close()

	outputFile2 = open(sys.argv[4], 'w')
	for user_id,tweetIds in userReTweetIds.items():
		tweetIdsSet = set(tweetIds)
		if len(tweetIdsSet) > 0:
			tempDict = {}
			tempDict[user_id] = list(tweetIdsSet)
			outputFile2.write(str(tempDict)+'\n')

	outputFile2.close()

if __name__ == "__main__" :
	main()
