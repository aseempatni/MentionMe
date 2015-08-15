#!/usr/bin/env python

from twython import Twython
import time
import sys

#argList = sys.argv
#fp1 = open('bachuFollower.txt','a')
'''fp1 = open('error100.txt','w')
fp2 = open(argList[4],'w')  # outputfile containing the list of all friends
fp3 = open(argList[3],'r')  # input file containing the list of specified userIds '''
APP_KEY = 'GSNIeSGknjrZSttJvkmKWZhHM'      #argList[1]    # App Key or Consumer Key (API Key)
APP_SECRET = 'xqdUjNJxHe1aY0qjucGs6oDHFDRDtI430P8Kx7ISoB8On7r7PJ'                 #argList[2]   # App secret or Consumer Secret (API Secret)

twitter = Twython(APP_KEY,APP_SECRET,oauth_version=2)
print twitter
ACCESS_TOKEN = twitter.obtain_access_token()
print 'access_token= ',ACCESS_TOKEN

client_args = {
	'timeout': 120
  }

twitter = Twython(APP_KEY,access_token=ACCESS_TOKEN, client_args=client_args)
print twitter
cursor = -1
while cursor != 0:
	try:
		response = twitter.get_friends_ids(user_id=18936583, cursor=cursor, count=5000)
		print response
		cursor = response['next_cursor']
		print 'cursor= ',cursor
		#cursor = -1
		#response = twitter.get_friends_ids(user_id=17285399, cursor=cursor, count=5000)
		#cursor = -1
		#re = twitter.get_lastfunction_header('x-rate-limit-remaining') 
		re = twitter.get_application_rate_limit_status(resources='friends')
		print 're= ',re
		print 'completed here'
	except Exception as e:
		print e
	
#print ttter.search(q='python',result_type='popular')

#fp.write(str(twitter.search(q='python',result_type='popular')))
'''
for user in fp3:
            
            user = user.rstrip()
            print 'user= ',user
            fp2.write(user + ',')
            cursor = -1
            while cursor != 0:
                try:
                    
                    print 'in WHILE'
                    time.sleep(80)
                    response = twitter.get_friends_ids(user_id=int(user), cursor=cursor, count=5000)
                    
                    ids = response['ids']
                    
                    
                    print 'X-RateLimit-Limit= ',response['X-RateLimit-Limit']
                    print 'X-RateLimit-Remaining= ',response['X-RateLimit-Remaining']
                    print 'X-RateLimit-Class= ',response['X-RateLimit-Class']
                    #print ids
                    cursor = response['next_cursor']
                    print cursor
                    for x in ids:
                    	fp2.write(str(x) + ',')
                    if cursor == 0:
                    	fp2.write('\n')
                    print 'X-Warning= ',response['X-Warning']
                except Exception as e:
                        print 'Bachu says ',e
                        print 'exception occurs for ',user
                        
                
                
                    
                
                



fp2.close()
fp3.close()
fp1.close()
'''

