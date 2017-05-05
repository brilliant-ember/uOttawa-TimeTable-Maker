#
# WebScraper
#
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://pythonprogramming.net/parsememcparseface/"
client = urlopen(url).read().decode("uft-8")
soup = BeautifulSoup(client, "lxml")

#prints all text in the page even if it's not in paragraph tags
print(soup.get_text())

print("\n  //////////////URLS//////////    ")

for url in soup.find_all("a"):
    print(url.get('href'))
