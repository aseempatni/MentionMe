#!/usr/bin/env python
def linearSearch(myItem,myList):
    found = False
    position = 0
    #print 'myItem= ',myItem
    #print 'lenthh of myList= ',len(myList)
    while position < len(myList) and not found:
        #print 'position= ',position
        #print 'myList[position]= ',myList[position][0]
        if myList[position] == myItem:
            found = True
        position += 1
    return found


