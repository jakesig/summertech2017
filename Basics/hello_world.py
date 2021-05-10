'''
Created on Aug 7, 2017

@author: summertech
'''
import random
num=random.randint(1,10)
def newguess():
    while True:
        try:
            guess=int(input("Guess a number! "))
        except ValueError:
            print ("That is not a number... Try again!")
            continue
        break
    while True:
        print (guess)
        if guess<num:
            print ("That number is too low!")
            while True:
                try:
                    guess=int(input("Guess a number! "))
                except ValueError:
                    print ("That is not a number... Try again!")
                    continue
                break
        elif guess>num:
            print ("That number is too high!")
            while True:
                try:
                    guess=int(input("Guess a number! "))
                except ValueError:
                    print ("That is not a number... Try again!")
                    continue
                break
        elif guess==num:
            print ("You got it! My number was {}".format(num)) 
            break

def wannaplay():
    play=input("Hello, Would You Like to Play JAKES SPECTACULAR NUMBER GUESSING GAME?? (y/n)")
    play=play.lower()    
    while True:
        if play=="y":
            print ("Alright, Here We GO!")
            newguess()
            break
        elif play=="n":
            print("OK... GOODBYE!! :(")
            break
        else:
            print("please print y or n (no spaces)")
            play=input("Hello, Would You Like to Play JAKES SPECTACULAR NUMBER GUESSING GAME?? (y/n)")
            play=play.lower()
wannaplay()
