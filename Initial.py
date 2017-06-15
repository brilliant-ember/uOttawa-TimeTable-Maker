###WebScraper Selenium
from selenium import webdriver
import copy

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
        self.section = sec
        self.activity=act
        self.location=loc
        self.prof=pro
        self.Empty = False
    
    def clear(self):
        self.Empty= True
        self.section=None
        self.activity=None
        self.location=None
        self.prof=None
        
        
    def __repr__(self):
        return str(self.slot)
        
    def __str__(self):
        e = str(self.isEmpty())
        s=str(self.slot)
        if self.section==None:
            return s+ " "+e
        else:
             return s+ " " + self.section


#######dont forget to print an error mssg if the class instances r from diffrent semsters
    
def insert(time, day, secInfo):
    '''Inserts the given time in the given day, if there is a conflict will return False, other wise will return True
    sec info is section, activity, location, prof in a list in that order
    can either take a float time slot or a string of a starttime and endtime'''
    if type(time)==float:
        if time/int(time) == 1:
            index = int(2*time -16)
        else:
            index = int(2*time -15)
        tmp = day[:]
        if tmp[index].isEmpty():
            tmp[index].fill(secInfo[0], secInfo[1],secInfo[2],secInfo[3])
        else:
            return False
        day = tmp[:]
    else:
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
        tmp = day[:]
        for slot in range(indexStart, indexEnd):
            if tmp[slot].isEmpty():
                tmp[slot].fill(secInfo[0], secInfo[1],secInfo[2],secInfo[3])
            else:
                return False
        day = tmp[:]
            

        
def switcher(time, day, secInfo):
    '''Takes a time and day and course info, and switches the given time with the time of the given day changing occupiance
    assumes that the time given and the day given r in conflict'''
  
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
        #if they share the same code then thry're a group so remove them togather
    x = day[indexStart].section
    y = day[indexEnd].section
#    print("\nTHIS IS THE SWITCHER METHODE \n")
    
    for slot in day:
#        print("\nTHIS IS THE SWITCHER LOOP \n")
        if slot.section == None:
            pass
        
        elif slot.section[-3:] == x or slot.section[-3:] == y :
            slot.clear()
            slot.fill(fill(secInfo[0], secInfo[1],secInfo[2],secInfo[3]))
    return day
            

    
    
def DayMaker():
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
    return Day

Day = DayMaker()
class Table:
    def __init__(self):                                                                                  
        self.Sat = DayMaker()                                                                           
        self.Sun = DayMaker()                                                                           #
        self.Mon = DayMaker()                                                                           #
        self.Tue = DayMaker()                                                                           #
        self.Wed = DayMaker()                                                                           #
        self.Thu = DayMaker()                                                                           #
        self.Fri = DayMaker()                                                                           #
        self.Week = [self.Sat, self.Sun, self.Mon, self.Tue, self.Wed, self.Thu, self.Fri]           #
                                                                                                     #

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
                
                if slot.isEmpty()==False:
                    Printed.append("-F-")
                else: Printed.append("_E_")
            
            Printed=str(Printed)
            Printed=Printed.replace(","," |")
            Printed=Printed.replace("'","")
            print(Printed)
            
        print("_______________________________________________________________________________________________________________________________________________________________________________________________________")

    def inserter(self, time, Day, secInfo):
        '''Takes a day and a session info and inserts that into the time table'''
        if Day =="Saterday":
            day = self.Sat
        elif Day == "Sunday":
            day = self.Sun
        elif Day == "Monday":
            day = self.Mon
        elif Day == "Tuesday":
            day = self.Tue
        elif Day == "Wednesday":
            day = self.Wed
        elif Day == "Thursday":
            day = self.Thu
        elif Day == "Friday":
            day = self.Fri
        else:
            day = Day
            
        insert(time, day, secInfo)
        
    def __str__(self):
        pass

                    

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
        self.secActs=[]
        self.tables = []
        self.Lister()
        self.numberOfSections = self.SecNum()
        self.Seprate()
        self.tabler()
        
        
        
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
        browser = webdriver.PhantomJS(path)

        #browser = webdriver.Chrome(path)
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
        Act =[]
        
        
        for j in range(Nsec): #number of sections
            days_per_sec = []
            daytmp= []
            prof_persec = []
            proftmp=[]
            time_persec =[]
            timetmp=[]
            locpersec= []
            loctmp=[]
            act_persec=[]
            acttmp=[]
            act = Lact[D]
            tmp = []
            tmp2 = []
            for i in act_per_sec:
                if i == act:
                    daytmp.append(self.Day[D])
                    proftmp.append(self.Prof[D])
                    timetmp.append(self.Time[D])
                    loctmp.append(self.Location[D])
                    acttmp.append(self.Activity[D])
                    
                    tmp2.append(Lsec[D])
                    act = Lact[D]
                    D = D+1
                else:
                    tmp.append(tmp2)
                    days_per_sec.append(daytmp)
                    prof_persec.append(proftmp)
                    time_persec.append(timetmp)
                    locpersec.append(loctmp)
                    act_persec.append(acttmp)
                    proftmp=[]
                    timetmp=[]
                    loctmp=[]
                    acttmp=[]
                    
                    daytmp=[]
                    tmp2=[]
                    tmp2.append(Lsec[D])
                    daytmp.append(self.Day[D])
                    proftmp.append(self.Prof[D])
                    timetmp.append(self.Time[D])
                    loctmp.append(self.Location[D])
                    acttmp.append(self.Activity[D])
                    
                    act = Lact[D]
                    D = D+1
            tmp.append(tmp2)       
            Out.append(tmp)
            days_per_sec.append(daytmp)
            prof_persec.append(proftmp)
            time_persec.append(timetmp)
            locpersec.append(loctmp)
            act_persec.append(acttmp)
            DaysL.append(days_per_sec)
            ProfL.append(prof_persec)
            TimeL.append(time_persec)
            LocL.append(locpersec)
            Act.append(act_persec)
            
        self.seprateSections = Out[:]
        self.secDays=DaysL[:]
        
        self.secProfs = ProfL[:]
        self.secTimes = TimeL[:]
        self.secLocs = LocL[:]
        self.secActs = Act[:]
               
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


        
    def tabler(self):
        '''Creates a list of all possible tables for this course
        ###not actual output# [[['ELG2138 A00', 'ELG2138 A00'], ['ELG2138 A03', 'ELG2138 A04'], ['ELG2138 A01', 'ELG2138 A02']], [['ELG2138 B00', 'ELG2138 B00'], ['ELG2138 B03', 'ELG2138 B04'], ['ELG2138 B01', 'ELG2138 B02']]]'''
        #week = ["Saterday", "Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday"]
        Nsec = self.numberOfSections
        
        for i in range(Nsec):
            secs = self.seprateSections[i]
            days = self.secDays
            #print("\nLoop Number "+str(i))
            self.tables.append([])
            
            for j in range(len(secs)):
                act_set = secs[j]
                
                tmpcode = act_set[0][-3:]
                if len(act_set) == 1:
                    codeChecker = False
                else:
                     codeChecker=all(tmpcode == code [-3:] for code in act_set)
                if codeChecker:# the case where both sessions are mandatory , then I need to make a case where only one is mandtory
                    T = Table()
                    for x in range(len(act_set)):
                        session = act_set[x]
                        sessionDay = days[i][j][x]
                        sessionTime = self.secTimes[i][j][x]
                        sessionAct = self.secActs[i][j][x]
                        sessionLoc = self.secLocs[i][j][x]
                        sessionProf = self.secProfs[i][j][x]
                        secInfo= [session, sessionAct, sessionLoc, sessionProf]
                        
                        T.inserter(sessionTime, sessionDay, secInfo)
                    self.tables[i].append(T)

                else: #the case where only on is mandatory
                    if len(self.tables[i]) == 0:
                        T= Table()
                        self.tables[i].append(T)
                        #print("I got into the first IF  ")
                    
                    tmp = []
                    for x in range(len(act_set)):
                        session = act_set[x]
                        sessionDay = days[i][j][x]
                        sessionTime = self.secTimes[i][j][x]
                        sessionAct = self.secActs[i][j][x]
                        sessionLoc = self.secLocs[i][j][x]
                        sessionProf = self.secProfs[i][j][x]
                        
                        tblCopyList = copy.deepcopy(self.tables[i])
                        
                        for N in range(len(self.tables[i])):
                            #print("\nB4")
                            oneTbl = tblCopyList[N]
                            #oneTbl.print()
                            oneTbl.inserter(sessionTime, sessionDay, secInfo)
                            #print("\nAfter")
                            #oneTbl.print()
                            tmp.append(oneTbl)
                            
                    self.tables[i] = copy.deepcopy(tmp)

                    
                    
def tableMixer(tbl1, tbl2):
    '''Takes two tables and mixes them togather if it is possible, a similar (isMixable) function will return a boolean if they are not mixable'''
    output = Table()
    for i in range(len(tbl1.Week)):
        day1 = tbl1.Week[i]
        day2 = tbl2.Week[i]
        outDay = output.Week[i]
        for j in range(len(day1)):
            slot1 = day1[j]
            slot2 = day2[j]
            
#            print("HEYYYYYYYYYYYYYYY!")
#            print(slot2.slot)
#            print(slot1.slot)
#            
            if slot1.Empty == True and slot2.Empty == False:
                secInfo = [slot2.section, slot2.activity, slot2.location, slot2.prof]
                output.inserter(slot2.slot, outDay, secInfo)

            elif slot1.Empty == False and slot2.Empty == True:
                secInfo = [slot1.section, slot1.activity, slot1.location, slot1.prof]
                output.inserter(slot1.slot, outDay, secInfo)
                
    return output
    
def isMixable(tbl1, tbl2):
    '''tells if the 2 tables can be mixed, returns True if they can and falses otherwise'''
    for i in range(len(tbl1.Week)):
        day1 = tbl1.Week[i]
        day2 = tbl2.Week[i]
        for j in range(len(day1)):
            slot1 = day1[j]
            slot2 = day2[j]
            if slot1.Empty == False and slot2.Empty == False:
                return False
    return True
               
#                
#path = "D:\chromedriver.exe"
##
##
##course1 = Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=011209&term=2179&session=FS")
#print("____________Finalllll  ________________")
#course1 = Course(path, "http://127.0.0.1:8000/html/ELG2138.html")
#
#print(len(course1.tables))
#for i in course1.tables:
#    for j  in i:
#        j.print()
#        

####################My approch to the problem -----------------------------------------------------------------------------------------------------------------
'''
Each day has 29 timeslots, each represents half an hour. each timeslot will be an object (class) and it will have a methode isOccupied which tells if that time slot has already been taken by returning a boolean.
-The class will also have a method which fills that time table with a course, and will change the obj boolean once the slot is full.
-The toString methode will print the time slot and the occuping course; maybe also section, and if the slot is empty it would print the time of the slot and empty
Eg: "9:00, ITI110 Z00" or "8:30, Empty".
-Each day is a list of timeslots.
-I used the 24 hour format rather than AM and PM, at last for the sake of coding.
'''
##################-------------------------------------------------------------------------------------------------------------------------------------------------


                        
                        


        






    
        
        
        

    
    
    
    
    
    