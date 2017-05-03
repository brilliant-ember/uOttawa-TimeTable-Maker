##WebScraper lxml
from urllib.request import urlopen
from bs4 import BeautifulSoup 

url="https://pythonprogramming.net/parsememcparseface/"
client=urlopen(url).read()
soup=BeautifulSoup(client, "lxml")

print(soup)#if u r getting Unicode error use this cmmnd in windoews chcp 65001 to use an endong that will fix the issue of the terminal not recognaizing the charecters in conflict

