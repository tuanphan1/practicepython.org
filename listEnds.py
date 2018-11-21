# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. For practice, 
# write this code inside a function.

import random

a = [5, 10, 15, 20, 25]
b = random.sample(range(100), 20)

print(b)

c = []
c.append(b[0])
c.append(b[len(b)-1])

print(c)