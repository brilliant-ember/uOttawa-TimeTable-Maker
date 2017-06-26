'''This module takes input from the GUI and starts the main program. It uses the data to extract urls then puts those in the main program'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Schedule import MultiPossibleTables as multi
from time import time
from tkinter import *
import threading as T
import multiprocessing as M
from Schedule import style
from selenium.common.exceptions import TimeoutException

url = "https://web30.uottawa.ca/v3/SITS/timetable/Search.aspx"
path = "D:\chromedriver.exe"
#path = r"D:\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe"

def urlExtract(L, urlList):
	'''takes a course code and spits urls'''
	browser = webdriver.Chrome(path)
	browser.get(url)
	for j in range(1, len(L)):
		'''takes a list made of [the semester, the rest of courses as strings]'''

		#browser = webdriver.PhantomJS(path)
		#select = Select(browser.find_element_by_xpath
		menu = browser.find_element_by_tag_name("select")
		option = menu.find_elements_by_tag_name("option")
		input1 = browser.find_element_by_id("ctl00_MainContentPlaceHolder_Basic_SubjectText")
		input2 = browser.find_element_by_id("ctl00_MainContentPlaceHolder_Basic_CatalogNumberText")
		submitB = browser.find_element_by_id("ctl00_MainContentPlaceHolder_Basic_Button")

		semList = ["Fall", "Winter", "Summer"]
		if L[0] == "f":
			semster = semList[0]
		elif L[0] == "w":
			semster = semList[1]
		elif L[0] == "s":
			semster = semList[2]

		for i in option:
			if semster in i.text:
				i.click()
				break
		course = L[j]
		if len(course) ==7:

			input1.send_keys(course[:3])
			input2.send_keys(course[3:])
			submitB.click()
			try:
				link = browser.find_element_by_class_name("CourseCode").find_element_by_tag_name("a").get_attribute('href')
			except:
				popup = Tk()
				popup.title("I found an Error heehe >.< ") 
				label =Label(popup, text="I couldn't find "+course+", Make sure the course code and semseter are right ", font = ("Vendera", 10, "bold"))
				label.pack(fill = "x", pady = 10, padx=7)
				b = Button(popup, text="Destroy?", command = popup.destroy)
				b.pack(side=BOTTOM, pady=7)

				popup.mainloop()


			urlList.append(link)
			if j != len(L) -1 :
				browser.get(url)
	


	##Now toss to the Scedule method

	


# t1 = T.Thread(target = urlExtract, args=(["w","iti1100"], 5) )
# t2 = T.Thread(target = urlExtract, args=(["w","iti1121"], 5) )
# t1.start()
# t2.start()

# t1.join()
# t2.join()
def mainMethod(list_of_courses, styleNo):


	if len(list_of_courses) == 2:
		ZaList = []
		urlExtract(list_of_courses, ZaList)
		multi(ZaList)

	elif len(list_of_courses) ==3 : #when u have 2 courses
		twoCourses(list_of_courses)



def twoCourses(list_of_courses):
	sem = list_of_courses[0]
	c1 = list_of_courses[1:2]
	c1.insert(0, sem)
	c2 = list_of_courses[2:]
	c2.insert(0, sem)

	if __name__ == "__main__":
		with M.Manager() as manager:
			l = manager.list()
			m1 = M.Process(target= urlExtract, args=( c1, l))
			m2 = M.Process(target= urlExtract, args=( c2, l))
			m1.start()
			m2.start()
			m1.join()
			m2.join()
			multi(l)








t = time()
co = ["w", "iti1121","iti1100"]
try:
	a = mainMethod(co, 1)
#twoCourses(co)
except TimeoutException:
	popup = Tk()
	popup.title("Guess What?! i got an error ;) ") 
	label =Label(popup, text="I couldn't find "+course+", I can't connect, check your internet connection ", font = ("Vendera", 10, "bold"))
	label.pack(fill = "x", pady = 10, padx=7)
	b = Button(popup, text="Destroy?", command = popup.destroy)
	b.pack(side=BOTTOM, pady=7)

	popup.mainloop()




print("In "+str(time()-t))

