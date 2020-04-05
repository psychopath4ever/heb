#Version 0.1
def PossibleMove(boa,wei,act,pla,num):
    directions = [0,0,0,0] #[Up,Right,Down,Left]
    stoned = 1
    antistoned = 3
    if pla == 1:
        stoned = 3
        antistoned = 1
    x = num[0]
    y = num[1]
    print(x,y,boa[x][y])
    ##go up?
    if wei[x] > 0:
        if pla == 0:
            if y==len(boa[x])-1:
                #last spot
                directions[0]=1
            else:
                if boa[x][y+1]==0:
                    directions[0]=1
                elif boa[x][y+1]==stoned:
                    for i in range(y+1,len(boa[x])-1):
                        #there could be a row of WHITE stones with different appearances
                        if i+1==8:
                            #filled with own stones till end of lever
                            directions[0]=1
                            break
                        elif boa[x][i] == antistoned:
                            #row is blocked by one stone of the BLACK team
                            break
                        else:
                            #there is an empty space
                            directions[0]=1
                elif boa[x][y+1]==antistoned and act == 2:
                    if y+1==len(boa[x]-1):
                        directions[0]=1
                    elif boa[x][y+2]==0:
                        directions[0]=1
        elif pla == 1:
            if y<len(boa[x])-1:
                #first spot
                if boa[x][y+1]==0:
                    directions[0]=1
                elif boa[x][y+1]==stoned:
                    for i in range(y+1,len(boa[x])-1):
                        #there could be a row of BLACK stones with different appearances
                        if i+1==8:
                            #filled with own stones till end of lever
                            break
                        elif boa[x][i] == antistoned:
                            #row is blocked by one stone of the WHITE team
                            break
                        else:
                            #there is an empty space
                            directions[0]=1
                elif boa[x][y+1]==antistoned and act == 2:
                    if y+1<len(boa[x]):
                        if boa[x][y+2]==0:
                            directions[0]=1
                            
    ##go down?
    if wei[x] < 0:
        if pla == 0:
            if y>0:
                if boa[x][y-1]==0:
                    directions[0]=1
                elif boa[x][y-1]==stoned:
                    for i in range(y-1,0):
                        #there could be a row of WHITE stones with different appearances
                        if i-1<0:
                            #filled with own stones till end of lever
                            break
                        elif boa[x][i-1] == antistoned:##########
                            #row is blocked by one stone of the BLACK team
                            break
                        else:
                            #there is an empty space
                            directions[0]=1
                elif boa[x][y+1]==antistoned and act == 2:
                    if y+1==len(boa[x]-1):
                        directions[0]=1
                    elif boa[x][y+2]==0:
                        directions[0]=1
        elif pla == 1:
            if y<len(boa[x])-1:
                #first spot
                if boa[x][y+1]==0:
                    directions[0]=1
                elif boa[x][y+1]==stoned:
                    for i in range(y+1,len(boa[x])-1):
                        #there could be a row of BLACK stones with different appearances
                        if i+1==8:
                            #filled with own stones till end of lever
                            break
                        elif boa[x][i] == antistoned:
                            #row is blocked by one stone of the WHITE team
                            break
                        else:
                            #there is an empty space
                            directions[0]=1
                elif boa[x][y+1]==antistoned and act == 2:
                    if y+1<len(boa[x]):
                        if boa[x][y+2]==0:
                            directions[0]=1
    
    #####to go: what moves can you do?
    #####

    return directions

def FullTurn(TURN, BOARD, GOAL, WEIGHT):
    #in a full turn the player has two actions. Here we read out the positions of the stones of the player.
    actions = 2
    player = TURN%2
    if TURN == 0:
        actions = 1
    possiblestones = Stones(BOARD, player)
    if player == 1:
        possiblestones.reverse() #We don't want to rotate the board. But we want to have another positioning-patter
    
    number = len(possiblestones)
    print("Your possible stones are:", possiblestones)
    print("Player", player, " choose one of your", number, "stones")
    errortest = 0
    stonenumber = input("Choose your stone:")

    #test of input
    while errortest == 0:
        if(stonenumber.isdigit()):
            if int(stonenumber) > 0 and int(stonenumber) < int(number) + 1:
                errortest = 1
            else:
                print("Input is not a number between 1 and ", number)
                stonenumber = input("Choose your stone:")
        else:
            print("Input is not a number between 1 and ", number)
            stonenumber = input("Choose your stone:")
    chosen = possiblestones[int(stonenumber)-1]
    
    possiblestonemoves = PossibleMove(BOARD,WEIGHT,actions,player,chosen)
    print(possiblestonemoves)

    #####MakeMove()
    ##### hier geht es weiter!!!!!
    

    #####
    game.append(BOARD)

    #status of the board and the points are returned
    return [BOARD,GOAL]

def PlayGame():
    #initialisation of a new game
    #player0 has 1s (WHITE) and player1 has 3s (BLACK)
    board = [[1,1,0,0,0,0,3,3],
           [1,1,0,0,0,0,3,3],
           [0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0,3,3],
           [1,1,0,0,0,0,3,3],
           [0,0,0,0,0,0,0,0],
           [1,1,0,0,0,0,3,3],
           [1,1,0,0,0,0,3,3]]
    game= [board] #save whole game
    goal = [0,0]
    weight = Weight(board)
    #print(w)
    count = 0
    while count < 3:
         status = FullTurn(count, board, goal, weight)
         board = status[0]
         goal = status[1]
         weight = Weight(board)
         count = count + 1
         if goal[0] > 3 or sum(weight) == -8:
             print("player0 has won the game")
             break
         elif goal[1] > 3 or sum(weight) == 8:
             print("player1 has won the game")
             break
    ##To do: same board over and over again.

def Weight(BOARD):
    #calculates the current orientation of the levers
    output = []
    rot = 1
    for i in BOARD:
        m = rot
        h = -8
        for j in i:
            m = j%2 * h + m
            h = h + 2
            if h == 0:
                h = h + 2
        #print(m)
        rot = -rot
        output.append(m)
    ###finished
    return output

def Stones(b,p):
    #returns the position of all stones of player p at boardstatus b
    if p == 0:
        value = 1
    else:
        value = 3
    positions = [];
    x = 0
    for i in b:
        y = 0
        for j in i:
            if j == value:
                positions.append([x,y])
            y = y + 1
        x = x + 1
    ###finished
    return positions


game = []
PlayGame()
print(game)
