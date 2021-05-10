'''
Created on Aug 9, 2017

@author: coditum
'''
def count(num):
    if num == 1:
        return 1
    return count(num-1)*num


a=input("WOULD YOU LIKE TO USE JAKE'S SPECTACULAR FACTORIAL CALCULATOR? (y or n)")

if a.upper()=="Y":
    c=int(input("Which Factorial?"))
    print(count(c))
elif a.upper()=="N":
    print("OK BYE...")

