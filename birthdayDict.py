
birtdayDict = {
    "Tuan1": '04/01/1996',
    "Tuan2": '04/02/1996',
    "Tuan3": '04/03/1996'
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for key in birtdayDict:
    print(key)

name = input("Who's birthday do you want to look up? ")
print(name + "'s" + " birthday is " + birtdayDict[name])
