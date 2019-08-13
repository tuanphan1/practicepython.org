
import json

birthdayDict = {}
with open("birthday.json") as birthdayFile:
    birthdayDict = json.load(birthdayFile)

print("Welcome to the birthday dictionary. We know the birthdays of:")
for key in birthdayDict:
    print(key)

name = input("Who's birthday do you want to look up? ")
print(name + "'s" + " birthday is " + birthdayDict[name])