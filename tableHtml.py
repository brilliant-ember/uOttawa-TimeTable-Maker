'''This module will reformat the html file exported by pandas and makes it into a pretty table in html format'''
from selenium import webdriver

def htmlChanger(htmlPath):
	file = open(htmlPath, "+r").readlines()
	print(file[3])

def firstRowRemover(htmlPath):
	browser = webdriver.Chrome("D:\chromedriver.exe")
	page = browser.get(htmlPath)
	row = page.find_elements_by_tag("tr")
	for i in range(len(row)):
		oneRow = row[i]
		firstCell = oneRow[0]
		print(firstCell)




path = "http://localhost:8000/filename%20-%20Copy.html"

firstRowRemover(path)