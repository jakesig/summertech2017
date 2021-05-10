'''
Created on Aug 10, 2017

@author: coditum
'''
mylist=list(range(1,100))

def bianary(lista,numtofind):
    lownum=0
    highnum=len(lista)
    while lownum<=highnum:
        mid=int((lownum+highnum)/2)
        print(mid)
        print(numtofind)
        if mid==numtofind:
            return mid
            break
        elif lista[mid]<numtofind:
            lownum=mid+1
        else:
            highnum=mid+1
    return 1
bianary(mylist,75)


            
            
            
    
        
        
    
    
    
    
    