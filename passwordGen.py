
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a 
# mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating 
# a new password every time the user asks for a new password. Include your run-time code in a main method.

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

def passLength():
    return int(input("Please enter length of random password"))

def genPassword(n):
    passList = random.sample(s, n)
    passString = ''.join(passList)
    return passString

print(genPassword(passLength()))