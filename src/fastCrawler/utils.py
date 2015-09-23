import json
import requests

def get_users_list_from(in_file):
    f = open('../../data/split_input/'+in_file)
    all_users = json.load(f)
    return all_users

def log(user, msg) :
    print user,':', msg

def username_from_id(id):
    r = requests.post("http://tweeterid.com/ajax.php", data={"input":id})
    return r.text
