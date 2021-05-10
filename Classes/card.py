'''
Created on Feb 25, 2018

@author: coditum
'''
import random
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
    playernumber=1
    player1=[]
    player2=[]
    player3=[]
    player4=[]
    player=[player1,player2,player3,player4]
    g=0
    card=" "
    f=deck()
    while playernumber<=4:
        print ("Player ",playernumber, "'s Hand")
        while True:
            card=f.returnhand()[0]
            player[playernumber].append(card)
            card
            print(player[playernumber][g])
            if playernumber==4 and len(player4)==7:
                player[playernumber].append(card[g])
                print(player[playernumber[g]])
                break
        print("--------------")
        playernumber+=1
turn()
            
            
        
        
    
    
