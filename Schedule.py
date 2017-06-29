import Initial as I
import itertools
import os
import tableHtml as T

#Notes
# -if u will add the feature of getting course info by giving the course code rather than url, make sure to throw an error if the corses are in diffrent semsters


#path = "D:\chromedriver.exe"
path = r"D:\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe"

def PossibleTables(one, two):
    '''takes 2 course objs then makes and outputs all possible tables with it, Cartisian product of the tables
    2 courses--->[Tables]'''
    tables_of_1 = one.tables
    tables_of_2 = two.tables
    output = []
    
    grouped_secs = [[x,y]for x in tables_of_1 for y in tables_of_2] #Groups secs based on cartisan product, eg: let course1 hv 2 sections and each section has 2 possible                                                                      tbls, 
                                                                    #and course2 has 2 sections as well with each having 3 possible tbls. what will this do is create this list
                                                                    #[[[all C1 SecA Tbls], [all C2 SecA tbls]], [[all C1 SecA Tbls], [all C2 SecB tbls]]
                                                                    #aka all possible section combinations
            
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


def two_possible_tables(tables_of_1, tables_of_2):
    '''takes 2 doubleLists of tables(each section in a sublist), then makes and outputs all possible tables with it based on Cartisian product of the tables aka all possible combinations
    2 DLists--->[Tables]'''

    output = []
    
    grouped_secs = [[x,y]for x in tables_of_1 for y in tables_of_2] #Groups secs based on cartisan product, eg: let course1 hv 2 sections and each section has 2 possible                                                                      tbls, 
                                                                    #and course2 has 2 sections as well with each having 3 possible tbls. what will this do is create this list
                                                                    #[[[all C1 SecA Tbls], [all C2 SecA tbls]], [[all C1 SecA Tbls], [all C2 SecB tbls]]
                                                                    #aka all possible section combinations

            
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

def ThreeTbls(t1, t2, t3):
    Out=[]
    grouped_secs = list([x,y,z]for x in t1 for y in t2 for z in t3)
    for i in range(len(grouped_secs)):
        grouped_tables = list(itertools.product(*grouped_secs[i]))
        for Atuple in grouped_tables:
            bool1 = I.isMixable(Atuple[0],Atuple[1])
            bool2=I.isMixable(Atuple[0],Atuple[2])
            bool3=I.isMixable(Atuple[1],Atuple[2])

            if bool1 and bool2 and bool3:
                tbl1 = I.tableMixer(Atuple[0], Atuple[1])
                oneP = I.tableMixer(tbl1, Atuple[2])
                Out.append(oneP)
    return Out
        
def table_singular(L):
    '''takes the double list from I.course.tables and makes that into a single list '''
    out = []
    for sec in L :
        for tbl in sec:
            out.append(tbl)
    return out


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

def MultiPossibleTables(tbls):
    '''This method takes a list of urls and makes a list of courses out of it, then takes these courses and makes all possible tables of them and spits that as a list of tables'''
    Out = [] 
    if len(tbls) == 1:
        Out.extend(table_singular(tbls[0]))
        
    elif len(tbls) ==2 :#we have an even number of tables
        Out.extend(two_possible_tables(tbls[0], tbls[1]))
        
    elif len(tbls) == 3:
        Out.extend(ThreeTbls(tbls[0], tbls[1], tbls[2]))
        
    elif len(tbls) == 4:
        t1 = two_possible_tables(tbls[0], tbls[1])
        t2 = two_possible_tables(tbls[2], tbls[3])
        grouped_tables = [(x,y) for x in t1 for y in t2]
        for tblTuple in grouped_tables:
            if I.isMixable(tblTuple[0], tblTuple[1]) == True:
                Onepossibleity =  I.tableMixer(tblTuple[0], tblTuple[1])
                Out.append(Onepossibleity)

    htmlMaker(Out)
            
                
def htmlMaker(Tlist):
    for i in range(len(Tlist)):
        tbl = Tlist[i]
        a = formater(tbl)
        T.UseThis(a, str(i))

#    
#
#ooo = PossibleTables(course1, course2)
#for i in range(len(ooo)):
##    print(i)
#
#    x = ooo[i]
#    a = formater(x)
#    T.UseThis(a, str(i))
#      
                
        
course1 = I.Course(path, "http://127.0.0.1:8000/html/ELG2138.html").tables #circuit theory
course2 = I.Course(path, "http://127.0.0.1:8000/html/MAT2322.html").tables#Calc 3
course3 = I.Course(path, "http://127.0.0.1:8000/html/ITI1121.html").tables#iti1121
#course4 = I.Course(path, "")
       
MultiPossibleTables([course1, course2,course3])


                     



        

    
    