##WebScraper Selenium
from selenium import webdriver

path = "D:\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get("https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=018041&term=2175&session=A")
#browser.find_element_by_xpath("""//*[@id="1"]""")
rows = browser.find_elements_by_class_name("display")
for i in rows:
    print(i.text)
    #oneRow=[x.text for x in i]