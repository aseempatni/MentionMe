import json
import subprocess

config_file = open('config.json','r')
configs = json.load(config_file)
config_file.close()

keys = configs['keys']

def spawn_crawlers(keys):
    for key in keys:
        in_file = 'all_user_ids.json'
        try:
            subprocess.Popen(["python", "crawl_friends.py",key['app_key'],key['app_secret'],in_file])
        except:
            print "Error: unable to start thread"

spawn_crawlers(keys)
