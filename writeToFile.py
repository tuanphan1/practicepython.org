
# Take the code from the How To Decode A Website exercise 
# (if you didn’t do it or just want to play with some different code, 
# use the code from the solution), and instead of printing the 
# results to a screen, write the results to a txt file. In your code, 
# just make up a name for the file you are saving to.

import requests
from bs4 import BeautifulSoup

url = 'https://kdvr.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)

with open('fileText.txt', 'w') as open_file:
    for entries in soup.find_all(class_="entry-title"):
        open_file.write(entries.text + '\n')
        print(entries.text)