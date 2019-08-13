
import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

birthdayDict = {}
birthdayList = []
x_categories = ["January", "Febuary", "March", "April", 
                "May", "June", "July", "August", 
                "Meptember", "October", "November", "December"]

x = []
y = []

numToString = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

with open("birthday.json") as birthdayFile:
    birthdayDict = json.load(birthdayFile)

for key in birthdayDict:
    birthdayList.append(birthdayDict[key][:2])
    x.append(numToString[int(birthdayDict[key][:2])])

c = Counter(birthdayList)
for key in c:
    y.append(c[key])

print(x)
print(y)
# we specify an HTML file where the output will go
output_file("plot.html")

p = figure(x_range=x_categories)
p.vbar(x=x, top=y, width=0.5)

show(p)
