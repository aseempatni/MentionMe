from serializer import *

def getRetweets(user_id) :
	ReTweet = deserialize("Retweets")
	tweets = deserialize('Tweets')
	retweeted_tweets = []

        # geting the content of the retweeted tweet
	for retweet in ReTweet[user_id] :
                # if original tweet not present then ignore
		if str(retweet) not in tweets:
			continue
		retweeted_tweet = {}
		retweeted_tweet['id'] = tweets[str(retweet)]['id']
		retweeted_tweet['text'] = tweets[str(retweet)]['text']
		retweeted_tweet['timestamp'] = tweets[str(retweet)]['timestamp'].strftime("%a %b %d %H:%M:%S +0000 %Y")
		retweeted_tweets.append(retweeted_tweet)

	return retweeted_tweets

if __name__ == "__main__":
        # an example
	print getRetweets(244876078)
