# This is the file server imports and calles the method get to serve requests

import sys
import os
sys.path.append(os.path.abspath('../scripts'))
from recommend_mention import *

def get(tweet):
    # Get recommendations for mention given a tweet
    # Return a list of users
    reco = recommend_mention(tweet)
    return reco
    return ['PatniAseem','agnivo_saha']
