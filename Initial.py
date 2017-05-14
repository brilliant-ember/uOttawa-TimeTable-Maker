###WebScraper Selenium
#from selenium import webdriver
#######dont forget to orint an error mssg if the class instances r from diffrent semsters
#class Course:
#    ''' A class that represents each indivisual course, it has 6 lists which contain information about the course including the time, day and other information'''
#
#    def __init__(self, path, url):
#        '''The Constructor or initalizer'''
#        self.url=url
#        self.path=path
#        
#        #each list represents a column in the course table, execpt for Time[]; it's an extra list I made
#        self.Section=[]
#        self.Activity=[]
#        self.Day=[]
#        self.Location=[]
#        self.Prof=[]
#        self.Time=[]#the first time is start time the end time is end time
#        self.Lister()
#    
#    
#
#    def Lister(self):
#        '''Takes no arguments execpt the class instance and prints the lists of the course which are Section, Activity, Day, Location, Prof and Time, returns nothing
#        self -> null'''
#        path = self.path
#        url = self.url
#        Activity = self.Activity
#        Section= self.Section
#        Day=self.Day
#        Location=self.Location
#        Prof=self.Prof
#        Time=self.Time
#        tmp=[]
#
#        browser = webdriver.Chrome(path)
#        browser.get(url)
#        #table = browser.find_element_by_xpath("""//*[@id="1"]""") 
#        tables = browser.find_elements_by_id("schedule")
#        
#        for table in tables:
#
#            act = table.find_elements_by_class_name("Activity")
#            sec = table.find_elements_by_class_name("Section")
#            day = table.find_elements_by_class_name("Day")
#            loc = table.find_elements_by_class_name("Place")
#            prof = table.find_elements_by_class_name("Professor")
#
#
#            #this loop fills the empty lists with there respective elements from the school's website
#            for a, s, d, l, p  in zip(act, sec, day, loc, prof):
#
#                #print(i.text, " Of Type= ",type(i.text))
#                Activity.append(a.text)
#                Section.append(s.text)
#                Day.append(d.text)
#                Prof.append(p.text)
#                Location.append(l.text)
#
#            #loop to split the actual day from time in the Day list
#
#
#            for x in Day:
#                y = x.split(" ")
#                Time.append(y[1]+","+y[-1])
#                tmp = tmp+[y[0]]
#
#            self.Day = tmp[:] # copy tmp's elements
#            #tmp = [] #Set tmp to an empty list
#        
#        '''
#       print("_______________________Day______________________________")
#        print(Day)
#        print("________________________Act_____________________________\n")
#        print(Activity)
#        print("_______________________Sec______________________________\n")
#        print(Section)
#        print("_______________________Loc______________________________\n")
#        print(Location)
#        print("________________________Prof_____________________________\n")
#        print(Prof)
#        print("________________________Time_____________________________\n")
#        print(Time)
#        '''
#
#        
#    def CourseName(self):
#        ''' Returns the name if the course with the section
#        null-> List[]'''
#        #problem im solving right now, each class has a section and each lab has a section, how will I know what to return
#        sections =[]
#        for i in self.Section:
#            x = i[0:11]
#            sections.append(x)
#        return sections
#            
#        
# 
#
#    
#    
#   
#    
#path = "D:\chromedriver.exe"
##course1 = Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=018041&term=2175&session=A")
##print("_____________________________")
##print(course1.CourseName())
##print(course1.Day)
##print("_____________________________")
##course2 = Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=011209&term=2179&session=FS")
##print(course2.CourseName())
##print(course2.Day)
##print("_____________________________")
##course3 = Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=020730&term=2181&session=FS")
##print(course3.CourseName())
##print(course3.Day)
#
#
#
#
##-------------------------day of the week class------------------------------#
##My approch to the problem
#'''
#Each day has 29 timeslots, each represents half an hour. each timeslot will be an object (class) and it will have a methode isOccupied which tells if that time slot has already been taken by returning a boolean.
#-The class will also have a method which fills that time table with a course, and will change the obj boolean once the slot is full.
#-The toString methode will print the time slot and the occuping course; maybe also section, and if the slot is empty it would print the time of the slot and empty
#Eg: "9:00, ITI110 Z00" or "8:30, Empty".
#-Each day is a list of timeslots.
#-I used the 24 hour format rather than AM and PM, at last for the sake of coding.
#'''
#
#
#class Time:
#    '''Represents a half an hour of the day'''
#    def __init__(self,time):
#        self.slot = time
#        self.Empty= False
#        self.section=None
#        self.activity=None
#        self.location=None
#        self.prof=None
#        
#    def isOccupied(self):
#        '''Null -> Boolean'''
#        return self.Empty
#    
#    def fill(self, sec, act, loc, pro):
#        '''Null -> Null'''
#        self.secton = sec
#        self.activity=act
#        self.location=loc
#        self.prof=pro
#        self.Empty = True
#        
#        
#    def __repr__(self):
#        return str(self.slot)
#        
#    def __str__(self):
#        e = str(self.isOccupied())
#        s=str(self.slot)
#        if self.section==None:
#            return s+ " "+e
#        else:
#             return s+ " " + this.secton
#        
#          
#t=8.00
#Day= []
#for eine in range(0, 28):
#    s=eine=Time(t)
#    Day.append(s)
#    if (t+0.30) > int(t)+0.50:
#        t = int(t)+1.00
#    else:
#        t = t+0.30
#        
#     
## to account for hour 22 or 10pm   
#s=Time(22.00)
#Day.append(s)
#
#
##Sat=Day[:]
##Sun=Day[:]
##Mon=Day[:]
##Tue=Day[:]
##Wed=Day[:]
##Thu=Day[:]
##Fri=Day[:]
##
##Week=[Sat,Sun,Mon,Tue,Wed,Thu,Fri]
#
####Testing lists to test the class without the need for internet
#
#Section1 = ['ELG2138 A00', 'ELG2138 A00', 'ELG2138 A03', 'ELG2138 A04', 'ELG2138 A01', 'ELG2138 A02', 'ELG2138 B00', 'ELG2138 B00', 'ELG2138 B03', 'ELG2138 B04', 'ELG2138 B01', 'ELG2138 B02']
#Activity1=['LEC', 'LEC', 'DGD', 'DGD', 'LAB', 'LAB', 'LEC', 'LEC', 'DGD', 'DGD', 'LAB', 'LAB']
#Time1=['11:30,13:00', '13:00,14:30', '14:30,16:00', '14:30,16:00', '14:30,17:30', '19:00,22:00', '10:00,11:30', '8:30,10:00', '16:00,17:30', '16:00,17:30', '16:00,19:00', '10:00,13:00']
#Location1=['LPR 155', 'LPR 155', 'MRT 221', 'MNO C211', 'DEP DEPT', 'DEP DEPT', 'HGN 302', 'STE H0104', 'MRT 221', 'LMX 390', 'DEP DEPT', 'DEP DEPT']
#Day1=['Wednesday', 'Monday', 'Thursday', 'Thursday', 'Wednesday', 'Tuesday', 'Thursday', 'Monday', 'Wednesday', 'Wednesday', 'Friday', 'Tuesday']
##--------------#-----------------------------------------------------
#Section2=['MCG1100 A00', 'MCG1100 A01', 'MCG1100 A01', 'MCG1100 B00', 'MCG1100 B01', 'MCG1100 B01', 'MCG1100 C00', 'MCG1100 C01', 'MCG1100 C01', 'MCG1100 D00', 'MCG1100 D01', 'MCG1100 D01']
#Activity2=['LEC', 'LAB', 'LAB', 'LEC', 'LAB', 'LAB', 'LEC', 'LAB', 'LAB', 'LEC', 'LAB', 'LAB']
#Time2=['11:30,13:00', '8:00,10:00', '14:30,17:30', '17:30,19:00', '12:00,14:00', '19:00,22:00', '14:30,16:00', '18:30,20:30', '13:00,16:00', '17:30,19:00', '8:00,10:00', '19:00,22:00']
#Location2=['STE C0136', 'DEP DEPT', 'DEP DEPT', 'STE C0136', 'DEP DEPT', 'DEP DEPT', 'STE C0136', 'DEP DEPT', 'DEP DEPT', 'STE C0136', 'DEP DEPT', 'DEP DEPT']
#Day2=['Thursday', 'Friday', 'Friday', 'Thursday', 'Monday', 'Tuesday', 'Wednesday', 'Tuesday', 'Thursday', 'Monday', 'Thursday', 'Monday']
##_________________________________________________________________
#Section3=['ITI1121 Z00', 'ITI1121 Z00', 'ITI1121 Z01', 'ITI1121 Z02', 'ITI1121 Z03']
#Activity3=['LEC', 'LEC', 'LAB', 'LAB', 'LAB']
#Time3=['11:30,13:00', '13:00,14:30', '11:30,14:30', '8:30,11:30', '8:30,11:30']
#Location3=['MRT 218', 'MRT 218', 'STE 2060', 'STE 2060', 'STE 2060']
#Day3=['Wednesday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
###_________________________________________________________________
##
##Section4=
##Activity4=
##Time4=
##Location4=
##------------------------------------------------------------------
#
#
#class Table:
#    def __init__(self):                                                                                  
#        self.Sat = Day[:]                                                                            
#        self.Sun = Day[:]                                                                            #
#        self.Mon = Day[:]                                                                            #
#        self.Tue = Day[:]                                                                            #
#        self.Wed = Day[:]                                                                            #
#        self.Thu = Day[:]                                                                            #
#        self.Fri = Day[:]                                                                            #
#        self.Week = [self.Sat, self.Sun, self.Mon, self.Tue, self.Wed, self.Thu, self.Fri]           #
#                                                                                                     #
#    def maker(self):
#        '''Makes a table with the approperiate course sessions'''
#        pass
#    def print(self):
#        '''Prints a Stirng representaion for the Table'''
#        print("_______________________________________________________________________________________________________________________________________________________________________________________________________")
#        print('{Tme:  | 8.0 | 8.3 | 9.0 | 9.3 | 10.0| 10.3| 11.0| 11.3| 12.0| 12.3| 13.0| 13.3| 14.0| 14.3| 15.0| 15.3| 16.0| 16.3| 17.0| 17.3| 18.0| 18.3| 19.0| 19.3| 20.0| 20.3| 21.0| 21.3| 22.0}')
#        
#        
#        W=['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
#        w=0
#        for day in self.Week:
#            Printed=[]
#            Printed.append(W[w]+": ")
#            w=w+1
#            for slot in day:
#                
#                if slot.isOccupied()==True:
#                    Printed.append("-F-")
#                else: Printed.append("_E_")
#            
#            Printed=str(Printed)
#            Printed=Printed.replace(","," |")
#            Printed=Printed.replace("'","")
#            print(Printed)
#            
#        print("_______________________________________________________________________________________________________________________________________________________________________________________________________")
#                    
#            
#
#
#            
#            


SecNum_param1=""
SecNum_param2=0
def SecNum(Lsec, SecNum_param1, SecNum_param2):
    '''Takes a list of sections,an empty string and number 0, to retuen the number of sections in the list.
    the empty string and number zero are passed by the above declaration SecNum_param1="" and SecNum_param2=0
    SecNum([sections], "", 0) --> Integer
     
     Example usage:
    #1  Lsec=['ELG2138 A00', 'ELG2138 A00', 'ELG2138 A03', 'ELG2138 A04', 'ELG2138 A01', 'ELG2138 A02', 'ELG2138 B00', 'ELG2138 B00', 'ELG2138 B03', 'ELG2138 B04', 'ELG2138 B01',            'ELG2138 B02']

        SecNum(Lsec,SecNum_param1,SecNum_param2) --returns-->2
    
    #2  Lsec=['ITI1121 Z00', 'ITI1121 Z00', 'ITI1121 Z01', 'ITI1121 Z02', 'ITI1121 Z03']
        SecNum(Lsec,SecNum_param1,SecNum_param2) --returns-->1
    '''
        L = len(Lsec)
        if SecNum_param2+1 == L :
                return len(SecNum_param1)
        else:
                x = Lsec[SecNum_param2]
                if SecNum_param1.find(x[-3]) == -1 :
                        SecNum_param1=SecNum_param1+x[-3]
                        return SecNum(Lsec, SecNum_param1, SecNum_param2+1)
                else:
                        return SecNum(Lsec, SecNum_param1, SecNum_param2+1)
                        
                        


        






    
        
        
        

    
    
    
    
    
    
