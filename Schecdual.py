import Initial as I
import itertools
import plotly as py
import plotly.figure_factory as ff


#Notes
# -if u will add the feature of getting course info by giving the course code rather than url, make sure to throw an error if the corses are in diffrent semsters


#path = "D:\chromedriver.exe"
path = r"D:\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe"
course1 = I.Course(path, "http://127.0.0.1:8000/html/ELG2138.html") #circuit theory
course2 = I.Course(path, "http://127.0.0.1:8000/html/MAT2322.html")#Calc 3
#course3 = I.Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=015025&term=2179&session=FS")#engineering mech
#course4 = I.Course(path, "")

#print(len(course1.tables))
#for i in course1.tables:
#    for j  in i:
#        j.print()
#        
        
def PossibleTables(one, two):
    '''takes 2 course objs then makes and outputs all possible tables with it, Cartisian product of the tables
    2 courses--->[Tables]'''
    tables_of_1 = one.tables
    tables_of_2 = two.tables
    output = []
    
    grouped_secs = [[x,y]for x in tables_of_1 for y in tables_of_2] #Groups secs based on cartisan product, eg: let course1 hv 2 sections and each section has 2 possible tbls, 
                                                                    #and course2 has 2 sections as well with each having 3 possible tbls. what will this do is create this list
                                                                    #[[[all C1 SecA Tbls], [all C2 SecA tbls]], [[all C1 SecA Tbls], [all C2 SecB tbls]]
#    print("\nthis is grouped secs")
#    print(grouped_secs)
            
    #grouped_tables refer to https://stackoverflow.com/questions/3034014/how-to-apply-itertools-product-to-elements-of-a-list-of-lists
    
    for i in range(len(grouped_secs)):
        
        grouped_tables = list(itertools.product(*grouped_secs[i])) #creates tuples of two for each 2 tbls combination, tables will be added with table mixer function like this
                                                     #[('table1A', 'table1C'), ('table1A', 'table2C'), ('table1A', 'table3C'), ('table2A', 'table1C'), ('table2A', 'table2C'), ('table2A', 'table3C')]
#        print("this is list of tuples")
#        print(grouped_tables)
        for tblTuple in grouped_tables:
            if I.isMixable(tblTuple[0], tblTuple[1]) == True:
                Onepossibleity =  I.tableMixer(tblTuple[0], tblTuple[1])
                output.append(Onepossibleity)
                
                
    return output


def formater(tableObj):
    '''takes a table object and creates a list in the format needed to export a Table via plotly'''
    t = tableObj
    w= ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
    times = ['8.0', '8.3', '9.0', '9.3', '10.0', '10.3', '11.0', '11.3', '12.0', '12.3', '13.0', '13.3', '14.0', '14.3', '15.0', '15.3', '16.0', '16.3', '17.0', '17.3', '18.0', '18.3', '19.0', '19.3', '20.0', '20.3', '21.0', '21.3', '22.0']
    
    dataMatrix = [("Days", w)
                  
                  
                 ]
    for i in range(len(times)):
        slotStr = times[i]
        timeList = []
        timeEntry = (slotStr,timeList)
        for day in t.Week:
            slot = day[i]
            if slot.location == None:
                timeList.append(" Free ")
            else:
                timeList.append(slot.activity+ '\n ' + slot.location+ '\n ' +slot.section)
        dataMatrix.append(timeEntry)
                
    return dataMatrix


def pandasFormater(t):
    '''formates the tables to a list of tuples so pandas dataframe can use it'''
    out = [("Times", ['8.0', '8.3', '9.0', '9.3', '10.0', '10.3', '11.0', '11.3', '12.0', '12.3', '13.0', '13.3', '14.0', '14.3', '15.0', '15.3', '16.0', '16.3', '17.0', '17.3', '18.0', '18.3', '19.0', '19.3', '20.0', '20.3', '21.0', '21.3', '22.0'])
          ]
    w= ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
    for i in range(len(t.Week)):
        day = t.Week[i]
        tmp = []
        for slot in day:
            if slot.location != None:              
                tmp.append(slot.activity+ ' ' + slot.location+ ' ' +slot.section)
            else:
                tmp.append("FreeTrack")
        x = (w[i],tmp)
        out.append(x)
    return out


def tableExport(L,fileName):
    '''takes a formated list L and makes a table with plotly. and takes a string as a name '''
    table = ff.create_table(L)
    py.offline.plot(table, filename=fileName )
    
    
        
            
            
    


ooo = PossibleTables(course1, course2)
a = ooo[0]
b = formater(a)

print(b)


print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLl\n")
tableExport(b, "Z")

#for i in range(len(ooo)):
#    table = ooo[i]
#    a = formater(table)
#    print (a)
#   


        
        

    
    