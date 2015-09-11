import json
import os

def log(user, msg) :
    print user,':', msg

def get_users_list_from(in_file):
    f = open('../../data/split_input/'+in_file)
    all_users = json.load(f)
    return all_users

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
    stats = {}
    stats["zero_size"] = 0
    stats["done"] = 0
    stats["missing"] = 0
    stats["exists"] = 0
    stats["total"] = 0
    stats["contain_data"] = 0

    for user in users:
        stats["total"] += 1
        file_name = file_name_for(user)
        if os.path.isfile(file_name):
            stats["exists"] += 1
            if os.stat(file_name).st_size == 0:
                stats["zero_size"] += 1
            else:
                stats["done"] += 1
                if os.stat(file_name).st_size >= 4096:
                    stats["contain_data"] += 1
        else:
            stats["missing"] += 1
    return stats


def file_name_for(user):
    file_name = '../../data/friend_id/'+str(user)
    return file_name

users = get_users_list_from("all_user_ids.json")
print get_stats(users)
