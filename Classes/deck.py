import random
import time
betplayer1=0
betplayer2=0
betplayer3=0
betplayer4=0
deck=[]
suit=["Diamonds","Clubs","Hearts","Spades"]
face=["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
for x in range(0,len(face)):
    for y in range(0, len(suit)):
        card=face[x]+" of "+suit[y]
        deck.append(card)
for z in range(0,len(deck)):
    randomvar=random.randint(0,len(deck)-1)
    toappend=deck[randomvar]
    deck.pop(randomvar)
    deck.append(toappend)
#print(len(deck))
#print(deck)
def bet(player):
    bet=input("How Many Tricks Do You Think You Will Get?")
    if player==1:
        betplayer1=bet
        print("Your Bet is "+betplayer1)
    elif player==2:
        betplayer2=bet
        print("Your Bet is "+betplayer2)
    elif player==3:
        betplayer3=bet
        print("Your Bet is "+betplayer3)
    elif player==4:
        betplayer4=bet
        print("Your Bet is "+betplayer4)
def clearboard():
    for num in range(15):
        print(" ")
def turn():
    playernumber=1
    randomnum=random.randint(1,5)
    trumpsuit=suit[randomnum-1]
    amtofcards=7
    player1=[]
    player2=[]
    player3=[]
    player4=[]
    player=[player1,player2,player3,player4]
    card=" "
    while amtofcards>0:
        card=deck[0]
        player1.append(card)
        deck.pop(0)  
        card=deck[0]
        player2.append(card)
        deck.pop(0)
        card=deck[0]
        player3.append(card)
        deck.pop(0)
        card=deck[0]
        player4.append(card)
        deck.pop(0)
        if len(player4)==7:
            card=deck[0]
            player4.append(card)
            deck.pop(0)
        amtofcards-=1
    print("The trumping Suit Is " + trumpsuit)
    print(player1)
    time.sleep(5)
    bet(1)
    clearboard()
    print(player2)
    time.sleep(5)
    bet(2)
    clearboard()
    print(player3)
    time.sleep(5)
    bet(3)
    clearboard()
    print(player4)
    bet(4)
turn()