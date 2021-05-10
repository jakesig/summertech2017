'''
Created on Aug 11, 2017

@author: coditum
'''
import random
import time
playagain=0
def checkforwin(card1,card2,p,card3=0):
    j=1
    total=0
    while True:
        if j==1:
            card=card1
        elif j==2:
            card=card2
        elif j==3:
            card=card3
        if str(card)=="2":
            total+=2
        elif str(card)=="3":
            total+=3
        elif str(card)=="4":
            total+=4
        elif str(card)=="5":
            total+=5
        elif str(card)=="6":
            total+=6
        elif str(card)=="7":
            total+=7
        elif str(card)=="8":
            total+=8
        elif str(card)=="9":
            total+=9
        elif str(card)=="10":
            total+=10
        elif str(card)=="Jack":
            total+=10
        elif str(card)=="Queen":
            total+=10
        elif str(card)=="King":
            total+=10
        elif str(card)=="Ace":
            total+=11
        if j==3:
            if total<21:
                print("Player {}'s Number Was Less Than 21... ({})".format(p,total))
                return total
                break
            elif total>21:
                if card1=="Ace" or card2=="Ace" or card3=="Ace":
                    total-=10
                    break
                print("Your Number Was Bigger Than 21...YOU LOSE")
                return total
                break
            elif total==21:
                print("We have a winner!")
                return total
                break
        j+=1
def clearboard():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
suit=["Diamonds","Hearts","Clubs","Spades"]
class card(object):
    def __init__(self,suit,number):
        self.number=number
        self.suit=suit
    def __str__(self):
        return str(self.number) + " of " + self.suit
    def __repr__(self):
        return str(self)
class deck(object):
    def __init__(self):
        suit=["Diamonds","Hearts","Clubs","Spades"]
        self.deck=[]
        self.hand = []
        i=0
        while True:
            p=i+1
            if i+1==1:
                p="Ace"
            elif i+1==11:
                p="Jack"
            elif i+1==12:
                p="Queen"
            elif i+1==13:
                p="King"
            self.deck.append(card(suit[0],p))
            self.deck.append(card(suit[1],p))
            self.deck.append(card(suit[2],p))
            self.deck.append(card(suit[3],p))
            i+= 1
            if i>=13:
                break
    def __str__ (self):
        string = ""
        for a in range(52):
            string = string + str(self.deck[a]) + "\n"
        return string
    def returnhand(self):
        self.hand=[]
        self.hand.append(random.choice(self.deck))
        self.hand.append(random.choice(self.deck))
        return self.hand
    def shuffle(self):
        x=0
        counter = 0
        while True:
            j= random.randint(0,51)
            k = random.randint(0,51)
            x=" "
            y = 0
            y = self.deck[j].number
            self.deck[j].number=self.deck[k].number
            self.deck[k].number = y
            x = self.deck[j].suit
            self.deck[j].suit=self.deck[k].suit
            self.deck[k].suit = x
            counter = counter + 1
            if counter > 1000:
                break
        return self.deck
    def deal(self):
        self.hand.append(random.choice(self.deck))
        return self.hand
def turn():
    counter=0
    a=deck()
    a.shuffle()
    print("Player One! Look At Your Hand!")
    time.sleep(2)
    print("Your Hand:",end="\n")
    print("_________________")
    time.sleep(2)
    x1=a.returnhand()[0]
    y1=a.returnhand()[1]
    print(x1)
    print("-------------")
    time.sleep(2)
    print(y1)
    time.sleep(2)
    clearboard()
    print("Player Two! Look At Your Hand!")
    time.sleep(2)
    print("Your Hand:",end="\n")
    print("_________________")
    time.sleep(2)
    x2=a.returnhand()[0]
    y2=a.returnhand()[1]
    print(x2)
    print("-------------")
    time.sleep(2)
    print(y2)
    time.sleep(2)
    z1 = card("",0)
    while True:
        hitornot1=input("Player 1: Hit or stay?")
        if hitornot1.lower()=="hit":
            print("Your Current Deck...")
            time.sleep(2)
            z1=a.deal()[2]
            print("_________________")
            time.sleep(2)
            print(x1)
            print("-------------")
            time.sleep(2)
            print(y1)
            print("-------------")
            time.sleep(2)
            print(z1)
            time.sleep(2)
            q1=int(checkforwin(x1.number,y1.number,1,z1.number))
            if q1>21:
                print("Game Over!, Dealer Wins!")
                return False
            elif q1==21:
                print("Player One Wins!")
                return False
            elif q1<21:
                print("Next Turn...")
                hitornot2=input("Dealer: Hit or stay?")
                if hitornot2.lower()=="hit":
                    print("Your Current Deck...")
                    time.sleep(2)
                    z2=a.deal()[2]
                    print("_________________")
                    time.sleep(2)
                    print(x2)
                    print("-------------")
                    time.sleep(2)
                    print(y2)
                    print("-------------")
                    time.sleep(2)
                    print(z2)
                    time.sleep(2)
                    time.sleep(2)
                    q=int(checkforwin(x2.number,y2.number,2 ,z2.number))
                    if q>21:
                        print("Game Over!, PLAYER ONE WINS!")
                        return False
                    elif q==21:
                        print("Player One Wins!")
                        return False
                    elif q<21:
                        print("Next Turn...")
                    clearboard()
        elif hitornot1.lower()=="stay":
            counter+=1
            hitornot2=input("Dealer: Hit or stay?")
            if hitornot2.lower()=="hit":
                print("Your Current Deck...")
                time.sleep(2)
                z2=a.deal()[2]
                print("_________________")
                time.sleep(2)
                print(x2)
                print("-------------")
                time.sleep(2)
                print(y2)
                print("-------------")
                time.sleep(2)
                print(z2)
                time.sleep(2)
                time.sleep(2)
                q2=checkforwin(x2.number,y2.number,2,z2.number)
                if q2>21:
                    print("Game Over!")
                    return False
                elif q2==21:
                        print("Dealer Wins!")
                        return False
                elif q2<21:
                    print("Next Turn...")
                clearboard()
            elif hitornot2.lower()=="stay":
                counter+=1
                if counter==2:
                    q1=checkforwin(x1.number, y1.number,1,z1.number)
                    q2=checkforwin(x2.number,y2.number,2)
                    if q2<q1:
                        print("Player One Wins!")
                        counter=0
                        return False
                    elif q2>q1:
                        print("Dealer Wins!")
                        counter=0
                        return False
                    elif q2==q1:
                        print("Dealer Wins!")
                        counter=0
                        return False
while True:
    turn()
    playagain=input("Want To Play Again? y/n")
    if playagain=="y":
        turn()
    elif playagain=="n":
        print("Thanks for playing!")
        False
    else:
        print("error! please input y/n")
        continue
        
    
