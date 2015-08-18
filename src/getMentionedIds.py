# Extract all the UserIds of the Users who are mentioned in at least one tweet.
import ast
import json
import pprint
import logging
logging.basicConfig(filename='./logs/getMentionIds.log',level=logging.INFO)
f = open('../data/Filtered_Tweets.txt', 'r')
UserIds = set([])
count=0
for line in f:
    tweet = ast.literal_eval(line)
    mentions = tweet['entities']['user_mentions']
    for mention in mentions:
        count+=1
        if count%1000==0:
            logging.info(count/1000)
        UserIds.add(mention['id'])
for userId in UserIds:
    print userId
