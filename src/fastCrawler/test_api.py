# testing twitter APIs
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

user = 16388972
key = {
    "app_key": "dI2Ed6y0U9pn0f1kEQvGLXnIl",
    "app_secret": "YdFcoL0R88iGfSaiFGVPY5YSx0ouG5xvHjgfwcvh7r0UOCkYJe"
}

def crawl_user_data(user):
    # Crawl user friends
    cursor = ''
    while True:
        try:
            if cursor=='':
                friends = twitter.get_friends_ids(user_id=user,count=5000)
            else:
                friends = twitter.get_friends_ids(user_id=user,count=5000,cursor=cursor)
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

# read sys args
app_key = key["app_key"]
app_secret = key["app_secret"]

# initialize twython
twitter = Twython(app_key, app_secret, oauth_version=2,client_args=client_args)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(app_key, access_token=ACCESS_TOKEN)

crawl_user_data(user)
