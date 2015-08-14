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
fp2=codecs.open('filtered_user_id.txt','w',encoding='utf-8');
#count = 0

def processUser(myDict):
    
    userID = myDict['id']
    if userID == '':
        print 'User id not available'
    	userID = -1

    val= userID, '\n'
    print 'val= ',val
    val=map(unicode,val)
    val=" ".join(val)
    fp2.write(val)
    
 
  
for line in fp1:
    try:
        
    	line = line.rstrip()
    	
    	myDict = ast.literal_eval(line)
        user = myDict['user']
        
    	
    	processUser(user)
        


    except Exception as e:
        fp2.write(line + '\n')
        print 'something went wrong in the tweet'

fp1.close()
fp2.close()
