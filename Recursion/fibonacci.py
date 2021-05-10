'''
Created on Aug 10, 2017

@author: coditum
'''
def count(num):
    if num == 1:
        return 1
    if num==2:
        return 2
    if num==3:
        return 3
    return count(num-1)+(count(num-2))
print(count(8))
