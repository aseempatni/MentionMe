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

filename1 = "Tweets.txt"
fp1 = codecs.open(filename1, encoding='utf-8')
fp2 = open('All_userIDs.txt','r')
fp3 = codecs.open('original_tweets.txt','w',encoding='utf-8');
#count = 0

def processUser(myDict):
    
    tweetID = myDict['id']
    print 'tweetID= ',tweetID
    print 'typeID= ',type(tweetID)
    if tweetID == '':
        print 'Tweet id not available'
    	tweetID = -1
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
    #val= tweetID, '\n'
    #print 'early_val= ',val
    #val = map(unicode,val)
    #print 'after_val= ',val
    try:
    	for ids in fp2:
			ids = ids.rstrip()
			#print 'ids= ',ids
			ids = int(ids)
			#print 'ids= ',type(ids)	
			if tweetID == ids:
				#val=" ".join(val)
				fp3.write(tweetID)
				print 'written in file'
        	                break
    	print 'TWEET ID DON"T MATCH'
    except Expression as e:
	print 'from def ',e
  
for line in fp1:
    try:
        
    	line = line.rstrip()
    	#print line
    	#fp2.write(origin)
    	myDict = ast.literal_eval(line)
        print 'up to here good'
    	#myDict = myDict['user']
    	#print 'myDict1= ',myDict
    	#t1=processTweet(myDict)
    	#processUser(myDict)
    	#print 'myDict2= ',myDict
    	#myDict = ast.literal_eval(line)
    	#if mini > t1 or mini == None :
    	#	mini=t1
   	if myDict.get('retweeted_status',None) != None:
    		myDict=myDict['retweeted_status']
                print 'under IF'
    		processUser(myDict)
	else:
		print 'does not contain retweetd_status'
    		#print 'myDict3= ',myDict
        	#t1 = processTweet(myDict['retweeted_status'])
        #if mini > t1 or mini == None :
    	#	mini=t1

#print mini
    except Exception as e:
        fp3.write(line + '\n')
        print e

fp1.close()
fp2.close()fp3.close()
