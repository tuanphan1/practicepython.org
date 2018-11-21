# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, 
# this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, 
# not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

import itertools

game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

game2 = [[2, 1, 1],
         [2, 1, 1],
         [1, 2, 2]]

gameOver = False

def sameItem(items):
    return all(x == items[0] for x in items)

def checkWin(gameList):
    gameRotated = [list(a) for a in zip(gameList[0],gameList[1],gameList[2])]
    print(gameRotated)
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

            
winner = checkWin(game2)
print("The winner is player " + str(winner))