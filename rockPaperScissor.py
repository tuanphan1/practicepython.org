# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
playAgain = "Y"
while (playAgain == "Y"):
    gameDict = {"rock": 1, "paper": 2, "scissor": 3}
    p1 = input("Player1: please enter rock, paper, or scissor ")
    p2 = input("Player2: please enter rock, paper, or scissor ")
    p1num = gameDict.get(p1)
    p2num = gameDict.get(p2)
    dif = int(p1num - p2num)

    if dif == 0:
        playAgain = input(print("draw, want to play again? Y/N"))
    elif dif == 1 or dif == -2:
        print("player 1 wins ")
        playAgain = input(print("do you want to play again? Y/N"))
    elif dif == -1 or dif == 2:
        print("player 2 wins ")
        playAgain = input(print("do you want to play again? Y/N"))



    




    
