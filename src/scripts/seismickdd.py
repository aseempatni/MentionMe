import sys
import math

def read_everything():
	master = deserialize("master")
	# tweetTopicScores = master["tweetTopicScores"]
	# cleanTweets = master["cleanTweets"]
	tweets = master["tweets"] 
	user_friends = master["user_friends"]
	# users = master["users"]
 	return tweets, user_friends

def getCleanTweets(cleanTweetFile) :
	cleanTweets = set()
	in_clean_tweets_file = open(cleanTweetFile, 'r')
	dataCleanTweets = in_clean_tweets_file.read()
	lines = dataCleanTweets.split('\n')
	for line in lines :
		words = line.split(' ')
		cleanTweets.add(str(words[0]))
	print "Num Clean Tweets : ", len(cleanTweets)
	return cleanTweets

def getReTweetInfo(cleanTweets, tweetFile) :
	try:
		retweets = pickle.load(open('RetweetsSeismic.pickle','rb'))
		return retweets
	except Exception as e:
		print 'Will be making the retweets file'	
	retweets = {}
	with open(tweetFile, 'r') as f:
		for line in f:
			try:
				mydict = eval(line)
				if str(mydict['id']) not in cleanTweets :
					continue
				if 'retweeted_status' in mydict and 'id' in mydict['retweeted_status']:
					orig_tweet_id = mydict['retweeted_status']['id']
					if orig_tweet_id in retweets.keys():
						retweets[str(orig_tweet_id)] = []
					retweets[orig_tweet_id].append(str(mydict['id']))
			except Exception as e :
				print e
	pickle.dump(retweets, open('RetweetsSeismic.pickle', 'wb'))
	return tweets

user_friends, tweetInfo = read_everything() #load from pickle
cleanTweets = getCleanTweets('somefile_1')
retweets = getReTweetInfo(cleanTweets,'somefile_2') #load from pickle


def getAlpha(curTimeStamp):
	return 0.0 #depends on curTimeStamp, not sure what to return

def getLambda(curTimeStamp):
	return 0.0 #depends on curTimeStamp, not sure what to return

def getK(s, curTimeStamp):
	return max(1-2*s/timestamp, 0.0)


def find_pt(curTimeStamp): #find infectiousness
	R_t_tilde = 0.0
	N_et_tilde = 0

	for retweetId in retweets[tweetId]:
		timeStamp = tweetInfo['timestamp']
		R_t_tilde += getK(curTimeStamp - timestamp, curTimeStamp)

	for retweetId in retweets[tweetId]:
		userWhoRetweeted = tweetInfo['userid']
		timeStamp = tweetInfo['timestamp']
		n_i = user_friends[userWhoRetweeted]
		N_et_tilde += n_i*getK(curTimeStamp - timestamp, curTimeStamp)*( math.exp(curTimeStamp - timestamp) - 1 )

	return R_t_tilde/N_et_tilde 


def seismic(tweetId): #return final number of reshares
	
	curTimeStamp = tweetInfo['timestamp']

	N_c = 0.0
	N_et = 0.0

	n_star = 0.0
	tot_cnt = 0.0

	for retweetId in retweets[tweetId]:
		userWhoRetweeted = tweetInfo['userid']
		timeStamp = tweetInfo['timestamp']
		n_i = user_friends[userWhoRetweeted]
		N_c += n_i
		N_et += n_i*( math.exp(curTimeStamp - timestamp) - 1 )

		n_star += len(user_friends[userWhoRetweeted])
		tot_cnt += 1.0

	n_star /= tot_cnt
	totnumRetweets = len(retweets[tweetId])

	alpha_t = getAlpha(curTimeStamp)
	lambda_t = getLambda(curTimeStamp)
	p_t = find_pt(tweetId, curTimeStamp)

	R_infi = totnumRetweets + alpha_t*p_t*(N_c - N_et)/(1 - lambda_t*p_t*n_star)
	
	return R_infi


if __name__ == '__main__':

	wfile = open('somefile.txt')
	for tweetId in tweetInfo.keys():
		wfile.write(str(tweetId) + ' ' + str(seismic(tweetId)) + '\n')
		wfile.flush()
	wfile.close()


