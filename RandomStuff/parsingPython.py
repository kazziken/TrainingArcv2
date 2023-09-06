#this block of code uses urllib to open the link and read the contents
#then spill out the contents, urlopen keeps the headers so it won't output any header

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')

for line in fhand:
    print(line.decode().strip())



#Webscrapping or parsing HTML docs
#use BeautifulSoap to parse HTML docs and extract data from them.
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieves all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))