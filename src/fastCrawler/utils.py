import json

def get_users_list_from(in_file):
    f = open('../../data/split_input/'+in_file)
    all_users = json.load(f)
    return all_users

def log(user, msg) :
    print user,':', msg


