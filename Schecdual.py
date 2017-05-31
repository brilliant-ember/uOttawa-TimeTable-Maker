import Initial as I
import itertools
#Notes
# -if u will add the feature of getting course info by giving the course code rather than url, make sure to throw an error if the corses are in diffrent semsters


#path = "D:\chromedriver.exe"
path = r"D:\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe"
course1 = I.Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=011209&term=2179&session=FS") #circuit theory
#course2 = I.Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=019810&term=2179&session=FS")#Calc 3
#course3 = I.Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=015025&term=2179&session=FS")#engineering mech
#course4 = I.Course(path, "")

print(len(course1.tables))
for i in course1.tables:
    for j  in i:
        j.print()
        
        
def PossibleTables(one, two):
    '''takes 2 course objs then makes and outputs all possible tables with it, Cartisian product of the tables
    2 courses--->[Tables]'''
    tables_of_1 = one.tables
    tables_of_2 = two.tables
    output = []
    
    grouped_secs = [[x,y]for x in tables_of_1 for y in tables_of_2] #Groups secs based on cartisan product, eg: let course1 hv 2 sections and each section has 2 possible tbls, 
                                                                    #and course2 has 2 sections as well with each having 3 possible tbls. what will this do is create this list
                                                                    #[[[all C1 SecA Tbls], [all C2 SecA tbls]], [[all C1 SecA Tbls], [all C2 SecB tbls]]
    print("\nthis is grouped secs")
    print(grouped_secs)
            
    #grouped_tables refer to https://stackoverflow.com/questions/3034014/how-to-apply-itertools-product-to-elements-of-a-list-of-lists
    
    for i in range(len(grouped_secs)):
        
        grouped_tables = list(itertools.product(*grouped_secs[i])) #creates tuples of two for each 2 tbls combination, tables will be added with table mixer function like this
                                                     #[('table1A', 'table1C'), ('table1A', 'table2C'), ('table1A', 'table3C'), ('table2A', 'table1C'), ('table2A', 'table2C'), ('table2A', 'table3C')]
        print("this is list of tuples")
        print(grouped_tables)
        for tblTuple in grouped_tables:
            if I.isMixable(tblTuple[0], tblTuple[1]) == True:
                Onepossibleity =  I.tableMixer(tblTuple[0], tblTuple[1])
                output.append(Onepossibleity)
                
                
    return output


#ooo = PossibleTables(course1, course2)
#print(len(ooo))
#for tbl in ooo:
#    tbl.print()
        
        
        

    
    