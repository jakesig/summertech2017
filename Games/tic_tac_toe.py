'''
Created on Aug 7, 2017

@author: summertech
'''
'''
Step 1. Make a board
Step 2. Modify the board
Step 3. Check for win conditions
'''
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
def printboard():
    print("    |      |")
    print(" "+board[0][0]+"  |  "+board[0][1]+"   | "+board[0][2])
    print("    |      |")
    print("-----------------")
    print("    |      |")
    print(" "+board[1][0]+"  |  "+board[1][1]+"   | "+board[1][2])
    print("    |      |")
    print("-----------------")
    print("    |      |")
    print(" "+board[2][0]+"  |  "+board[2][1]+"   | "+board[2][2])
    print("    |      |")



def replace(arg,char):
    if arg.lower()=="topleft":
        if board[0][0]=="x" or board[0][0] =="o":
            return False
        board[0][0]=str(char)
    elif arg.lower()=="topmiddle":
        if board[0][1]=="x" or board[0][1]== "o":
            return False
        board[0][1]=str(char) 
    elif arg.lower()=="topright":
        if board[0][2]=="x" or board[0][2] == "o":
            return False
        board[0][2]=str(char)
    elif arg.lower()=="middleleft":
        if board[1][0]=="x" or board[1][0]== "o":
            return False
        board[1][0]=str(char)  
    elif arg.lower()=="middle":
        if board[1][1]=="x" or board[1][1]== "o":
            return False
        board[1][1]=str(char)
    elif arg.lower()=="middleright":
        if board[1][2]=="x" or board[1][2]== "o":
            return False
        board[1][2]=str(char)  
    elif arg.lower()=="bottomleft":
        if board[2][0]=="x" or board[2][0]== "o":
            return False
        board[2][0]=str(char)
    elif arg.lower()=="bottommiddle":
        if board[2][1]=="x" or board[2][1]== "o":
            return False
        board[2][1]=str(char)   
    elif arg.lower()=="bottomright":
        if board[2][2]=="x" or board[2][2]== "o":
            return False
        board[2][2]=str(char)
def winloss(xo):
    if xo=="x":
        p="One"
    elif xo=="o":
        p="Two"
    if board[0][0]==board[0][1]==board[0][2]==xo:
        print("Player {} Wins!".format(p))
        return False
    elif board[1][0]==board[1][1]==board[1][2]==xo:
        print("Player {} Wins!".format(p))
        return False
    elif board[2][0]==board[2][1]==board[2][2]==xo:
        print("Player {} Wins!".format(p))
        return False
    elif board[0][0]==board[1][0]==board[2][0]==xo:
        print("Player {} Wins!".format(p))
        return False
    elif board[0][1]==board[1][1]==board[2][1]==xo:
        print("Player {} Wins!".format(p))
        return False
    elif board[0][2]==board[1][2]==board[2][2]==xo:
        print("Player {} Wins!".format(p))
        return False
    elif board[0][0]==board[1][1]==board[2][2]==xo:
        print("Player {} Wins!".format(p))
        return False
    elif board[0][2]==board[1][1]==board[2][0]==xo:
        print("Player {} Wins!".format(p))
        return False
    return True
def gameplay():   
    printboard() 
    num=1
    while True:
        what=""
        if num%2==1:
            print("Player One's Turn")
            what="x"
            num=num+1
            where=str(input("Where do you want to place?"))
            while replace(where,what)==False:
                print ("There is already Something There!")
                where=str(input("Where do you want to place?"))
            if winloss("x")==False:
                
                break
        elif num%2==0:
            print("Player Two's Turn")
            what="o"
            num=num+1
            where=str(input("Where do you want to place?"))
            while replace(where,what)==False:
                print ("There is already Something There!")
                where=str(input("Where do you want to place?"))
            if winloss("o")==False:
                printboard()
                break
        printboard()
        if num==10:
            print("GAME OVER, ITS A TIE!")
            break
play=str(input("Hello, would you like to play JAKE's SPECTACULAR TIC TAC TOE GAME? (y/n)"))
if play == "y":
    gameplay()
elif play == "n":
    print ("GOODBYE! :(")
else:
    print ("Please Print y or n")
    


