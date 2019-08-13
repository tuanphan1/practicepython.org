
# Create a program that will play the “cows and bulls” game with the user. The game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the 
# user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly 
# in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” 
# they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses 
# the user makes throughout teh game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.

import random

randNum = ''.join(random.sample('0123456789', 4))
cow = 0
bull = 0

def cowsAndBull(n):
  cow = 0
  bull = 0
  randNumList = [int(d) for d in str(randNum)]
  guessNumList = [int(d) for d in str(n)]

  for indexA, a in enumerate(randNumList):
    for indexB, b in enumerate(guessNumList):
      if a == b:
        cow = cow + 1
        if indexA == indexB:
          bull = bull + 1
        break
  
  print(str(cow) + " cows, " + str(bull) + " bulls")
  return(bull)

if __name__=="__main__":
  print(randNum)
  
  while(bull != 4):
    user_num = int(input("Give me a number: "))
    bull = cowsAndBull(user_num)
  