from urllib.request import urlopen
from bs4 import BeautifulSoup

#
# How to use this class
#######################
#
# Create an instance of the class, and pass it a single url or
# a list of urls as strings.
#
# builder = CourseBuilder( url )
# builder = CourseBuilder( urlList )
#
# Obtain a list of one or more json objects representing
# the courses you have requested by calling the
# getCourseData method
#
# builder.getRows() -> returns rows of course data
# builder.getJSON() -> returns json object of course data
#
#
class CourseBuilder:

    def __init__(self, url=None):
        if( type(url) is str ):
            self.urls = [url]

        elif( type(url) is list ):
            self.urls = url

        else:
            print("Usage: builder = CourseBuilder(url)\nUsage: builder = CourseBuilder([url1, url2, ...])")

    def getJSON(self):
        course_json = {} # for each course build json object
        rows = self.getRows()

        #
        # JSON Data Format
        #
        #   courseID (ABC1234)
        #       sectionLetter ('000' or A, B, C)
        #           activity
        #               sectionNumber ('000' or LAB number)
        #               starttime (just the time of day)
        #               endtime (just the time of day)
        #               day (three letter lowercase abbr)
        #               periods (array of periods)
        #               location
        #               prof

        #
        # lookup arrays
        #
        periodFromStart = {
            '8:30:00':1,
            '10:00:00':2,
            '11:30:00':3,
            '13:00:00':4,
            '14:30:00':5,
            '16:00:00':6,
            '17:30:00':7,
            '19:00:00':8,
            '20:30:00':9
        }
        periodFromEnd = {
            '10:00:00':1,
            '11:30:00':2,
            '13:00:00':3,
            '14:30:00':4,
            '16:00:00':5,
            '17:30:00':6,
            '19:00:00':7,
            '20:30:00':8,
            '22:00:00':9
        }

        for item in rows:
            # example:
            # ['PDP1828 WL00',
            # 'January 10 - April 07',
            # 'LEC',
            # 'Tuesday 18:00 - 21:00',
            # 'DEP DEPT',
            # 'Claudine Rolland  Gauthier']
            #

            # ignore title row
            if item[0] == "CourseCode":
                continue

            #
            # get course, section, and section_number
            #
            code, term = item[0], item[1]

            code = code.split(' ')
            if len(code) == 2:
                course, sectcode = code
            else: # for case of ESL 123 A00
                course, sectcode = (code[0] + code[1], code[2])

            section = sectcode # set defaults
            section_number = '000'
            if sectcode != '000' and sectcode.find('0') != -1:
                section = sectcode[:sectcode.find('0')]
                section_number = sectcode[sectcode.find('0'):]

            #
            # get term
            #
            term = term.split(' ')[0]
            if term == 'January':
                term = 'winter'

            elif term == 'September':
                term = 'fall'

            else: # summer term
                term = 'summer'

            #
            # get activity
            #
            activity = item[2]

            #
            # get day, starttime, endtime, and periods
            #
            date_info = item[3].split(' ')
            if(date_info[0][0] != 'N'): # for 'Not available at this time'

                starttime = date_info[1] + ':00' # 00 for seconds
                endtime = date_info[3] + ':00' # 00 for seconds

                day = date_info[0][0:3].lower()

                #
                # build a list of the periods that the class takes up ex. [7, 8, 9]
                #
                periods = []
                try:
                    for i in range(periodFromStart[starttime], periodFromEnd[endtime]+1):
                        periods.append(i)

                except: # because some online courses don't fit into regular periods
                    starttime = 0
                    endtime = 0
                    day = 'null'
                    periods = []

                #
                # format dates for query
                #
                #if len(periods) > 0:
                #    today = date.today().strftime('%Y-%m-%d')
                #    starttime = today + ' ' + starttime
                #    endtime = today + ' ' + endtime

            else: # period time is not available
                starttime = 0
                endtime = 0
                day = 'null'
                periods = []

            #
            # get location and prof
            #
            location = item[4]
            prof = item[5]

            #
            # variables now available
            # term, course, section, section_number, activity,
            # day, starttime, endtime, periods, location, prof

            #
            # ensure json object is built
            #
            if not(course in course_json):
                course_json[course] = {}

            if not(section in course_json[course]):
                course_json[course][section] = {}

            if not(activity in course_json[course][section]):

                if activity == 'LEC': # NOTE LEC in list, all else in dict
                    course_json[course][section][activity] = []
                else:
                    course_json[course][section][activity] = {}

            # get shorter ref
            obj = course_json[course][section][activity]

            #
            # create temp object to place in course_json
            #
            temp_object = {}
            temp_object['day'] = day
            temp_object['starttime'] = starttime
            temp_object['endtime'] = endtime
            temp_object['periods'] = periods
            temp_object['location'] = location.replace("'", "")
            temp_object['prof'] = prof.replace("'", "") # remove simgle quote from names

            if activity == 'LEC': # section_number will be '000', as LEC are not numbered
                obj.append(temp_object)

            else: # NOTE - assume section_number is unique
                obj[section_number] = temp_object

        # dict of objects {courseName: courseData, courseName: courseData, ...}
        return course_json

    def getRows(self):

        rows = []
        rows.append(['CourseCode', 'StartEndDate', 'ActivityType', 'DateTime', 'Location', 'Prof']) # title row

        for url in self.urls:

            try:
                html = urlopen(url).read().decode("utf-8")

            except:
                print("Could not find url: " + str(url))
                continue

            #
            # parse html with BeautifulSoup
            #
            soup = BeautifulSoup(html, 'html.parser')

            #
            # Get all section divs
            #
            sections = soup.findAll("div", { "class" : "schedule" })

            #
            # get LEC/LAB/TUT info from each section
            #
            data = []
            for section in sections: # course page may have multiple sections

                class_rows = section.findAll("div")

                for classes in class_rows: # classes in section table come in blocks of rows

                    class_rh = classes.find_all("tr")

                    for c in class_rh: # for each row in this row block or LEC/LAB/TUT, etc...

                        #
                        # get a list containing the data for each LEC/LAB/TUT
                        #
                        data_list = [x.text for x in c.find_all("td")]

                        # take only 5-column table rows
                        if len(data_list) == 5:

                            #
                            # seperate course name and date range
                            #
                            try:
                                courseName, startEndDate = data_list[0].split("(")
                                startEndDate = startEndDate.split(")")[0]
                                data_list = [courseName] + [startEndDate] + data_list[1:]
                            except:
                                print("Could not parse course name from string: " + str(data_list[0]))
                                continue

                            #
                            # write each course row to output file
                            #
                            rows.append( data_list )

        # element format -> ['CourseCode', 'StartEndDate', 'ActivityType', 'DateTime', 'Location', 'Prof']
        return rows

# testing
# builder = CourseBuilder("https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=018039&term=2175&session=A")

# print( builder.getRows() )
# print( builder.getJSON() )

# end
