###WebScraper Selenium
from selenium import webdriver
#######dont forget to orint an error mssg if the class instances r from diffrent semsters
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
        
        self.seprateSections = []  #A list whose elements r lists where each list represents all activities for one section, and those activities are grouped in lists based on the activity type
        self.secDays = [] #a list that contains lists, each sublist has the days of the week assciated with a section
        self.secTimes = []
        self.secLocs = []
        self.secProfs =[]

        self.dayCalander = [] # A list that contains dicttionaries, one for each sec. there're 7 keys for all dictionaries for the days of the week, the content in each dic is a list of days for all the possible ways a day can be made, if the dic has an empty list then that day isn't required at all for that section
        self.Lister()
        self.numberOfSections = self.SecNum()
        self.Seprate()
        
        
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
        #self.numberOfSections = len(tables) Doesn't work cuz not allways r tables seprate based on secs, sometimes there re 3 sections but one table
                
        for table in tables:

            act = table.find_elements_by_class_name("Activity")
            sec = table.find_elements_by_class_name("Section")
            day = table.find_elements_by_class_name("Day")
            loc = table.find_elements_by_class_name("Place")
            prof = table.find_elements_by_class_name("Professor")
            Asec = []
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
                Time.append(y[1].replace(":",".")+","+y[-1].replace(":","."))
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
        ''' Returns the name if the course with the section
        null-> List[]'''
        #problem im solving right now, each class has a section and each lab has a section, how will I know what to return
        sections =[]
        for i in self.Section:
            x = i[0:11]
            sections.append(x)
        return sections
    
    
    
    def Seprate(self): 
        '''Returns lists each list represents a section, and in each sectionlist there are lists represting all activities(a list per activity)
        self.Seprate() --> [[[Lectures A], [DGDs A], [Labs A]], [[Lectures B], [DGDs B], [Labs B]]], And the same idea for the days and other info of each sec
        example output.
        self.Seprate()-->[[['ELG2138 A00', 'ELG2138 A00'], ['ELG2138 A03', 'ELG2138 A04'], ['ELG2138 A01', 'ELG2138 A02']], [['ELG2138 B00', 'ELG2138 B00'], ['ELG2138 B03', 'ELG2138 B04'], ['ELG2138 B01', 'ELG2138 B02']]]
        --                --    ---------------------------                     --
        [['Wednesday', 'Monday', 'Thursday', 'Thursday', 'Wednesday', 'Tuesday'], ['Thursday', 'Monday', 'Wednesday', 'Wednesday', 'Friday', 'Tuesday']]
        --                ----------------------------------                         --------
        ______#@_______for preformance THERE IS NO OUT OUTPUT, THE FUNCTION TORES THE VALUE TO VARIABLE (self.seprateSections)-------------------@#-------------------- '''
        Lact = self.Activity
        Lsec = self.CourseName()
        Nsec = self.numberOfSections
        Out=[]
        act_per_sec = Lact[:int(len(Lact)/Nsec)]
        D = 0
        DaysL = []
        ProfL = []
        TimeL = []
        LocL =  []
        
        x = 0
        for j in range(Nsec): #number of sections
            days_per_sec = []
            prof = []
            time =[]
            locl= []
            act = Lact[D]
            tmp = []
            tmp2 = []
            for i in act_per_sec:
                days_per_sec.append(self.Day[x])
                prof.append(self.Prof[x])
                time.append(self.Time[x])
                locl.append(self.Location[x])
                #print(self.Day[x])
                x = x+1
                if i == act:
                    tmp2.append(Lsec[D])
                    act = Lact[D]
                    D = D+1

                else:
                    tmp.append(tmp2)
                    tmp2=[]
                    tmp2.append(Lsec[D])
                    act = Lact[D]
                    D = D+1
            #print("Loop")
            tmp.append(tmp2)       
            Out.append(tmp)
            DaysL.append(days_per_sec)
            ProfL.append(prof)
            TimeL.append(time)
            LocL.append(locl)
            
            

        self.seprateSections = Out[:]
        self.secDays.append(DaysL)
        
        self.secProfs.append(ProfL)
        self.secTimes.append(TimeL)
        self.secLocs.append(LocL)
               
               
             
        
    def SecNum(self, SecNum_param1 = "", SecNum_param2 = 0):
        
         '''A Recursive method. Takes a list of sections,an empty string and number 0, to retuen the number of sections in the list.
     the empty string and number zero are passed by the above declaration SecNum_param1="" and SecNum_param2=0
     self.SecNum() --> Integer
-         Example usage:
      -------------------------------------------------------------------------------------------------
-        #1  Lsec=['ELG2138 A00', 'ELG2138 A00', 'ELG2138 A03', 'ELG2138 A04', 'ELG2138 A01', 'ELG2138 A02', 'ELG2138 B00', 'ELG2138 B00', 'ELG2138 B03', 'ELG2138 B04', 'ELG2138 B01',            'ELG2138 B02']
         SecNum(Lsec,SecNum_param1,SecNum_param2) --returns-->2
         _____________________
     #2  Lsec=['ITI1121 Z00', 'ITI1121 Z00', 'ITI1121 Z01', 'ITI1121 Z02', 'ITI1121 Z03']
         SecNum(Lsec,SecNum_param1,SecNum_param2) --returns-->1
     '''
         Lsec = self.CourseName()
         L = len(Lsec)
         if SecNum_param2+1 == L :
                 return len(SecNum_param1)
         else:
                 x = Lsec[SecNum_param2]
                 #print(x[-3])
                 if SecNum_param1.find(x[-3]) == -1 :
                         SecNum_param1=SecNum_param1+x[-3]
                         return self.SecNum( SecNum_param1, SecNum_param2+1)
                 else:
                         return self.SecNum( SecNum_param1, SecNum_param2+1)

            
         
    
        
        
#    def Calander(self):# to work around the bug in Seprate methode, add i,j,k in anything except the section
#        '''Creates a list of Dictioaries, it fills self.dayCalander list whose description is: A list whose elements r lists where each list represents all activities for one section, and those activities are grouped in lists based on the activity type
#        None --> None
#        [[['ELG2138 A00', 'ELG2138 A00'], ['ELG2138 A03', 'ELG2138 A04'], ['ELG2138 A01', 'ELG2138 A02']], [['ELG2138 B00', 'ELG2138 B00'], ['ELG2138 B03', 'ELG2138 B04'], ['ELG2138 B01', 'ELG2138 B02']]]'''
#        Out = []
#        week = ["Saterday", "Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday"]
#        Nsec = self.numberOfSections
#        for i in range(Nsec):
#            dictn = {"Saterday":[], "Sunday":[], "Monday":[],"Tuesday":[],"Wednesday":[],"Thursday":[],"Friday":[]}
#            sec = self.seprateSections[i]
#            days = self.secDays
#            for j in sec: 
#                activitie_set = sec[j]
#                counter = 0
#                tmp = activitie_set[0][-3:]
#                mandatory_set= []
#                #if len(activitie_set)%2 == 0: #to account for when the activies are even
#                #elif len(activitie_set)%2 != 0: #Odd case
#                
#                for k in activitie_set: #when u have the same tail code (A00) that means that all those r madatory, if u hv diff then u chose on code or the other
#                    session = activitie_set[k]
#                    if tmp == session[-3:]:
#                        mandatory_set.append([i,j,k, session])
#                        tmp = mandatory_set[counter][-1][-3:] 
#                        counter = counter +1
#                    else:
#                        for x in mandatory_set:
#                            classDay = self.secDays[i][j][k]
#                            dictDay= dictn[classDay]
#                            classTime = secTimes[i][j][k]
#                            if len(dictDay)==0 or t.isEmpty() for 
#                            
#                        
                        
                        
                        
                        
                        
                        
#                        for day in week:# check if the days are the same
#                            tmpDay=Day[:]
#                            if self.secDays[i][j][k] == day:
#                                
#                                 # dont forget to add all possible day configs to the dictionary
#                                    
#                                for timesSlot in possibleDay:#all the time slots
#                                    if timeSlot.isEmpty():
#                                            
                                        
                                    
                                
                                
        
        
        
path = "D:\chromedriver.exe"

        
        

course1 = Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=015025&term=2181&session=FS")
print("____________Finalllll  ________________")

print(course1.numberOfSections)
print(course1.seprateSections)
print(course1.secDays)
print(course1.secTimes)



#
##-------------------------day of the week class------------------------------#
#My approch to the problem
'''
Each day has 29 timeslots, each represents half an hour. each timeslot will be an object (class) and it will have a methode isOccupied which tells if that time slot has already been taken by returning a boolean.
-The class will also have a method which fills that time table with a course, and will change the obj boolean once the slot is full.
-The toString methode will print the time slot and the occuping course; maybe also section, and if the slot is empty it would print the time of the slot and empty
Eg: "9:00, ITI110 Z00" or "8:30, Empty".
-Each day is a list of timeslots.
-I used the 24 hour format rather than AM and PM, at last for the sake of coding.
'''


class Time:
    '''Represents a half an hour of the day'''
    def __init__(self,time):
        self.slot = time
        self.Empty= True
        self.section=None
        self.activity=None
        self.location=None
        self.prof=None
        
    def isEmpty(self):
        ''' if its empty it will return True
        Null -> Boolean'''
        return self.Empty
    
    def fill(self, sec, act, loc, pro):
        '''Null -> Null'''
        self.secton = sec
        self.activity=act
        self.location=loc
        self.prof=pro
        self.Empty = False
        
        
    def __repr__(self):
        return str(self.slot)
        
    def __str__(self):
        e = str(self.isEmpty())
        s=str(self.slot)
        if self.section==None:
            return s+ " "+e
        else:
             return s+ " " + this.secton
        
          
t=8.00
Day= []
for eine in range(0, 28):
    s = eine = Time(t)
    Day.append(s)
    if (t+0.30) > int(t)+0.50:
        t = int(t)+1.00
    else:
        t = t+0.30
        
     
# to account for hour 22 or 10pm   
s=Time(22.00)
Day.append(s)


###Testing lists to test the class without the need for internet

Section1 = ['ELG2138 A00', 'ELG2138 A00', 'ELG2138 A03', 'ELG2138 A04', 'ELG2138 A01', 'ELG2138 A02', 'ELG2138 B00', 'ELG2138 B00', 'ELG2138 B03', 'ELG2138 B04', 'ELG2138 B01', 'ELG2138 B02']
Activity1=['LEC', 'LEC', 'DGD', 'DGD', 'LAB', 'LAB', 'LEC', 'LEC', 'DGD', 'DGD', 'LAB', 'LAB']
Time1=['11:30,13:00', '13:00,14:30', '14:30,16:00', '14:30,16:00', '14:30,17:30', '19:00,22:00', '10:00,11:30', '8:30,10:00', '16:00,17:30', '16:00,17:30', '16:00,19:00', '10:00,13:00']
Location1=['LPR 155', 'LPR 155', 'MRT 221', 'MNO C211', 'DEP DEPT', 'DEP DEPT', 'HGN 302', 'STE H0104', 'MRT 221', 'LMX 390', 'DEP DEPT', 'DEP DEPT']
Day1=['Wednesday', 'Monday', 'Thursday', 'Thursday', 'Wednesday', 'Tuesday', 'Thursday', 'Monday', 'Wednesday', 'Wednesday', 'Friday', 'Tuesday']
#--------------#-----------------------------------------------------
Section2=['MCG1100 A00', 'MCG1100 A01', 'MCG1100 A01', 'MCG1100 B00', 'MCG1100 B01', 'MCG1100 B01', 'MCG1100 C00', 'MCG1100 C01', 'MCG1100 C01', 'MCG1100 D00', 'MCG1100 D01', 'MCG1100 D01']
Activity2=['LEC', 'LAB', 'LAB', 'LEC', 'LAB', 'LAB', 'LEC', 'LAB', 'LAB', 'LEC', 'LAB', 'LAB']
Time2=['11:30,13:00', '8:00,10:00', '14:30,17:30', '17:30,19:00', '12:00,14:00', '19:00,22:00', '14:30,16:00', '18:30,20:30', '13:00,16:00', '17:30,19:00', '8:00,10:00', '19:00,22:00']
Location2=['STE C0136', 'DEP DEPT', 'DEP DEPT', 'STE C0136', 'DEP DEPT', 'DEP DEPT', 'STE C0136', 'DEP DEPT', 'DEP DEPT', 'STE C0136', 'DEP DEPT', 'DEP DEPT']
Day2=['Thursday', 'Friday', 'Friday', 'Thursday', 'Monday', 'Tuesday', 'Wednesday', 'Tuesday', 'Thursday', 'Monday', 'Thursday', 'Monday']
#_________________________________________________________________
Section3=['ITI1121 Z00', 'ITI1121 Z00', 'ITI1121 Z01', 'ITI1121 Z02', 'ITI1121 Z03']
Activity3=['LEC', 'LEC', 'LAB', 'LAB', 'LAB']
Time3=['11:30,13:00', '13:00,14:30', '11:30,14:30', '8:30,11:30', '8:30,11:30']
Location3=['MRT 218', 'MRT 218', 'STE 2060', 'STE 2060', 'STE 2060']
Day3=['Wednesday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
##_________________________________________________________________
#
#Section4=
#Activity4=
#Time4=
#Location4=
#------------------------------------------------------------------


class Table:
    def __init__(self):                                                                                  
        self.Sat = Day[:]                                                                            
        self.Sun = Day[:]                                                                            #
        self.Mon = Day[:]                                                                            #
        self.Tue = Day[:]                                                                            #
        self.Wed = Day[:]                                                                            #
        self.Thu = Day[:]                                                                            #
        self.Fri = Day[:]                                                                            #
        self.Week = [self.Sat, self.Sun, self.Mon, self.Tue, self.Wed, self.Thu, self.Fri]           #
                                                                                                     #
    def maker(self):
        '''Makes a table with the approperiate course sessions'''
        pass
    def print(self):
        '''Prints a Stirng representaion for the Table'''
        print("_______________________________________________________________________________________________________________________________________________________________________________________________________")
        print('{Tme:  | 8.0 | 8.3 | 9.0 | 9.3 | 10.0| 10.3| 11.0| 11.3| 12.0| 12.3| 13.0| 13.3| 14.0| 14.3| 15.0| 15.3| 16.0| 16.3| 17.0| 17.3| 18.0| 18.3| 19.0| 19.3| 20.0| 20.3| 21.0| 21.3| 22.0}')
        
        
        W=['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
        w=0
        for day in self.Week:
            Printed=[]
            Printed.append(W[w]+": ")
            w=w+1
            for slot in day:
                
                if slot.isOccupied()==True:
                    Printed.append("-F-")
                else: Printed.append("_E_")
            
            Printed=str(Printed)
            Printed=Printed.replace(","," |")
            Printed=Printed.replace("'","")
            print(Printed)
            
        print("_______________________________________________________________________________________________________________________________________________________________________________________________________")
        
        
def tableMaker():
    '''Genetates a list of all possible Tables'''
    pass
    
    
def insert(time, day, secInfo):
    '''Inserts the given time in the given day, if there is a conflict will return False, other wise will return True
    sec info is section, activity, location, prof in a list in that order'''
    Time = time.split(",")
    start = float(Time[0])
    end =   float(Time[1])
    if start/int(start) == 1:
        indexStart = int(2*start -16)
    else:
        indexStart = int(2*start -15)
        
    if end/int(end) == 1:
        end  = int(end)
        indexEnd = int(2*end -16)
    else:
        end  = int(end)
        indexEnd = int(2*end -15)
    for slot in range(indexStart, indexEnd+1):
        if day[slot].isEmpty():
            day[slot].fill(secInfo[0], secInfo[1],secInfo[2],secInfo[3],)
        else:
            print("Conflict in time "+ str(day[slot])[:5])
            return False
            
                    
            


            
            



                        
                        


        






    
        
        
        

    
    
    
    
    
    
