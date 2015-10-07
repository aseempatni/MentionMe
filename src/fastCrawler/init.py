import json
import subprocess
import time

def init():

    # Get the required configurations
    config_file = open('config.json','r')
    configs = json.load(config_file)
    config_file.close()

    keys = configs['keys']

    # Start the crawler
    spawn_crawlers(keys)


def spawn_crawlers(keys):

    in_file = 'all_user_ids.json'
    i=0

    # start a crawler with each key
    for key in keys:

        # try to spawn a new crawler with the keu
        try:
            subprocess.Popen(["/usr/bin/python2.7", "crawl_friends.py",key['app_key'],key['app_secret'],in_file,str(i)])
        except:
            print "Error: unable to start thread"

        # eait for 60 seconds before spawning next thread
	i+=1
        time.sleep(60)


if __name__ == "__main__":
    init()
