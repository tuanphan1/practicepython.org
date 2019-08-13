
#TickTacToe Game in python

import itertools

horizontalLine = " ---"
verticalLine = "|"
space = "   "

boardSize = 3
gameOver = False
player1 = 1
player2 = 2
winner = 0

game = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

def printBoard():
    print(horizontalLine * boardSize)
    for i in range(boardSize):
        print(((verticalLine + space) * boardSize) + verticalLine)
        print(horizontalLine * boardSize)

def sameItem(items):
    return all(x == items[0] for x in items)

def checkWin(gameList):
    gameRotated = [list(a) for a in zip(gameList[0],gameList[1],gameList[2])]
    for i in range(3):
        if gameList[i][0] == 1 or gameList[i][0] == 2:
            if sameItem(gameList[i]):
                return gameList[i][0]
        if gameList[0][i] == 1 or gameList[0][i] == 2:
            if sameItem(gameRotated[i]):
                return gameList[0][i]
    
    if game[1][1] != 0:
        if game[1][1] == game[0][0] == game[2][2]: 
            return game[1][1]
        elif game[1][1] == game[0][2] == game[2][0]:
            return game[1][1]
    return 0		

def move(player):
    playerInput = input("Player " + str(player) + " Please enter a move in the format x,y ")
    playerInput.strip()
    moveList = [int(x) for x in playerInput.split(",")]
    if game[moveList[0]][moveList[1]] == 0:
        game[moveList[0]][moveList[1]] = player
        return True
    else:
        print("This move is invalid")
        return False

def runGame():
    moves = 0
    while(not gameOver and moves < 9):
        while move(player1) != True:
            print("Please try again")
        moves = moves + 1
        winner = checkWin(game)
        if winner == 1 or winner == 2:
            return winner
        print(game)
        while move(player2) != True:
            print("Please try again")
        moves = moves + 1
        winner = checkWin(game)
        if winner == 1 or winner == 2:
            return winner
        print(game)
        if moves >= 9:
            return 0

print(str(runGame()) + " has won the game") 