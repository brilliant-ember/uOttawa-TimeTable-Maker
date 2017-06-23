'''This module takes input from the GUI and starts the main program. It uses the data to extract urls then puts those in the main program'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Schedule import MultiPossibleTables as multi
from time import time

urlList = []
url = "https://web30.uottawa.ca/v3/SITS/timetable/Search.aspx"
#path = "D:\chromedriver.exe"
path = r"D:\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe"
def urlExtract(L, styleInt):
	for j in range(1, len(L)):
		'''takes a list made of [the semester, the rest of courses as strings]'''
		t = time()
		browser = webdriver.PhantomJS(path)
		#browser = webdriver.Chrome(path)
		browser.get(url)
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
		#browser.switch_to.frame("textarea_iframe")
		#wait = WebDriverWait(browser, 10)
		course = L[j]
		if len(course) ==7:

			#user = wait.until(EC.visibility_of(input2))
			input1.send_keys(course[:3])
			input2.send_keys(course[3:])
			submitB.click()
			link = browser.find_element_by_class_name("CourseCode").find_element_by_tag_name("a").get_attribute('href')

			urlList.append(link)
	
	print(urlList)
	print("In "+str(time()-t))
	#multi(urlList)

##Now the scedule function takes the links list and the style number

	#browser.switch_to.default_content()




	


urlExtract(["w","iti1100", "iti1121"], 5)
