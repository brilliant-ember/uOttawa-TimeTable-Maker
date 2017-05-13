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
        self.Lister()
    
    

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
        tmp=[]

        browser = webdriver.Chrome(path)
        browser.get(url)
        #table = browser.find_element_by_xpath("""//*[@id="1"]""") 
        tables = browser.find_elements_by_id("schedule")
        
        for table in tables:

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


            for x in Day:
                y = x.split(" ")
                Time.append(y[1]+","+y[-1])
                tmp = tmp+[y[0]]

            self.Day = tmp[:] # copy tmp's elements
            #tmp = [] #Set tmp to an empty list
        
        '''
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
        '''

        
    def CourseName(self):
        pass
        ''' Returns the name if the course with the section'''
        #problem im solving right now, each class has a section and each lab has a section, how will I know what to return
        

#'''
    
        

    
path = "D:\chromedriver.exe"
course1 = Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=011209&term=2179&session=FS&yearOfStudy=2")
print("_____________________________")
print(course1.Time)
print(course1.Activity)
print(course1.Day)


#-------------------------day of the week class------------------------------#
#My approch to the problem
'''
Each day has 28 timeslots, each represents half an hour. each timeslot will be an object (class) and it will have a methode isOccupied which tells if that time slot has already been taken by returning a boolean.
-The class will also have a method which fills that time table with a course, and will change the obj boolean once the slot is full.
-The toString methode will print the time slot and the occuping course; maybe also section, and if the slot is empty it would print the time of the slot and empty
Eg: "9:00, ITI110 Z00" or "8:30, Empty".
-Each day is a list of timeslots.
-I used the 24 hour format rather than AM and PM, at last for the sake of coding.
'''

    
    
    
    
    
    
