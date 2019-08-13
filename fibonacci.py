
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter 
# the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers 
# where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence 
# looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def getInt():
    return int(input("Please enter number of Fibonnaci number to generate: "))

def genFibo(n):
    if n == 0:
        fibList = []
        return fibList
    first = 0
    second = 1
    fibList = [1]
    while(len(fibList) !=  n):
        fibList.append(first+second)
        first = second
        second = fibList[len(fibList)-1]
    return fibList

print(genFibo(getInt()))
