#!/usr/bin/env python
filename1 = "appDetail_accTok_modified_get_friends.txt"
filename2 = "modified_run_get_friends.sh"
counter = 1
maxCounter = 33

fp1 = open(filename1,'r')
fp2 = open(filename2,'w')


appKeys = []
for line in fp1:
	appKey = line.split(',')[0]
	appSecret = line.split(',')[1].rstrip()
	appKeys.append((appKey,appSecret))


print len(appKeys)
#print appKeys

while counter<= maxCounter:
        print 'appKey= ',appKeys[counter-1][0]
        print 'appSecret= ',appKeys[counter-1][1]
	fp2.write("python modified_get_friends.py {0} {1} {2} {3} &\n".format(appKeys[counter-1][0],appKeys[counter-1][1],'user'+str(counter)+'.txt', 'out'+str(counter)))
	counter += 1

