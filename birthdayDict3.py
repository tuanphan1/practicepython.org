
import json
from collections import Counter

birthdayDict = {}
birthdayList = []
with open("birthday.json") as birthdayFile:
    birthdayDict = json.load(birthdayFile)

for key in birthdayDict:
    birthdayList.append(birthdayDict[key][:2])

print(Counter(birthdayList))