
# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)
import random

number = random.randint(1,9)

guess = input("guess the number between 1 - 9 ")
guess = int(guess)
if guess == number:
    print("You got the right number")
elif guess > number:
    print("Your guess is high, the number was :" + str(number))
elif guess < number:
    print("Your guess is low, the number was :" + str(number))