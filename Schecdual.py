import Initial as I
#Notes
# -if u will add the feature of getting course info by giving the course code rather than url, make sure to throw an error if the corses are in diffrent semsters



path = "D:\chromedriver.exe"

course1 = I.Course(path, "https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=011209&term=2179&session=FS")

for i in course1.tables:
    for j  in i:
        j.print()