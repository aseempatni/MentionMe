import csv
from collections import defaultdict
import operator
import ast


filename = "Tweets.txt"
fp = open(filename,'r')

tweets = {}
for line in fp:
	line = line.rstrip()
	try:
		myDict = ast.literal_eval(line)
	except:
		continue
	
	tweetID = myDict['id']
	authorID = myDict['user']['id']
	tweets[tweetID] = authorID

print len(tweets)
