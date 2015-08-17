import ast
from collections import defaultdict
from sets import Set
filename = "Tweets.txt"
fp = open(filename,'r')

users = Set([])
for line in fp:
	line = line.rstrip()
	try:
		myDict = ast.literal_eval(line)
	except:
		continue
	
	userID = myDict['user']['id']
	friendsCount = myDict['user']['friends_count']
	users.add((userID,friendsCount))

for user in users:
	print user[0],user[1]
