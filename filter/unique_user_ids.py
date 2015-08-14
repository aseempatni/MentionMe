#!/usr/bin/env python
# program to remove duplicate user ids from the 
#print 'form begining part10'
#before = [23,34,45,67,78,90,23,67,12,47]
#after = [23]
#fp1 = open('tweet_mention_id23.txt','r')
fp1 = open('filtered_user_id.txt','r')

for i in fp1:
    try:
		flag = 1
		fp2 = open('unique_user2_ids.txt','a+')
		for j in fp2:
			print 'i= ',i
			print 'j= ',j
			if i == j:
				flag = 0
				print 'already present!'
				break
		print 'End j loop here'
		print 'flag= ',flag
		if flag:
			fp2.write(i)
			print 'Appended in the new list'
		print 'Bachu'
		fp2.close()
		
    except Exception as e:
	        print e
print 'end i loop here'		
			
fp1.close()			
#print 'before= ',before
#print 'after= ',after
