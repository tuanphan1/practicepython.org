
# Use the BeautifulSoup and requests Python packages to print out a list 
# of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

url = 'https://kdvr.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)

for entries in soup.find_all(class_="entry-title"):
    print(entries.text)