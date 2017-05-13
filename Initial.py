##WebScraper Selenium
from selenium import webdriver

class Course:
    ''' A class that represents each indivisual course, it has 6 lists which contain information about the course including the time, day and other information'''

    def __init__(self, path, url):
        '''The Constructor or initalizer'''
        self.url=url
        self.path=path
        
        #each list represents a column in the course table, execpt for Time[]; it's an extra list I made
        self.Section=[]
        self.Activity=[]
        self.Day=[]
        self.Location=[]
        self.Prof=[]
        self.Time=[]#the first time is start time the end time is end time
    
    

    def Lister(self):
        '''Takes no arguments execpt the class instance and prints the lists of the course which are Section, Activity, Day, Location, Prof and Time, returns nothing
        self -> null'''
        path = self.path
        url = self.url
        Activity = self.Activity
        Section= self.Section
        Day=self.Day
        Location=self.Location
        Prof=self.Prof
        Time=self.Time

        browser = webdriver.Chrome(path)
        browser.get(url)
        table = browser.find_element_by_xpath("""//*[@id="1"]""") 
        #ObjRows = table.find_elements_by_tag_name("div")




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

    
course1 = Course("D:\chromedriver.exe", "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=018041&term=2175&session=A")
course1.Lister()



    
    
    
    
    
    
