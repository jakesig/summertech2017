'''
Created on Aug 7, 2017

@author: summertech
'''
board=[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],]


def printboard():
    print ("   1     2     3     4     5     6     7")
    print ("|  "+board[0][0]+"  |  "+board[0][1]+"  |  "+board[0][2]+"  |  "+board[0][3]+"  |  "+board[0][4]+"  |  "+board[0][5]+"  |  "+board[0][6]+"  |")
    print ("|-----|-----|-----|-----|-----|-----|-----|")
    print ("|  "+board[1][0]+"  |  "+board[1][1]+"  |  "+board[1][2]+"  |  "+board[1][3]+"  |  "+board[1][4]+"  |  "+board[1][5]+"  |  "+board[1][6]+"  |")
    print ("|-----|-----|-----|-----|-----|-----|-----|")
    print ("|  "+board[2][0]+"  |  "+board[2][1]+"  |  "+board[2][2]+"  |  "+board[2][3]+"  |  "+board[2][4]+"  |  "+board[2][5]+"  |  "+board[2][6]+"  |")
    print ("|-----|-----|-----|-----|-----|-----|-----|")
    print ("|  "+board[3][0]+"  |  "+board[3][1]+"  |  "+board[3][2]+"  |  "+board[3][3]+"  |  "+board[3][4]+"  |  "+board[3][5]+"  |  "+board[3][6]+"  |")
    print ("|-----|-----|-----|-----|-----|-----|-----|")
    print ("|  "+board[4][0]+"  |  "+board[4][1]+"  |  "+board[4][2]+"  |  "+board[4][3]+"  |  "+board[4][4]+"  |  "+board[4][5]+"  |  "+board[4][6]+"  |")
    print ("|-----|-----|-----|-----|-----|-----|-----|")
    print ("|  "+board[5][0]+"  |  "+board[5][1]+"  |  "+board[5][2]+"  |  "+board[5][3]+"  |  "+board[5][4]+"  |  "+board[5][5]+"  |  "+board[5][6]+"  |")
    print ("|-----|-----|-----|-----|-----|-----|-----|")
def replace(char,num):
    char=str(char)
    num=int(num)
    num-=1
    global y 
    global x
    y = num
    if board[5][num]==" ":
        x = 5
        board[5][num]=char
        printboard()
        return True
    elif board[4][num]==" ": 
        x= 4
        board[4][num]=char
        printboard()
        return True
    elif board[3][num]==" ":
        x = 3
        board[3][num]=char
        printboard()
        return True
    elif board[2][num]==" ":
        x= 2
        board[2][num]=char
        printboard()
        return True
    elif board[1][num]==" ":
        x = 1
        board[1][num]=char
        printboard()
        return True
    elif board[0][num]==" ":
        x = 0
        board[0][num]=char
        printboard()
        return True
    elif board[0][num]!=" ":
        print ("Column Is Full!")
        return False
def winloss(char):
    player=""
    if char == "X":
        player = "One"
    elif char=="O":
        player="Two"
    if board[x][y]==board[x-1][y]==board[x-2][y]==board[x-3][y]==char:
        print ("Player {} Wins!".format(player))
        return False
    elif board[x][y]==board[x][y-1]==board[x][y-2]==board[x][y-3]==char:
        print ("Player {} Wins!".format(player))
        return False
    elif board[x][y]==board[x+1][y]==board[x+2][y]==board[x+3][y]==char:
        print ("Player {} Wins!".format(player))
        return False
    elif board[x][y]==board[x][y+1]==board[x][y+1]==board[x][y+3]==char:
        print ("Player {} Wins!".format(player))
        return False
    elif board[x][y]==board[x-1][y-1]==board[x-2][y-2]==board[x-3][y-3]==char:
        print ("Player {} Wins!".format(player))
        return False
    elif board[x][y]==board[x-1][y+1]==board[x-2][y+2]==board[x-3][y+3]==char:
        print ("Player {} Wins!".format(player))
        return False
    elif board[x][y]==board[x+1][y-1]==board[x+2][y-2]==board[x+3][y-3]==char:
        print ("Player {} Wins!".format(player))
        return False
    return True
def turn(): 
    num=1
    printboard()
    while True:
        if num%2==1:
            while True:
                print ("Player One's Turn")
                try:
                    where=int(input("Choose a Column: "))
                    while where>7 or where<1:
                        print("Please Enter a Number between 1 and 7")
                        where=int(input("Choose a Column: "))
                except ValueError:
                    print("Please Enter a Number between 1 and 7")
                    continue
                num+=1
                if replace("X",where): 
                    break
        if not(winloss("X")):
                break
                
        if num%2==0:
            while True:
                print ("Player Two's Turn")
                try:
                    where=int(input("Choose a Column: "))
                    while where>7 or where<1:
                        print("Please Enter a Number between 1 and 7")
                        where=int(input("Choose a Column: "))
                except ValueError:
                    print("Please Enter a Number between 1 and 7")
                    continue
                num+=1
                if replace("O",where): 
                    break
        if not(winloss("O")):
            break
play=str(input("Hello, would you like to play JAKE's SPECTACULAR CONNECT 4 GAME? (y/n)"))
if play == "y":
    turn()
elif play == "n":
    print ("GOODBYE! :(")
else:
    print ("Please Print y or n")
