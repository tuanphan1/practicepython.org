# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) 
# and another number. The function decides whether or not the given 
# number is inside the list and returns (then prints) an appropriate boolean.

import random

choiceList = random.sample(range(1,100), 50)
choiceList.sort()

def checkNum(n):
    if n in choiceList:
        return True
    return False

if __name__=="__main__":
    n = random.randint(0,100)
    print(n)
    print(choiceList)
    print(checkNum(n))