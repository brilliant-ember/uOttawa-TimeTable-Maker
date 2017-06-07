'''This module will reformat the html file exported by pandas and makes it into a pretty table in html format'''


def htmlChanger(htmlPath):
	file = open(htmlPath, "+r").readlines()
	print(file[3])

