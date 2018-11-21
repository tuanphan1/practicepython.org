# The next logical step is to deal with handling user input. When a player (say player 1, who is X) 
# wants to place an X on the screen, they can’t just click on a terminal. So we are going to 
# approximate this clicking simply by asking the user for a coordinate of where they want to place
# their piece.


# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty 
# game board like this:

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

player1 = 1
player2 = 2

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

while(True):
    while move(player1) != True:
        print("Please try again")
    print(game)
    while move(player2) != True:
        print("Please try again")
    print(game)