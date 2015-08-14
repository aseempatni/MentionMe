from twython import Twython, TwythonError, TwythonRateLimitError
import json
import sys


argList = sys.argv
filename1 = 'user33.txt'  #argList[3]   # will contain the username 
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

apiKey = 'Tl4x7q0fMxTTnwU4gacWOaTBW'    #str(argList[1])
accessToken = 'AAAAAAAAAAAAAAAAAAAAAA2BewAAAAAABUUGEYgpIQ1z056Xaib2hyrc6mI%3DTjG1tqzGOv7PfiTJAjPtkA2AmVkw4gqmPduB4UnIteNK2xEpAw'         #str(argList[2])

twitter = Twython(apiKey,access_token = accessToken,client_args = client_args)

for user in userIDs:
    cur = -1
    friendList = []
    
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
