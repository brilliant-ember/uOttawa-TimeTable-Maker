##WebScraper Selenium
from selenium import webdriver

path = "D:\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get("https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=018041&term=2175&session=A")
table = browser.find_element_by_xpath("""//*[@id="1"]""") 
#ObjRows = table.find_elements_by_tag_name("div")


Section=[]
Activity=[]
Day=[]
Location=[]
Prof=[]


act = table.find_elements_by_class_name("Activity")
sec = table.find_elements_by_class_name("Section")
day = table.find_elements_by_class_name("Day")
loc = table.find_elements_by_class_name("Place")
prof = table.find_elements_by_class_name("Professor")





for a, s, d, l, p  in zip(act, sec, day, loc, prof):
    
    #print(i.text, " Of Type= ",type(i.text))
    Activity.append(a.text)
    Section.append(s.text)
    Day.append(d.text)
    Prof.append(p.text)
    Location.append(l.text)
    


    
print("_______________________Day______________________________")
print(Day)
print("________________________Act_____________________________\n")
print(Activity)
print("_______________________Sec______________________________\n")
print(Section)
print("_______________________Loc______________________________\n")
print(Location)
print("________________________Prof_____________________________\n")
print(Prof)



    
    
    
    
    
    
