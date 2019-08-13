
# Given a .txt file that has a list of a bunch of names, count how many of each name there are in 
# the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

nameDict = {"Darth": 0, "Luke": 0, "Lea": 0}

with open('namelist.txt') as openFile:
    line = openFile.readline()
    while line:
        line = line.replace('\n', '')
        nameDict[line] = nameDict[line] + 1
        line = openFile.readline()
 
print(nameDict)

