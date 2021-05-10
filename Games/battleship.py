'''
Created on Aug 9, 2017

@author: coditum
'''
'''
Created on Aug 8, 2017

@author: coditum
'''
import time
global p1ship1,p1ship2,p1ship3,p1ship4,p2ship1,p2ship2,p2ship3,p2ship4,letterg,spot,win,colum,lette
p1ship1=[]
p1ship2=[]
p1ship3=[]
p1ship4=[]
p2ship1=[]
p2ship2=[]
p2ship3=[]
p2ship4=[]
def setcolumn(lette):
    if lette=="A":
        colum=0
    elif lette=="B":
        colum=1
    elif lette=="C":
        colum=2
    elif lette=="D":
        colum=3
    elif lette=="E":
        colum=4
    elif lette=="F":
        colum=5
    elif lette=="G":
        colum=6
    elif lette=="H":
        colum=7
    elif lette=="I":
        colum=8
    elif lette=="J":
        colum=9
    if lette=="K":
        colum=10
    elif lette=="L":
        colum=11
    elif lette=="M":
        colum=12
    elif lette=="N":
        colum=13
    elif lette=="O":
        colum=14
    elif lette=="P":
        colum=15
    elif lette=="Q":
        colum=16
    elif lette=="R":
        colum=17
    elif lette=="S":
        colum=18
    elif lette=="T":
        colum=19
    elif lette=="U":
        colum=20
    elif lette=="V":
        colum=21
    elif lette=="W":
        colum=22
    elif lette=="X":
        colum=23
    elif lette=="Y":
        colum=24
    elif lette=="Z":
        colum=25
    return colum

    
board=[[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
board2=[[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]]
boardCoor=[["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1"],["A2","B2","C2","D2","E2","F2","G2","H2","I2","J2"],["A3","B3","C3","D3","E3","F3","G3","H3","I3","J3"],["A4","B4","C4","D4","E4","F4","G4","H4","I4","J4"],["A5","B5","C5","D5","E5","F5","G5","H5","I5","J5"],["A6","B6","C6","D6","E6","F6","G6","H6","I6","J6"],["A7","B7","C7","D7","E7","F7","G7","H7","I7","J7"],["A8","B8","C8","D8","E8","F8","G8","H8","I8","J8"],["A9","B9","C9","D9","E9","F9","G9","H9","I9","J9"],["A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]]
win = 0
def printboard(board):
    print("       A     B     C     D     E     F     G     H     I     J")
    print("1   |  "+board[0][0]+"  |  "+board[0][1]+"  |  "+board[0][2]+"  |  "+board[0][3]+"  |  "+board[0][4]+"  |  "+board[0][5]+"  |  "+board[0][6]+"  |  "+board[0][7]+"  |  "+board[0][8]+"  |  "+board[0][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("2   |  "+board[1][0]+"  |  "+board[1][1]+"  |  "+board[1][2]+"  |  "+board[1][3]+"  |  "+board[1][4]+"  |  "+board[1][5]+"  |  "+board[1][6]+"  |  "+board[1][7]+"  |  "+board[1][8]+"  |  "+board[1][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("3   |  "+board[2][0]+"  |  "+board[2][1]+"  |  "+board[2][2]+"  |  "+board[2][3]+"  |  "+board[2][4]+"  |  "+board[2][5]+"  |  "+board[2][6]+"  |  "+board[2][7]+"  |  "+board[2][8]+"  |  "+board[2][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("4   |  "+board[3][0]+"  |  "+board[3][1]+"  |  "+board[3][2]+"  |  "+board[3][3]+"  |  "+board[3][4]+"  |  "+board[3][5]+"  |  "+board[3][6]+"  |  "+board[3][7]+"  |  "+board[3][8]+"  |  "+board[3][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("5   |  "+board[4][0]+"  |  "+board[4][1]+"  |  "+board[4][2]+"  |  "+board[4][3]+"  |  "+board[4][4]+"  |  "+board[4][5]+"  |  "+board[4][6]+"  |  "+board[4][7]+"  |  "+board[4][8]+"  |  "+board[4][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("6   |  "+board[5][0]+"  |  "+board[5][1]+"  |  "+board[5][2]+"  |  "+board[5][3]+"  |  "+board[5][4]+"  |  "+board[5][5]+"  |  "+board[5][6]+"  |  "+board[5][7]+"  |  "+board[5][8]+"  |  "+board[5][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("7   |  "+board[6][0]+"  |  "+board[6][1]+"  |  "+board[6][2]+"  |  "+board[6][3]+"  |  "+board[6][4]+"  |  "+board[6][5]+"  |  "+board[6][6]+"  |  "+board[6][7]+"  |  "+board[6][8]+"  |  "+board[6][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("8   |  "+board[7][0]+"  |  "+board[7][1]+"  |  "+board[7][2]+"  |  "+board[7][3]+"  |  "+board[7][4]+"  |  "+board[7][5]+"  |  "+board[7][6]+"  |  "+board[7][7]+"  |  "+board[7][8]+"  |  "+board[7][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("9   |  "+board[8][0]+"  |  "+board[8][1]+"  |  "+board[8][2]+"  |  "+board[8][3]+"  |  "+board[8][4]+"  |  "+board[8][5]+"  |  "+board[8][6]+"  |  "+board[8][7]+"  |  "+board[8][8]+"  |  "+board[8][9]+"  |  ")
    print("-----------------------------------------------------------------")
    print("10  |  "+board[9][0]+"  |  "+board[9][1]+"  |  "+board[9][2]+"  |  "+board[9][3]+"  |  "+board[9][4]+"  |  "+board[9][5]+"  |  "+board[9][6]+"  |  "+board[9][7]+"  |  "+board[9][8]+"  |  "+board[9][9]+"  |  ")
    print("-----------------------------------------------------------------")
printboard(board)

def checkforship(what,space,direction,board,ship1,ship2,ship3,ship4):
    global column
    global letter
    global times
    global number
    
    times=1
    letter=space[0]
    letter=letter.upper()
    if len(space)==2: #If they typed in 2 characters
        while True:
            try: #Is second character a number?
                number=int(space[1]) 
            except ValueError:
                print("Please Input a Number for your row")
                space=input("Where do you want to place your ship? ")
            else:
                number-=1
                break
    elif len(space)==3: #If they typed in 3 characters
        while True:
            try: #Are characters after first numbers?
                number=int(space[1:])
            except ValueError:
                print("Please Input a Number for your row")
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
            else:
                number-=1
                break
    column = setcolumn(letter)
    if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
        while column>9 or column<0: #While Number not 0-10
            print("Please Input A Letter Between A and J")
            space=input("Where do you want to place your ship? ")
            direction=input("Please Put In A Direction That The Ship Should Point In: ")
            letter=space[0]
            letter=letter.upper()
            column = setcolumn(letter)
            if len(space)==2:
                while True:
                    try: # Is second character a number?
                        number=int(space[1])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3:
                while True:
                    try: #Is second character a number?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            
        while number<0 or number>9:
            print("Please Input A Row Between 1 and 10")
            space=input("Where do you want to place your ship? ")
            direction=input("Please Put In A Direction That The Ship Should Point In: ")
            letter=space[0]
            letter=letter.upper()
            if len(space)==2:
                number=int(space[1])
                number-=1
            elif len(space)==3:
                number=int(space[1:2])
                number-=1
            column = setcolumn(letter)
    if what==2:
            what=str(what)
            ship1.append(space.upper())
            if direction.upper()=="RIGHT":
                board[number][column]="."
                board[number][column+1]="."
                ship1.append(boardCoor[number][column+1])
                printboard(board)
                times+=1
                
            elif direction.upper()=="LEFT":
                board[number][column]="."
                board[number][column-1]="."
                ship1.append(boardCoor[number][column-1])
                printboard(board)
                times+=1
                
            elif direction.upper()=="UP" :
                board[number][column]="."
                board[number-1][column]="."
                ship1.append(boardCoor[number-1][column])
                printboard(board)
                times+=1
                
            elif direction.upper()=="DOWN":
                board[number][column]="."
                board[number+1][column]="."
                ship1.append(boardCoor[number+1][column])
                printboard(board)
                times+=1
                
    if what==3 :
        ship2.append(space.upper())
        if direction.upper()=="RIGHT":
            board[number][column]="."
            board[number][column+1]="."
            board[number][column+2]="."
            ship2.append(boardCoor[number][column+1])
            ship2.append(boardCoor[number][column+2])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship2.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
                        
        elif direction.upper()=="LEFT":
            board[number][column]="."
            board[number][column-1]="."
            board[number][column-2]="."
            ship2.append(boardCoor[number][column-1])
            ship2.append(boardCoor[number][column-2])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship2.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
            printboard(board)
            times+=1
                    
        elif direction.upper()=="UP" :
            board[number][column]="."
            board[number-1][column]="."
            board[number-2][column]="."
            ship2.append(boardCoor[number-1][column])
            ship2.append(boardCoor[number-2][column])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship2.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
            printboard(board)
            times+=1
            
        elif direction.upper()=="DOWN":
            board[number][column]="."
            board[number+1][column]="."
            board[number+2][column]="."
            ship2.append(boardCoor[number+1][column])
            ship2.append(boardCoor[number+2][column])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship2.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
            printboard(board)
            times+=1
        if what==4 :
            ship3.append(space.upper())
            what=str(what)
            if direction.upper()=="RIGHT":
                board[number][column]="."
                board[number][column+1]="."
                board[number][column+2]="."
                board[number][column+3]="."
                ship3.append(boardCoor[number][column+1])
                ship3.append(boardCoor[number][column+2])
                ship3.append(boardCoor[number][column+3])
                printboard(board)
                overlap = False
                for a in ship1:
                    for b in ship2:
                        if a == b:
                            overlap = True
                for a in ship2:
                    for b in ship3:
                        if a == b:
                            overlap = True
                while overlap:
                    print("Your ship overlapped, try again")
                    ship3.clear()
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                if len(space)==2: #If they typed in 2 characters
                    while True:
                        try: #Is second character a number?
                            number=int(space[1]) 
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                        else:
                            number-=1
                            break
                elif len(space)==3: #If they typed in 3 characters
                    while True:
                        try: #Are characters after first numbers?
                            number=int(space[1:])
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        else:
                            number-=1
                            break
                column = setcolumn(letter)
                if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                    while column>9 or column<0: #While Number not 0-10
                        print("Please Input A Letter Between A and J")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        column = setcolumn(letter)
                        if len(space)==2:
                            while True:
                                try: # Is second character a number?
                                    number=int(space[1])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                else:
                                    number-=1
                                    break
                        elif len(space)==3:
                            while True:
                                try: #Is second character a number?
                                    number=int(space[1:])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                                else:
                                    number-=1
                                    break
                        
                        while number<0 or number>9:
                            print("Please Input A Row Between 1 and 10")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            letter=space[0]
                            letter=letter.upper()
                            if len(space)==2:
                                number=int(space[1])
                                number-=1
                            elif len(space)==3:
                                number=int(space[1:2])
                                number-=1
                            column = setcolumn(letter)
                            for a in ship1:
                                for b in ship2:
                                    if a == b:
                                        overlap = True
                            printboard(board)
                            times+=1
                printboard(board)
                times+=1
                
            elif direction.upper()=="LEFT":
                board[number][column]="."
                board[number][column-1]="."
                board[number][column-2]="."
                board[number][column-3]="."
                ship3.append(boardCoor[number][column-1])
                ship3.append(boardCoor[number][column-2])
                ship3.append(boardCoor[number][column-3])
                overlap = False
                for a in ship1:
                    for b in ship2:
                        if a == b:
                            overlap = True
                for a in ship2:
                    for b in ship3:
                        if a == b:
                            overlap = True
                while overlap:
                    print("Your ship overlapped, try again")
                    ship3.clear()
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                if len(space)==2: #If they typed in 2 characters
                    while True:
                        try: #Is second character a number?
                            number=int(space[1]) 
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                        else:
                            number-=1
                            break
                elif len(space)==3: #If they typed in 3 characters
                    while True:
                        try: #Are characters after first numbers?
                            number=int(space[1:])
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        else:
                            number-=1
                            break
                column = setcolumn(letter)
                if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                    while column>9 or column<0: #While Number not 0-10
                        print("Please Input A Letter Between A and J")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        column = setcolumn(letter)
                        if len(space)==2:
                            while True:
                                try: # Is second character a number?
                                    number=int(space[1])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                else:
                                    number-=1
                                    break
                        elif len(space)==3:
                            while True:
                                try: #Is second character a number?
                                    number=int(space[1:])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                                else:
                                    number-=1
                                    break
                        
                        while number<0 or number>9:
                            print("Please Input A Row Between 1 and 10")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            letter=space[0]
                            letter=letter.upper()
                            if len(space)==2:
                                number=int(space[1])
                                number-=1
                            elif len(space)==3:
                                number=int(space[1:2])
                                number-=1
                            column = setcolumn(letter)
                            for a in ship1:
                                for b in ship2:
                                    if a == b:
                                        overlap = True
                            printboard(board)
                            times+=1
                printboard(board)
                times+=1
                
            elif direction.upper()=="UP" :
                board[number][column]="."
                board[number-1][column]="."
                board[number-2][column]="."
                board[number-3][column]="."
                ship3.append(boardCoor[number-1][column])
                ship3.append(boardCoor[number-2][column])
                ship3.append(boardCoor[number-3][column])
                overlap = False
                for a in ship1:
                    for b in ship2:
                        if a == b:
                            overlap = True
                for a in ship2:
                    for b in ship3:
                        if a == b:
                            overlap = True
                while overlap:
                    print("Your ship overlapped, try again")
                    ship3.clear()
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                if len(space)==2: #If they typed in 2 characters
                    while True:
                        try: #Is second character a number?
                            number=int(space[1]) 
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                        else:
                            number-=1
                            break
                elif len(space)==3: #If they typed in 3 characters
                    while True:
                        try: #Are characters after first numbers?
                            number=int(space[1:])
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        else:
                            number-=1
                            break
                column = setcolumn(letter)
                if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                    while column>9 or column<0: #While Number not 0-10
                        print("Please Input A Letter Between A and J")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        column = setcolumn(letter)
                        if len(space)==2:
                            while True:
                                try: # Is second character a number?
                                    number=int(space[1])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                else:
                                    number-=1
                                    break
                        elif len(space)==3:
                            while True:
                                try: #Is second character a number?
                                    number=int(space[1:])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                                else:
                                    number-=1
                                    break
                        
                        while number<0 or number>9:
                            print("Please Input A Row Between 1 and 10")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            letter=space[0]
                            letter=letter.upper()
                            if len(space)==2:
                                number=int(space[1])
                                number-=1
                            elif len(space)==3:
                                number=int(space[1:2])
                                number-=1
                            column = setcolumn(letter)
                            for a in ship1:
                                for b in ship2:
                                    if a == b:
                                        overlap = True
                            printboard(board)
                            times+=1
                printboard(board)
                times+=1
                
            elif direction.upper()=="DOWN":
                board[number][column]="."
                board[number+1][column]="."
                board[number+2][column]="."
                board[number+3][column]="."
                ship3.append(boardCoor[number+1][column])
                ship3.append(boardCoor[number+2][column])
                ship3.append(boardCoor[number+3][column])
                overlap = False
                for a in ship1:
                    for b in ship2:
                        if a == b:
                            overlap = True
                for a in ship2:
                    for b in ship3:
                        if a == b:
                            overlap = True
                while overlap:
                    print("Your ship overlapped, try again")
                    ship3.clear()
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                if len(space)==2: #If they typed in 2 characters
                    while True:
                        try: #Is second character a number?
                            number=int(space[1]) 
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                        else:
                            number-=1
                            break
                elif len(space)==3: #If they typed in 3 characters
                    while True:
                        try: #Are characters after first numbers?
                            number=int(space[1:])
                        except ValueError:
                            print("Please Input a Number for your row")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        else:
                            number-=1
                            break
                column = setcolumn(letter)
                if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                    while column>9 or column<0: #While Number not 0-10
                        print("Please Input A Letter Between A and J")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        column = setcolumn(letter)
                        if len(space)==2:
                            while True:
                                try: # Is second character a number?
                                    number=int(space[1])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                else:
                                    number-=1
                                    break
                        elif len(space)==3:
                            while True:
                                try: #Is second character a number?
                                    number=int(space[1:])
                                except ValueError:
                                    print("Please Input a Number for your row")
                                    space=input("Where do you want to place your ship? ")
                                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                                else:
                                    number-=1
                                    break
                        
                        while number<0 or number>9:
                            print("Please Input A Row Between 1 and 10")
                            space=input("Where do you want to place your ship? ")
                            direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            letter=space[0]
                            letter=letter.upper()
                            if len(space)==2:
                                number=int(space[1])
                                number-=1
                            elif len(space)==3:
                                number=int(space[1:2])
                                number-=1
                            column = setcolumn(letter)
                            for a in ship1:
                                for b in ship2:
                                    if a == b:
                                        overlap = True
                            printboard(board)
                            times+=1
                printboard(board)
                times+=1        
    
    if what==5 :
        ship4.append(space.upper())
        what=str(what)
        if direction.upper()=="RIGHT":
            board[number][column]="."
            board[number][column+1]="."
            board[number][column+2]="."
            board[number][column+3]="."
            board[number][column+4]="."
            ship4.append(boardCoor[number][column+1])
            ship4.append(boardCoor[number][column+2])
            ship4.append(boardCoor[number][column+3])
            ship4.append(boardCoor[number][column+4])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            for a in ship2:
                for b in ship3:
                    if a == b:
                        overlap = True
            for a in ship3:
                for b in ship4:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship4.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
            printboard(board)
            times+=1
            
        elif direction.upper()=="LEFT":
            board[number][column]="."
            board[number][column-1]="."
            board[number][column-2]="."
            board[number][column-3]="."
            board[number][column-4]="."
            ship4.append(boardCoor[number][column-1])
            ship4.append(boardCoor[number][column-2])
            ship4.append(boardCoor[number][column-3])
            ship4.append(boardCoor[number][column-4])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            for a in ship2:
                for b in ship3:
                    if a == b:
                        overlap = True
            for a in ship3:
                for b in ship4:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship4.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
            printboard(board)
            times+=1
            
        elif direction.upper()=="UP" :
            board[number][column]="."
            board[number-1][column]="."
            board[number-2][column]="."
            board[number-3][column]="."
            board[number-4][column]="."
            ship4.append(boardCoor[number-1][column])
            ship4.append(boardCoor[number-2][column])
            ship4.append(boardCoor[number-3][column])
            ship4.append(boardCoor[number-4][column])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            for a in ship2:
                for b in ship3:
                    if a == b:
                        overlap = True
            for a in ship3:
                for b in ship4:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship4.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
            printboard(board)
            times+=1
            
        elif direction.upper()=="DOWN":
            board[number][column]="."
            board[number+1][column]="."
            board[number+2][column]="."
            board[number+3][column]="."
            board[number+4][column]="."
            ship4.append(boardCoor[number+1][column])
            ship4.append(boardCoor[number+2][column])
            ship4.append(boardCoor[number+3][column])
            ship4.append(boardCoor[number+4][column])
            overlap = False
            for a in ship1:
                for b in ship2:
                    if a == b:
                        overlap = True
            for a in ship2:
                for b in ship3:
                    if a == b:
                        overlap = True
            for a in ship3:
                for b in ship4:
                    if a == b:
                        overlap = True
            while overlap:
                print("Your ship overlapped, try again")
                ship4.clear()
                space=input("Where do you want to place your ship? ")
                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                letter=space[0]
                letter=letter.upper()
            if len(space)==2: #If they typed in 2 characters
                while True:
                    try: #Is second character a number?
                        number=int(space[1]) 
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                    else:
                        number-=1
                        break
            elif len(space)==3: #If they typed in 3 characters
                while True:
                    try: #Are characters after first numbers?
                        number=int(space[1:])
                    except ValueError:
                        print("Please Input a Number for your row")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    else:
                        number-=1
                        break
            column = setcolumn(letter)
            if column>9 or column<0 or number<0 or number>10: #If Letter not A-J or Number not 0-10
                while column>9 or column<0: #While Number not 0-10
                    print("Please Input A Letter Between A and J")
                    space=input("Where do you want to place your ship? ")
                    direction=input("Please Put In A Direction That The Ship Should Point In: ")
                    letter=space[0]
                    letter=letter.upper()
                    column = setcolumn(letter)
                    if len(space)==2:
                        while True:
                            try: # Is second character a number?
                                number=int(space[1])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                            else:
                                number-=1
                                break
                    elif len(space)==3:
                        while True:
                            try: #Is second character a number?
                                number=int(space[1:])
                            except ValueError:
                                print("Please Input a Number for your row")
                                space=input("Where do you want to place your ship? ")
                                direction=input("Please Put In A Direction That The Ship Should Point In: ")
                            else:
                                number-=1
                                break
                    
                    while number<0 or number>9:
                        print("Please Input A Row Between 1 and 10")
                        space=input("Where do you want to place your ship? ")
                        direction=input("Please Put In A Direction That The Ship Should Point In: ")
                        letter=space[0]
                        letter=letter.upper()
                        if len(space)==2:
                            number=int(space[1])
                            number-=1
                        elif len(space)==3:
                            number=int(space[1:2])
                            number-=1
                        column = setcolumn(letter)
                        for a in ship1:
                            for b in ship2:
                                if a == b:
                                    overlap = True
                        printboard(board)
                        times+=1
            printboard(board)
            times+=1
                
        
                    
        

def hitmiss(board,ship1,ship2,ship3,ship4,boardtoprint,win):
    guess=input("Guess a spot: ")
    guess=guess.upper()
    spot=0
    letterg=guess[0]
    letterg=guess[0].upper()
    numberg=int(guess[1])
    numberg-=1
    if letterg=='A':
        spot=0
    elif letterg=='B':
        spot=1
    elif letterg=='C':
        spot=2
    elif letterg=='D':
        spot=3
    elif letterg=='E':
        spot=4
    elif letterg=='F':
        spot=5
    elif letterg=='G':
        spot=6
    elif letterg=='H':
        spot=7
    elif letterg=='I':
        spot=8
    elif letterg=='J':
        spot=9
    guess=boardCoor[numberg][spot]
    guess=guess.upper()
    print(ship1)
    print(ship2)
    print(ship3)
    print(ship4)
    if  guess in ship1 or guess in ship2 or guess in ship3 or guess in ship4:
        print("Hit!")
        win+=1
        boardtoprint[numberg][spot]="X"
        printboard(boardtoprint)
        if win==14:
            print("You Sunk All Of The Ships!")
            return False
    else:
        print("Miss!")
        boardtoprint[numberg][spot]="O"
        printboard(boardtoprint)
def placeship():
    what=2
    print("Player One's Turn!")
    global w
    w=0
    while True:
        placeship=input("Where would you like to place your ship? ")
        direction=input("Please Put In A Direction That The Ship Should Point In: ")
        checkforship(what,placeship,direction,board,p1ship1,p1ship2,p1ship3,p1ship4)
        time.sleep(2)
        while True:
            print("")
            if w>22:
                break
            w+=1
        printboard(board)
        what+=1
        if what>5:
            print(p1ship3)
            break
    printboard(board2)
    print("Player Two's Turn!")
    what=2
    w=0
    while True:
        placeship=input("Where would you like to place your ship? ")
        direction=input("Please Put In A Direction That The Ship Should Point In: ")
        checkforship(what,placeship,direction,board2,p2ship1,p2ship2,p2ship3,p2ship4)
        time.sleep(2)
        w=0
        while True:
            print("")
            if w>22:
                break
            w+=1
        printboard(board2)
        what+=1
        if what>5:
            
            break
def turn():
    w=0
    while True:
        while True:
            print("")
            if w>22:
                break
            w+=1
        printboard(board)
        print ("Player One's Turn!")
        hitmiss(board2,p2ship1,p2ship2,p2ship3,p2ship4,board,0)
        time.sleep(2)
        while True:
            print("")
            if w>22:
                break
            w+=1
        printboard(board2)
        print ("Player Two's Turn!")
        hitmiss(board,p1ship1,p1ship2,p1ship3,p1ship4,board2,0)
        time.sleep(2)
        w=0
        
placeship()
turn()

global player
player=1

