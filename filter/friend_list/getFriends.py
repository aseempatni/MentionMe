from twython import Twython, TwythonError, TwythonRateLimitError
import json
import sys


argList = sys.argv
filename1 = 'user1'  #argList[3]   # will contain the username 
filename2 = 'out33'   #argList[4] # will contain the output friend list
fp1 = open(filename1,'r')
fp2 = open(filename2,'w')
userIDs = []

client_args = {
	'timeout': 120
  }
  
for line in fp1:
        user = int(line.rstrip())
        userIDs.append(user)


APP_KEY =  'bkIHr7FQg6uoWkPUQIHTisPCC'            #argList[1]    # App Key or Consumer Key (API Key)
APP_SECRET = 'lX5x9siCGTQ0pvbaxClomJXySUL0Av1pZG0cRKr9itTh6kStT5'              #argList[2]   # App secret or Consumer Secret (API Secret)



twitter = Twython(APP_KEY,APP_SECRET,oauth_version=2)
print twitter
ACCESS_TOKEN = twitter.obtain_access_token()
print 'access_token= ',ACCESS_TOKEN



twitter = Twython(APP_KEY,access_token = ACCESS_TOKEN,client_args = client_args)

for user in userIDs:
    cur = -1
    friendList = []
    fp2.write(user + ',')
    while cur != 0:
        try:
            response = twitter.get_friends_ids(user_id=user,count=5000,cursor = cur)
            print response
        except Exception as e:
            print e
            continue
        cur = response['next_cursor']
        friendList = friendList + response['ids']
    
    if cur != 0:
        continue
    dictionary = {}
    dictionary[str(user)] = friendList
    fp2.write("{0}\n".format(dictionary))

fp1.close()
fp2.close()
