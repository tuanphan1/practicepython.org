
# Implement a function that takes as input three variables, and returns the largest of the 
# three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python 
# normally takes care of for us. All you need is some variables and if statements!

def max(x, y, z):
    if x > y:
        if x > z:
            return z
        else:
            return x
    else:
        if y > z:
            return y
        else: 
            return z

print(max(1,5,3))