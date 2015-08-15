#!/usr/bin/env python

from twython import Twython
import time
import sys

argList = sys.argv
#fp1 =      #open('bachuFollower.txt','a')
fp1 = open('error10.txt','w')
fp2 =  open('out10','w')  # outputfile containing the list of all friends
fp3 =  open('user10','r')  # input file containing the list of specified userIds 
APP_KEY = 'GSNIeSGknjrZSttJvkmKWZhHM'   # App Key or Consumer Key (API Key)
APP_SECRET = 'xqdUjNJxHe1aY0qjucGs6oDHFDRDtI430P8Kx7ISoB8On7r7PJ'  # App secret or Consumer Secret (API Secret)

twitter = Twython(APP_KEY,APP_SECRET,oauth_version=2)
print twitter
ACCESS_TOKEN = twitter.obtain_access_token()
print 'access_token= ',ACCESS_TOKEN

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
                    time.sleep(100)
                    response = twitter.get_friends_ids(user_id=int(user), cursor=cursor, count=5000)
                    
                    ids = response['ids']
                    cursor = response['next_cursor']
                    #print ids
                    print cursor
                    id_str = ','.join(str(x) for x in ids)
                    print id_str + ' have done'
                    if cursor == 0:
                        fp2.write(id_str + '\n\n')
                    else:
                        fp2.write(id_str + ',')
                except Exception as e:
                        print 'Bachu says ',e
                        print 'exception occurs for ',user
                        fp1.write('\nexception occurs for ' + user + '\ne')
                       
                
                
                    
                
                


fp1.close()
fp2.close()
fp3.close()


# to check for individual user's friend list

'''
fp2 = open('etc','a')
cursor = -1
fp2.write('102384789' + ',')
while cursor != 0:
    print 'in WHILE'
    #print twitter.get_friends_ids(user_id=102384789, cursor=cursor, count=5000)
    response = twitter.get_friends_ids(user_id=102384789, cursor=cursor, count=5000)
    ids = response['ids']
    cursor = response['next_cursor']
    print ids
    print cursor
    id_str = ','.join(str(x) for x in ids)
    print id_str + ' have done'
    if cursor == 0:
        fp2.write(id_str + '\n\n')
    else:
        fp2.write(id_str + ',')

fp2.close()

'''
