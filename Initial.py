##WebScraper Selenium
from selenium import webdriver

path = "D:\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get("https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=018041&term=2175&session=A")
table = browser.find_element_by_xpath("""//*[@id="1"]""") 
#ObjRows = table.find_elements_by_tag_name("div")

#each list represents a column in the course table, execpt for Time[]; it's an extra list I made
Section=[]
Activity=[]
Day=[]
Location=[]
Prof=[]
Time=[]#the first time is start time the end time is end time


act = table.find_elements_by_class_name("Activity")
sec = table.find_elements_by_class_name("Section")
day = table.find_elements_by_class_name("Day")
loc = table.find_elements_by_class_name("Place")
prof = table.find_elements_by_class_name("Professor")



#this loop fills the empty lists with there respective elements from the school's website
for a, s, d, l, p  in zip(act, sec, day, loc, prof):
    
    #print(i.text, " Of Type= ",type(i.text))
    Activity.append(a.text)
    Section.append(s.text)
    Day.append(d.text)
    Prof.append(p.text)
    Location.append(l.text)
    
#loop to split the actual day from time in the Day list
tmp=[]

for x in Day:
    y = x.split(" ")
    Time = Time+[y[1]+","+y[-1]]
    tmp = tmp+[y[0]]
    
Day = tmp[:] # copy tmp's elements
tmp = [] #Set tmp to an empty list

    
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
print("________________________Time_____________________________\n")
print(Time)



    
    
    
    
    
    
