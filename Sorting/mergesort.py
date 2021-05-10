'''
Created on Aug 10, 2017

@author: coditum
'''

def bubblesort(mylist):
    haii=0
    while True:
        if mylist[haii+1]<mylist[haii]:
            x = mylist[haii]
            mylist[haii]=mylist[haii+1]
            mylist[haii+1] = x
            haii = 0
        haii+=1
        if haii>=len(mylist)-1:
            return mylist

listtosort=[1,4,2,4,3,6,5,3,5,2,6,3,5,2,4,2,4,2,4,4,6,7,5,4,6,5,3,4,6,6,4,4,4,4,4,4,4,4,3,2,2,2,3,4,5,5,7,8,8]
def mergesort(listtosort):
    pt1 = []
    pt2 = []
    sor = []
    if len(listtosort)>1:
        mid=int(len(listtosort)/2)
        pt1=list(listtosort[:mid])
        pt2=list(listtosort[mid:])
        return bubblesort(mergesort(pt1) + mergesort(pt2))
       
    elif len(listtosort)<=1:
        return listtosort
print(mergesort(listtosort))






