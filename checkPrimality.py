
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity 
# to practice using functions, described below.

def get_integer():
    return int(input("Please enter a prime number: "))

def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

print(isPrime(get_integer()))
