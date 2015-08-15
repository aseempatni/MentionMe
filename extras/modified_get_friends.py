#!/usr/bin/env python

from twython import Twython
import time
import sys

#argList = sys.argv
#fp1 =      #open('bachuFollower.txt','a')
fp1 = open('error11.txt','w')
fp2 =  open('out11','w')  #open(argList[4],'w')  # outputfile containing the list of all friends
fp3 =  open('user10','r')   #open(argList[3],'r')  # input file containing the list of specified userIds 
APP_KEY =  'JVFUSnxpJrdt2eTdx4Law8nA9'      #argList[1]    # App Key or Consumer Key (API Key)
APP_SECRET = 'Mbuq3quubukLbhx3tyBQwvveN6jiHXFcjfsWxoRGzMFGqggUDy'           #argList[2]   # App secret or Consumer Secret (API Secret)

twitter = Twython(APP_KEY,APP_SECRET,oauth_version=2)
print twitter
try:
	ACCESS_TOKEN = twitter.obtain_access_token()
	print 'access_token= ',ACCESS_TOKEN
except Exception as e:
	print e

client_args = {
	'timeout': 120
  }

twitter = Twython(APP_KEY,access_token=ACCESS_TOKEN)
print twitter

#print ttter.search(q='python',result_type='popular')

#fp.write(str(twitter.search(q='python',result_type='popular')))

for user in fp3:
            
            user = user.rstrip()
            #print 'user= ',user
            fp2.write(user + ',')
            cursor = -1
            while cursor != 0:
                try:
                    
                    print 'in WHILE'
                    time.sleep(80)
                    response = twitter.get_friends_ids(user_id=int(user), cursor=cursor, count=5000)
                    
                    ids = response['ids']
                    cursor = response['next_cursor']
                    #print ids
                    print cursor
                   # id_str = ','.join(str(x) for x in ids)
                    #print id_str + ' have done'
                    for x in ids:
                    	
                        fp2.write(str(x) + ',')
                    if cursor == 0:
                    	fp2.write('\n')	
                except Exception as e:
                		#time.sleep(100)
                        print 'Bachu says ',e
                        print 'exception occurs for ',user
                        fp1.write('\nexception occurs for ' + user + '\ne')
                       
                
                
                    
                
                


fp1.close()
fp2.close()
fp3.close()




