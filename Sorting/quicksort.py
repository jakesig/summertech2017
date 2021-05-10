'''
Created on Aug 10, 2017

@author: coditum
'''
import random
mylist=[1,3,4,5,3,1,4,5,6,6,4,4,6,3,4,6,7,8,8,5,4,2,2,4,6,6,3,3,6,7]
def quicksort(alist):
    left=[]
    right=[]
    pivotlist= []
    if len(alist) == 1 or len(alist) == 0:
        return alist
    else:
        rand=random.randint(0,len(alist)-1)
        pivot = alist[rand]
        for j in range(len(alist)-1):
            if j == rand:
                pivotlist.append(pivot)
            if alist[j] < pivot:
                left.append(alist[j])
            elif alist[j]>=pivot:
                right.append(alist[j])
        return quicksort(left) +pivotlist+ quicksort(right)
print(quicksort(mylist))

        
