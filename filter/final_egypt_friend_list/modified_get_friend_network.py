#!/usr/bin/env python

#This produces the required set of friends for a given userId separated by '\n'.
#The first element in each newline is the provided userId so will alwyas be
# present in the unique userId set.
from function import linearSearch
import sys

argList = sys.argv 

fp1 = open(argList[1],'r')    # userIds of all friends for a given userId
fp2 = open(argList[2],'w')   #output file  

#convert all unique userId into a list of string to compare
fp3 = open('egypt_users_unique.txt','r') # given set of unique userIds
#integer = []
list_string = []
for j in fp3:
    string = j.rstrip().split(',')
    
    #print 'string= ',string
    list_string.append(string[0])
    #integer.append(map(int,string))
    #print 'interger from= ',list_string

#print "unique_userIds",integer
print 'Total unique users= ',len(list_string)
 # End Here
count = 1
#fp2.write('\n starts from here \n')
for line in fp1:
    # use only for getFriennds.py
    #friend_str_list = line.replace('[','').replace(']','').rstrip().split(',')
    friend_str_list = line.rstrip().split(',')
    #print 'friend_list= ',friend_str_list
    print 'user number= ',count
    if friend_str_list == '':
        fp2.write('\n')    #seprating friend list for each user
        continue
    
    

    #fp2.write('\n' + friend_str_list[0] + ',')
    for i in friend_str_list:      #linear search starts here
        print 'i= ' + i
        flag = linearSearch(i,list_string)    #this function is contained in the program named function.py
        print 'flag=',flag
        if flag: 
           fp2.write(str(i) + ',')
           print 'written in file'
    fp2.write('\n\n')    #linear search ends here
     
    #intcreate = ','.join(create_str_list)
    #print intcreate
    #print createList
    #fp2.write(intcreate + '\n')
    print 'friend network for ' + friend_str_list[0] + 'created' 
    count += 1

fp2.close()
fp1.close()

'''
    last = friend_str_list[-1]
    str_last = last.rstrip('\n') # removing '\n' from the last friend userId
    friend_str_list[-1] = str_last
    print "createList",friend_str_list
    
    # don not consider this
    item = map(int,friend_str_list)    # Converts string list into integer list
    print "item",item
    '''

