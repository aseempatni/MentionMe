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

filename3 = "Tweets.txt"
fp1 = codecs.open(filename3, encoding='utf-8')
fp2=codecs.open('All_userIDs.txt','w',encoding='utf-8');
count = 0

def processUser(myDict):
    
    userID = myDict['id']
    if userID == '':
    	userID = -1
    
    userName = myDict['name']
    if userName == '':
    	userName = 'None'
    	
    screenName = myDict['screen_name']
    if screenName == '':
    	screenName = 'None'	
    	
    followersCount  = myDict['followers_count']
    if followersCount == '':
    	followersCount = 0
    	
    listedCount = myDict['listed_count']
    if listedCount == '':
    	listedCount = 0
    	
    createdAt = myDict['created_at']
    if createdAt == '':
    	ts = 'None'
    else:
    	ts = int(datetime.strptime(str(createdAt),'%a %b %d %H:%M:%S +0000 %Y').strftime('%s'))
    	ts = ts - 1276940494
    	
    timeZone = myDict['time_zone']
    if timeZone == '':
    	timeZone = 'None'
    	
    description = myDict['description']
    if description == '':
        description  = 'None'
        
    location = myDict['location']
    if location == '':
        location = 'None'
        
    statusCount = myDict['statuses_count']
    if statusCount == '':
    	statusCount = 0
    	
    friendsCount = myDict['friends_count']
    if friendsCount == '':
    	friendsCount = 0
    
    utcOffset = myDict['utc_offset']
    if utcOffset == '':
    	utcOffset = 'None'
    	
    language = myDict['lang']
    if language == '':
    	language = 'None'
    
    favouritesCount = myDict['favourites_count']
    if favouritesCount == '':
    	favouritesCount = 0
    
    #val= userID,'|%',userName,'|%',screenName,'|%',followersCount,'|%',listedCount,'|%',location,'|%',ts,'|%',timeZone,'|%',description,'|%',statusCount,'|%',friendsCount,'|%',utcOffset,'|%',favouritesCount,'|%',language,'$\n'
    val= userID, '\n'
    val=map(unicode,val)
    val=" ".join(val)
    fp2.write(val)
    
    
for line in fp1:
    line = line.rstrip()
    myDict = ast.literal_eval(line)
    myDict = myDict['user']
    #t1=processTweet(myDict)
    processUser(myDict)
    myDict = ast.literal_eval(line)
    #if mini > t1 or mini == None :
    #	mini=t1
    if myDict.get('retweeted_status')!=None:
    	myDict=myDict['retweeted_status']
    	processUser(myDict['user'])
        #t1 = processTweet(myDict['retweeted_status'])
        #if mini > t1 or mini == None :
    	#	mini=t1

#print mini
    
