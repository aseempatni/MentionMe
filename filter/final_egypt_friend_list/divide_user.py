# this program will divide the users into 33 files named user1,user2,user3 etc

fp1 = open('egypt_users_unique.txt','r')

cur = 1
for counter in range(1,34):
    max = 7298 * counter
    print 'counter= ',counter
    print 'max= ',max
    with open('user{0}.txt'.format(counter),'w') as f:
        for user in fp1:
            if cur <= max:
                name = user.rstrip()
                print 'name= ',name
                print cur
                f.write(name + '\n')
                if cur == max:
                    cur += 1 
                    print 'cut out'
                    break
            cur += 1      
                         
    f.close()
fp1.close()
                        
                         
                          
                         
            
            
 
