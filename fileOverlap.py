
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
# happy numbers up to 1000.

firstList = []
secondList = []

with open('list1.txt') as list1:
    line = list1.readline()
    while line:
        firstList.append(int(line))
        line = list1.readline()
    list1.close()
        
with open('list2.txt') as list2:
    line = list2.readline()
    while line:
        secondList.append(int(line))
        line = list2.readline()
    list2.close()

print(set(firstList).intersection(secondList))