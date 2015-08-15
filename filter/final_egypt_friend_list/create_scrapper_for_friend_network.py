#!/usr/bin/env python


filename1 = "modified_run_get_friend_network.sh" 
fp1 = open(filename1,'w')
count = 1
maxCount = 33



while count<= maxCount:
        
	fp1.write("python modified_get_friend_network.py {0} {1} &\n".format('out'+str(count), 'friend_network'+str(count)))
	count += 1


fp1.close()
