import sys
import time
from twython import Twython, TwythonRateLimitError
#import config
import json
import thread
import os

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
        file_name = '../../data/friend_id/'+str(user)
        if os.path.isfile(file_name):
            log(user,str(i) + " data already present")
        else:
            try:
                # Crawl user friends
                out = open(file_name,'w')
                friends = twitter.get_friends_ids(user_id=user,count=5000)
                json.dump(friends,out)
                log (user,i)
            except:
                # rate limit reached
                 reset = int(twitter.get_lastfunction_header('x-rate-limit-reset'))
                 msg =  "waiting for "+str(reset - time.time())+ ' sec'
                 log(user,msg)
                 wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
                 time.sleep(wait)
                 i-=1
        i+=1


print "Crawler initialized:" ,sys.argv[1], sys.argv[2]
start_crawler(sys.argv[1], sys.argv[2],sys.argv[3])
