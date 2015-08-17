import ast
from collections import defaultdict

filename = "Tweets.txt"
fp = open(filename,'r')

retweetDict = {}
for line in fp:
	line = line.rstrip()
	try:
		myDict = ast.literal_eval(line)
	except:
		continue
	tweetID = myDict['id']
	retweetCount = myDict['retweet_count']
	retweetDict[tweetID] = int(retweetCount)

for key in retweetDict:
	print key,retweetDict[key]
