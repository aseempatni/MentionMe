# frequency distribution of tweeting, mentioning, getting mentioned

import ast
from collections import defaultdict

filename = "Tweets.txt"
fp = open(filename,'r')

tweetDict = defaultdict(int)
mentioningDict = defaultdict(int)
mentionedDict = defaultdict(int)

for line in fp:
	line = line.rstrip()
	try:
		myDict = ast.literal_eval(line)
	except:
		continue
	
	authorID = myDict['user']['id']
	tweetDict[authorID] += 1
	
	mentionList = myDict['entities']['user_mentions']
	if len(mentionList) != 0:
		mentioningDict[authorID] += 1

	mentionIds = [x['id'] for x in mentionList]	
	for id in mentionIds:
		mentionedDict[id] += 1

print "Tweet Count"
for key in tweetDict:
	print key,tweetDict[key]

print "Mentioning Count"
for key in mentioningDict:
	print key,mentioningDict[key]

print "Mentioned Count"
for key in mentionedDict:
	print key,mentionedDict[key]
