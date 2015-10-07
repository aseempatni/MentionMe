import sys
import time
from twython import Twython, TwythonRateLimitError
#import config
import json
import thread
import os

# read config
config_file = open('config.json','r')
configs = json.load(config_file)
config_file.close()

# apply config
client_args = configs['client_args']
keys = configs['keys']

def log(user, msg) :
    print user,':', msg

def file_name_for(user):
    file_name = '../../data/friend_id/'+str(user)
    return file_name

def get_users_list_from(in_file):
    f = open('../../data/split_input/'+in_file)
    all_users = json.load(f)
    return all_users

def crawl_user_data(user):
    # Crawl user friends
    out = open(file_name_for(user),'w')
    friends = twitter.get_friends_ids(user_id=user,count=5000)
    json.dump(friends,out)
    log (user,"done now")

def crawl_more_friends(user):
    log(user,"TODO: crawl more friends for user: "+user)

# checks if the user has 5000 friends
def should_crawl_more_friends(user):
    file_name = file_name_for(user)
    if os.path.isfile(file_name):
        if os.stat(file_name).st_size != 0:
    	    with open(file_name,'r') as friends:
    	        x = json.load(friends)
                if len(x["ids"]) >=5000:
                    return True
    return False

def should_we_crawl(user):
    file_name = file_name_for(user)
    # if a file exists then we have already tried to crawl the data
    if os.path.isfile(file_name):
        log(user,"already tried.")
        # if the file is empty, then we should retry
        if os.stat(file_name).st_size == 0:
            log(user,"file empty, retrying")
            return True
        else:
            return False
    # file doesn't exist, then we should crawl
    else:
        return True

def start_crawler_old(users):
    i=0
    while i<len(all_users):
        user = all_users[i]
        i+=1
        if should_we_crawl(user):
            try:
                crawl_user_data(user)
            except TwythonRateLimitError:
                # rate limit reached
                reset = int(twitter.get_lastfunction_header('x-rate-limit-reset'))
                msg =  "waiting for "+str(reset - time.time())+ ' sec'
                log(user,msg)
                wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
                time.sleep(wait)
                i-=1
            except Exception as e:
                # other exceptions
                log(user,e.__doc__+" "+ e.message)


def crawl_user_friends(user):
    # Crawl user friends
    friendfile = open("output/"+str(user),'a+')
    cursor = ''
    while True:
        try:
            if cursor=='':
                friends = twitter.get_friends_ids(user_id=user,count=5000)
            else:
                friends = twitter.get_friends_ids(user_id=user,count=5000,cursor=cursor)
            json.dump(friends,friendfile)
            cursor = friends['next_cursor_str']
            print cursor
            if cursor=='0':
                # all friends done
                break
        except TwythonRateLimitError:
            # rate limit reached
            reset = int(twitter.get_lastfunction_header('x-rate-limit-reset'))
            msg =  "waiting for "+str(reset - time.time())+ ' sec'
            print msg
            wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
            time.sleep(wait)
        except Exception as e:
            # other exceptions
            print e.__doc__+" "+ e.message
            break
    friendfile.close()

# read sys args
app_key = sys.argv[1]
app_secret = sys.argv[2]
in_file = sys.argv[3]
process_number = int(sys.argv[4])

# initialize twython
twitter = Twython(app_key, app_secret, oauth_version=2,client_args=client_args)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(app_key, access_token=ACCESS_TOKEN)

all_users = get_users_list_from(in_file)

max_process=10

# start crawler
def crawl():
    print "Crawler initialized:" ,sys.argv[1], sys.argv[2]
    start_crawler(all_users)

def crawl_more():
    print "Crawling friends" ,sys.argv[1], sys.argv[2], sys.argv[4]
    i=0
    count=0
    while i<len(all_users):
	if i%max_process==process_number:
        	user = all_users[i]
        	if should_crawl_more_friends(user):
        	    crawl_user_friends(user)
		    count+=1
	i+=1
crawl_more()
