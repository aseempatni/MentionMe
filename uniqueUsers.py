from sets import Set
filename = "friendCount.txt"

fp = open(filename,'r')

userSet = Set([])
for line in fp:
	userID = line.split()[0]
	friendCount = int(line.split()[1].rstrip())
	userSet.add((friendCount,userID))
userSet = sorted(userSet)

for user in userSet:
	if user[0]>0 and user[0]<10000:
		print user[1]
