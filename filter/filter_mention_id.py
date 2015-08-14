#!/usr/bin/env python
#import matplotlib.pyplot as plt
import math
from collections import defaultdict
import time
import operator
import calendar
import ast
#import numpy as np
import codecs
from datetime import time, date, datetime
import datetime

filename3 = 'original23_tweets.txt'                                               #"/home/soumajit/mohit/egypt/real/bachu/original_tweets.txt"
fp1 = codecs.open(filename3, encoding='utf-8')
fp2=codecs.open('tweet_mention_id23.txt','w',encoding='utf-8');
#count = 0

def processUser(myDict):
    
    userID = myDict['id']
    if userID == '':
        print 'User id not available'
    	userID = -1
##    # while retrieving tweet ids consider only myDict['id'] and comment every other keys as it will show error
##    
##    userName = myDict['name']
##    if userName == '':
##    	userName = 'None'
##    	
##    screenName = myDict['screen_name']
##    if screenName == '':
##    	screenName = 'None'	
##    	
##    followersCount  = myDict['followers_count']
##    if followersCount == '':
##    	followersCount = 0
##    	
##    listedCount = myDict['listed_count']
##    if listedCount == '':
##    	listedCount = 0
##    	
##    createdAt = myDict['created_at']
##    if createdAt == '':
##    	ts = 'None'
##    else:
##        print 'CREATED_AT= %s'% createdAt 
##        #ts = datetime.strptime(str(createdAt),'%a %b %d %H:%M:%S +0000 %Y').strftime('%a %b %d %H:%M:%S +0000 %Y')
##        ts = (datetime.datetime.strptime(str(createdAt),'%a %b %d %H:%M:%S +0000 %Y')- datetime.datetime(2011,1,12)).total_seconds()
##        print 'TS= ',ts
##        ts = ts - 1276940494
##    	
##    timeZone = myDict['time_zone']
##    if timeZone == '':
##    	timeZone = 'None'
##    	
##    description = myDict['description']
##    if description == '':
##        description  = 'None'
##        
##    location = myDict['location']
##    if location == '':
##        location = 'None'
##        
##    statusCount = myDict['statuses_count']
##    if statusCount == '':
##    	statusCount = 0
##    	
##    friendsCount = myDict['friends_count']
##    if friendsCount == '':
##    	friendsCount = 0
##    
##    utcOffset = myDict['utc_offset']
##    if utcOffset == '':
##    	utcOffset = 'None'
##    	
##    language = myDict['lang']
##    if language == '':
##    	language = 'None'
##    
##    favouritesCount = myDict['favourites_count']
##    if favouritesCount == '':
##    	favouritesCount = 0
    
    #val= userID,'|%',userName,'|%',screenName,'|%',followersCount,'|%',listedCount,'|%',location,'|%',ts,'|%',timeZone,'|%',description,'|%',statusCount,'|%',friendsCount,'|%',utcOffset,'|%',favouritesCount,'|%',language,'$\n'
    val= userID, '\n'
    print 'val= ',val
    val=map(unicode,val)
    val=" ".join(val)
    fp2.write(val)
    
 
  
for line in fp1:
    try:
        
    	line = line.rstrip()
    	#print line
    	#fp2.write(line)
    	myDict = ast.literal_eval(line)
	print 'Tweet ID= ', myDict['id']
        entities = myDict['entities']
	print 'entities'
        mention = entities['user_mentions']
	print 'len of mention= ', len(mention)
        
	for count in range(0,len(mention)):
		processUser(mention[count])
		print ' mention is done'
		
    	#myDict = myDict['user']
    	#print 'myDict1= ',myDict
    	#t1=processTweet(myDict)
    	#processUser(user)
        #print 'myDict2= ',myDict
    	#myDict = ast.literal_eval(line)
    	#if mini > t1 or mini == None :
    	#	mini=t1
   	# if myDict.get('retweeted_status')!=None:
    		#myDict=myDict['retweeted_status']
    		#processUser(myDict['user'])
    		#print 'myDict3= ',myDict
        	#t1 = processTweet(myDict['retweeted_status'])
        #if mini > t1 or mini == None :
    	#	mini=t1

#print mini
    except Exception as e:
        #fp2.write(line + '\n')
        print 'something went wrong in the tweet'

fp1.close()
fp2.close()
