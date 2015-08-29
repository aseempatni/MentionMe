import sys
import time
from twython import Twython, TwythonRateLimitError
#import config
import json
import thread

config_file = open('config.json','r')
configs = json.load(config_file)
config_file.close()

client_args = configs['client_args']
keys = configs['keys']

def log(user, msg) :
    print user,':', msg

def start_crawler(app_key, app_secret, in_file):
    f = open('../../data/split_input/'+in_file)
    all_users = json.load(f)
    twitter = Twython(app_key, app_secret, oauth_version=2,client_args=client_args)
    ACCESS_TOKEN = twitter.obtain_access_token()
    twitter = Twython(app_key, access_token=ACCESS_TOKEN)

    i=0
    while True and i<len(all_users):
        user = all_users[i]
        try:
            friends = twitter.get_friends_ids(user_id=user,count=5000)
            #print friends
            out = open('../../data/friend_id/'+str(user),'w')
            json.dump(friends,out)
            i+=1
            log (user,i)
        except:
            reset = int(twitter.get_lastfunction_header('x-rate-limit-reset'))
            msg =  "waiting for "+str(reset - time.time())+ ' sec'
            log(user,msg)
            wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
            time.sleep(wait)

print "Crawler initialized:" ,sys.argv[1], sys.argv[2]
start_crawler(sys.argv[1], sys.argv[2],sys.argv[3])
