from classfiles.CourseBuilder import CourseBuilder
from classfiles.TableBuilder import TableBuilder
from classfiles.ViewBuilder import ViewBuilder

#
# for testing purposes we pass a list of files
# (instead of "files" we could pass "selenium" or "urlopen" )
#
course = CourseBuilder(["demodata/ITI1100.txt", "demodata/ITI1121.txt", "demodata/MAT1348.txt", "demodata/CSI2911.txt", "demodata/CEG3185.txt"], "files")

#
# we could also pass a list of urls like this
#
#course = CourseBuilder([url1, url2, url3, ...], "selenium")

#
# get the course data as a JSON object
#
data = course.getJSON()

#
# get TableBuilder to make all possible schedules
# as a list of timetables, where each timetable is a list
# of periods
#
table = TableBuilder(data)
tables = table.getTimeTables()

#
# format and print tables
#
view = ViewBuilder(tables)
view.showTables()
