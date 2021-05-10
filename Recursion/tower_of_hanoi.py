'''
Created on Aug 10, 2017

@author: coditum
'''
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        printMove(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def printMove(fp,tp):
    print("move from",fp,"to",tp)

moveTower(8,"A","C","B")