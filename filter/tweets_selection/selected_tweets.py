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
#fp2 = open('All_userIDs.txt','r')
fp3 = codecs.open('original23_tweets.txt','w',encoding='utf-8');
#count = 0



def processUser(tweet_status,myDict):
    try:

    	tweetID = tweet_status['id']
    	print 'tweetID= ',tweetID
    	#print 'typeID= ',type(tweetID)
    	if tweetID == '':
	        print 'Tweet id not available'
   		tweetID = -1
    	
    	fp2 = open('All_userIDs.txt','r')
    	for ids in fp2:
             
			ids = ids.rstrip()
			#print 'ids= ',ids
			ids = int(ids)
			#print 'ids= ',type(ids)	
                        #break
			if tweetID == ids:
				#val=" ".join(val)
				fp3.write(str(myDict) + '\n')   #tweetID
				print 'written in file'
        	                break
                        #else:
                                #print 'In else'
    except Exception as e:
	                print 'from def ',e
    #print "Tweet Id don't match"
    fp2.close()


for line in fp1:
    try:
        
    	line = line.rstrip()
    	#print line
    	#fp2.write(origin)
    	myDict = ast.literal_eval(line)
        #print 'Successfully converted into dictionary'
    	#myDict = myDict['user']
    	#print 'myDict1= ',myDict
    	#t1=processTweet(myDict)
    	#processUser(myDict)
    	#print 'myDict2= ',myDict
    	#myDict = ast.literal_eval(line)
    	#if mini > t1 or mini == None :
    	#	mini=t1
   	if myDict.get('retweeted_status',None) != None:
    		tweet_status = myDict['retweeted_status']
                #print 'under IF'
    		processUser(tweet_status,myDict)
	else:
		print 'does not contain retweetd_status'
    		#print 'myDict3= ',myDict
        	#t1 = processTweet(myDict['retweeted_status'])
        #if mini > t1 or mini == None :
    	#	mini=t1

#print mini
    except Exception as e:
        fp3.write('THIS TWEET IS INCOMPLETE. PLEASE REPLACE IT--' + line + '\n')
        print e

fp1.close()
#fp2.close()fp3.close()
