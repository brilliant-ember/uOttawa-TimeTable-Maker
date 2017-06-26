import Initial as I
import itertools
import os
import tableHtml as T

#Notes
# -if u will add the feature of getting course info by giving the course code rather than url, make sure to throw an error if the corses are in diffrent semsters


#path = "D:\chromedriver.exe"
path = r"D:\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe"
#course1 = I.Course(path, "http://127.0.0.1:8000/html/ELG2138.html") #circuit theory
#course2 = I.Course(path, "http://127.0.0.1:8000/html/MAT2322.html")#Calc 3
#course3 = I.Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=015025&term=2179&session=FS")#engineering mech
#course4 = I.Course(path, "")
     
        
def PossibleTables(one, two):
    '''takes 2 course objs then makes and outputs all possible tables with it, Cartisian product of the tables
    2 courses--->[Tables]'''
    tables_of_1 = one.tables
    tables_of_2 = two.tables
    output = []
    
    grouped_secs = [[x,y]for x in tables_of_1 for y in tables_of_2] #Groups secs based on cartisan product, eg: let course1 hv 2 sections and each section has 2 possible                                                                      tbls, 
                                                                    #and course2 has 2 sections as well with each having 3 possible tbls. what will this do is create this list
                                                                    #[[[all C1 SecA Tbls], [all C2 SecA tbls]], [[all C1 SecA Tbls], [all C2 SecB tbls]]

            
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





def PossibleTablesVer2(tables_of_1, tables_of_2):
    '''takes 2 Lists of table obj then makes and outputs all possible tables with it, Cartisian product of the tables
    2 courses--->[Tables]'''

    output = []
    
    grouped_secs = [[x,y]for x in tables_of_1 for y in tables_of_2] #Groups secs based on cartisan product, eg: let course1 hv 2 sections and each section has 2 possible                                                                      tbls, 
                                                                    #and course2 has 2 sections as well with each having 3 possible tbls. what will this do is create this list
                                                                    #[[[all C1 SecA Tbls], [all C2 SecA tbls]], [[all C1 SecA Tbls], [all C2 SecB tbls]]

            
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



def MultiPossibleTables(*args):
    '''This method takes a list of urls and makes a list of courses out of it, then takes these courses and makes all possible tables of them and spits that as a list of tables'''
    #the *args is a tuple that includes only one list, which is the list of links
    links = args[0]
    courses = []
    print(str(links) + "Im Multi")
#    for i in links:
#        print("inital")
#        courses.append(I.Course(path,i))
#    
#    print(len(courses))
#        
                       
                       

def style(I):
    return I

def formater(tableObj):
    '''takes a table object and creates a list in the format needed to export a Table'''
    t = tableObj
    w= ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
    dataMatrix = []
    for i in range(len(w)):
        day = t.Week[i]
        dayEntry = [w[i]]
        for slot in day:
            if slot.location != None:              
                dayEntry.append(slot.activity+ ' ' + slot.location+ ' ' +slot.section)
            else:
                dayEntry.append(None)
        dataMatrix.append(dayEntry)
    
    return dataMatrix

#    
#
#ooo = PossibleTables(course1, course2)
#for i in range(len(ooo)):
##    print(i)
#    print("\n \n \n")
    #x.print()
  #  x = ooo[i]
   # a = formater(x)
    #print(a)
  #  T.UseThis(a, str(i))
      
        
        
        


                    



        

    
    