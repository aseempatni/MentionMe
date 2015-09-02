import sys

def main() :
        users = {}
        out_file = open('UserTweetMapping.txt', 'w')
        with open(sys.argv[1], 'r') as f:
                for line in f:
                        try:
                                mydict = eval(line)
                                if 'id' not in mydict['user'] :
                                        print line
                                        sys.exit(1)
                                if mydict['user']['id'] not in users :
                                        users[mydict['user']['id']] = []
                                        users[mydict['user']['id']].append(mydict['id'])
                                else :
                                        users[mydict['user']['id']].append(mydict['id'])
                        except Exception as e :
                                print e
        out_file.write(str(users))

if __name__ == "__main__" :
        main()