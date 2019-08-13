#
#  This time, we’re going to do exactly the opposite. You, the user, will have in your head a number
# between 0 and 100. The program will guess a number, and you, the user, will say whether it is too 
# high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

def guessNumber():
    low = 0
    high = 100
    notCorrect = True
    attemps = 0
    print("I will guess a number you're thinking between 0 - 100")
    while(notCorrect):
        attemps = attemps + 1
        guess = int((low + high)/2)
        notCorrect = int(input("Was your number " + str(guess) + " enter 1 for True, 2 for low, 3 for high "))
        if notCorrect == 1:
            print("Guess took " + str(attemps) + " attemps")
        elif notCorrect == 2:
            low = guess
        elif notCorrect == 3:
            high = guess

if __name__ == '__main__':
    guessNumber()