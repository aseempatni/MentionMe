import ast
from collections import defaultdict

filename = "Tweets.txt"

fp = open(filename,'r')

hashtagDict = defaultdict(int)
for line in fp:
	line = line.rstrip()
	try:
		myDict = ast.literal_eval(line)
	except:
		continue
	
	hashtagList = [x['text'] for x in myDict['entities']['hashtags']]
	for tag in hashtagList:
		hashtagDict[tag] += 1

print "Hashtag Count",len(hashtagDict)
for key in hashtagDict:
	try:
		print key,hashtagDict[key]
	except:
		pass
	
