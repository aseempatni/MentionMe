import json
import os
from collections import defaultdict
import matplotlib.pyplot as plt
from utils import *
def should_we_crawl(user):
    file_name = file_name_for(user)
    # if a file exists then we have already tried to crawl the data
    if os.path.isfile(file_name):
        # log(user," already tried.")
        # if the file is empty, then we should retry
        if os.stat(file_name).st_size == 0:
            # log(user,"file empty, retrying")
            return True
        else:
            return False
    # file doesn't exist, then we should crawl
    else:
        return True

def get_stats(users):
    stats = {
            "zero_size": 0,
            "done" : 0,
            "missing" : 0,
            "exists" : 0,
            "total" : 0,
            "contain_data" : 0
            }
    count=0
    d = defaultdict(int)
    for user in users:
        count+=1
	stats["total"] += 1
        file_name = file_name_for(user)
        if os.path.isfile(file_name):
            stats["exists"] += 1
            if os.stat(file_name).st_size == 0:
                stats["zero_size"] += 1
            else:
                stats["done"] += 1
		with open(file_name,'r') as friends:
			#print count,user
			x = json.load(friends)
			d[len(x["ids"])] +=1
			# print x["next_cursor_str"]
                if os.stat(file_name).st_size >= 4096:
                    stats["contain_data"] += 1
        else:
            stats["missing"] += 1
    print d
    plot = False
    if plot:
        d.pop(5000)
        d.pop(0)
        d.pop(1)
        plt.plot( d.values() )
        #plt.yscale('log')
        #plt.xscale('log')
        plt.xlabel('No of friends')
        plt.ylabel('No of users')
        plt.savefig('Frequency')
        plt.show()
    return stats

def file_name_for(user):
    file_name = '../../data/friend_id/'+str(user)
    return file_name

if __name__ == "__main__":
    users = get_users_list_from("all_user_ids.json")
    print get_stats(users)
