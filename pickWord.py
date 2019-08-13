
# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

# In this exercise, the task is to write a function that picks a random word from a list of words from the SOWPODS dictionary. 

import random

with open('sowpods.txt') as wordFile:
    lines = wordFile.readlines()
    lineNumber = random.randint(0,267751)
    print(lines[lineNumber])