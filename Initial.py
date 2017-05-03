##WebScraper lxml
#use chcp 65001 in terminal in case of an encoding error
from urllib.request import urlopen
from bs4 import BeautifulSoup 

url="https://pythonprogramming.net/parsememcparseface/"
client=urlopen(url).read()
soup=BeautifulSoup(client, "lxml")

#print(soup.find_all("p")) #finds all object p tags in the page{paragraphs}

#for paragraph in soup.find_all("p"): 
 #   print (paragraph.text) # only prints paragraphs not all texts
    
print(soup.get_text())#prints all text in the page even if it's not in paragraph tags
