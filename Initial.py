##WebScraper 
from urllib.request import urlopen
from bs4 import BeautifulSoup 
wiki = "https://en.wikipedia.org/wiki/Shakespeare_Programming_Languagehttps://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

uClient = urlopen(wiki)
html=uClient.read()
uClient.close()
#html parsing
soup=BeautifulSoup(html, "html.parser")
#print (soup.prettify())
soup.h1