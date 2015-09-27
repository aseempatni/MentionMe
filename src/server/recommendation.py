# This is the file server imports and calles the method get to serve requests

import sys
import os
sys.path.append(os.path.abspath('../scripts'))
from recommend_mention import *
import operator
import username

def init_rec():
	init()

def get(tweet):
    	# Get recommendations for mention given a tweet
    	# Return a list of users
    	reco = recommend_mention(tweet)
    	sorted_x = sorted(reco.items(), key=operator.itemgetter(1))
	print "sorted x", sorted_x
	print "======================================="
    	user_ids = [i[0] for i in sorted_x[0:10]]
	response = []
        for user_id in user_ids:
            user = {}
            name = username.get(user_id)
            user["name"] = name
            user["id"] = user_id
	    print user
            response.append(user)
	print "======================================="
	return response
    	return ['PatniAseem','agnivo_saha']

if __name__ == "__main__":
	init()
	get("latest news protests bahrain libya algeria egypt yemen iran visit hyperlink")
