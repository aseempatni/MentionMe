import argparse
import init
import stats
from utils import *

# argument parser
parser = argparse.ArgumentParser(description='The fastest Twitter crawler.')
parser.add_argument('--stats', dest='stats', action='store_const',
                           const=sum, default=False,
                                              help='Get stats of crawled data')
parser.add_argument('--init', dest='init',action='store_const',const=True,default=False,help="Initialize the crawler")
args = parser.parse_args()

# select action based on arguments
if args.stats:
    users = get_users_list_from("all_user_ids.json")
    print stats.get_stats(users)
if args.init:
    init.init()
