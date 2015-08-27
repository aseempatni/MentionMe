import time
from twython import Twython, TwythonRateLimitError
#APP_KEY = 'kDoXEJc9Wd3KsjwuKDn1IpvS'
#APP_SECRET = 'MqkxtuJVS2e23pUebbedodpvjaiNTRRSTymJ8dx5Rpt9BLJqH2'
APP_KEY = 'dI2Ed6y0U9pn0f1kEQvGLXnIl'
APP_SECRET = 'YdFcoL0R88iGfSaiFGVPY5YSx0ouG5xvHjgfwcvh7r0UOCkYJe'

client_args = {
            'proxies': {
            'http': 'http://10.3.100.207:8080',
            'https': 'https://10.3.100.207:8080',
     }
}

import json
f = open('../../data/all_user_ids.json')
all_users = json.load(f)

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2,client_args=client_args)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

i=0
while True and i<len(all_users):
    user = all_users[i]
    try:
        friends = twitter.get_friends_ids(user_id=user,count=5000)
        #print friends
        out = open('../../data/friend_id/'+str(user),'w')
        json.dump(friends,out)
        i+=1
        print i,"\r"
    except TwythonRateLimitError, e:
        reset = int(twitter.get_lastfunction_header('x-rate-limit-reset'))
        print "waiting for",reset - time.time() , 'time'
        wait = max(reset - time.time(), 0) + 10 # addding 10 second pad
        time.sleep(wait)
