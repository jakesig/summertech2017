'''
Created on Aug 10, 2017

@author: coditum
'''
import time
haii=0
x=0
mylist=[1,4,2,5,6,2,7,9,3,6,6,3,6,6,4,6,4,5,7,8,4,2,5,7,9,3,4,5,3,2,3,3,4,5,5,4,3,5,5,4,3,3,3]
def sort(mylist):
    haii=0
    print("YOU CHOSE...")
    time.sleep(3)
    print("YOU CHOSE TO MAKE ME SORT SOMETHING")
    time.sleep(3)
    print("WHY?")
    time.sleep(3)
    print("WELL, HERE I GO...")
    time.sleep(3)
    print(mylist)
    time.sleep(3)
    print("OOOPS...")
    time.sleep(3)
    while True:
        if mylist[haii+1]<mylist[haii]:
            x = mylist[haii]
            mylist[haii]=mylist[haii+1]
            mylist[haii+1] = x
            haii = 0
        haii+=1
        if haii>=len(mylist)-1:
            break
    print(mylist)
    time.sleep(3)
    print("NEVER ASK ME TO DO THAT AGAIN, IT HURTS...")
sort(mylist)