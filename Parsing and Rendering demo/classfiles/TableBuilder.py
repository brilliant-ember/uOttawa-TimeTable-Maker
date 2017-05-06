import json
import math

class TableBuilder:

    def __init__(self, courseData = None):
        self.data = None # course data object
        self.tableList = [] # list possible schedules

        if courseData != None:
            self.data = courseData

    def addCourseData(self, courseData):
        self.data = courseData

    def getTimeTables(self):
        # returns a list of format
        # [ timetable, timetable, ...]
        #
        # each timetable is a list of format
        # [[period, metadata], [period, metadata], ...]

        #
        # lookup for day offset
        #
        offset = {}
        offset["mon"] = 0
        offset["tue"] = 9
        offset["wed"] = 18
        offset["thu"] = 27
        offset["fri"] = 36

        #
        # a list n courses long, each element is all possible course tables
        #
        course_tables = []
        for i in range(len(self.data)):
            course_tables.append([])

        index = 0
        for courseName in self.data: # for each course
            courseObj = self.data[courseName]

            for section in courseObj: # for each section

                #
                # collect LEC, LAB, DGD, and TUT
                #

                #
                # LEC
                #
                lec_list = []
                for lec in courseObj[section]["LEC"]:
                    for period in lec["periods"]:

                        metadata = {
                            'courseName': courseName,
                            'section': section,
                            'period': period,
                            'day': lec["day"],
                            'starttime': lec['starttime'],
                            'endtime': lec['endtime'],
                            'location': lec['location'],
                            'prof': lec['prof'],
                            'type': "LEC",
                            'id': None # ex. lab/tut/dgd identifier
                        }

                        lec_list.append( [period + offset[lec["day"]], metadata] )

                #
                # LAB
                #
                lab_list = []
                if "LAB" in courseObj[section]:
                    for lab in courseObj[section]["LAB"]:
                        labNumber = lab
                        lab = courseObj[section]["LAB"][lab]

                        temp = []
                        for period in lab["periods"]:

                            metadata = {
                                'courseName': courseName,
                                'section': section,
                                'period': period,
                                'day': lab["day"],
                                'starttime': lab['starttime'],
                                'endtime': lab['endtime'],
                                'location': lab['location'],
                                'prof': lab['prof'],
                                'type': "LAB",
                                'id': labNumber # ex. lab/tut/dgd identifier
                            }

                            temp.append( [period + offset[lab["day"]], metadata] )
                        lab_list.append(temp)




                #
                # DGD
                #
                dgd_list = []
                if "DGD" in courseObj[section]:
                    for dgd in courseObj[section]["DGD"]:
                        dgdNumber = dgd
                        dgd = courseObj[section]["DGD"][dgd]

                        temp = []
                        for period in dgd["periods"]:

                            metadata = {
                                'courseName': courseName,
                                'section': section,
                                'period': period,
                                'day': dgd["day"],
                                'starttime': dgd['starttime'],
                                'endtime': dgd['endtime'],
                                'location': dgd['location'],
                                'prof': dgd['prof'],
                                'type': "DGD",
                                'id': dgdNumber # ex. lab/tut/dgd identifier
                            }

                            temp.append( [period + offset[dgd["day"]], metadata] )
                        dgd_list.append(temp)


                #
                # TUT
                #
                tut_list = []
                if "TUT" in courseObj[section]:
                    for tut in courseObj[section]["TUT"]:
                        tutNumber = tut
                        tut = courseObj[section]["TUT"][tut]

                        temp = []
                        for period in tut["periods"]:

                            metadata = {
                                'courseName': courseName,
                                'section': section,
                                'period': period,
                                'day': tut["day"],
                                'starttime': tut['starttime'],
                                'endtime': tut['endtime'],
                                'location': tut['location'],
                                'prof': tut['prof'],
                                'type': "TUT",
                                'id': tutNumber # ex. lab/tut/dgd identifier
                            }

                            temp.append( [period + offset[tut["day"]], metadata] )
                        tut_list.append(temp)

                #
                # ensure all arrays have at least one element
                #
                if(len(lab_list) == 0): lab_list.append([])
                if(len(dgd_list) == 0): dgd_list.append([])
                if(len(tut_list) == 0): tut_list.append([])

                #
                # make all possible combinations of LEC + other for this section
                #
                combos = []
                for a in lab_list:
                    for b in dgd_list:
                        for c in tut_list:
                            combos.append( a + b + c + lec_list )

                #
                # save this batch of possible course timetables
                #
                course_tables[index] += combos
            index += 1

        #
        # begin at index [0, 0, 0, ...]
        #
        index = [0 for x in range(len(self.data))]

        #
        # increments index list by one
        #
        def next(index):
            index = index[:]
            for i in range(len(index)-1, -1, -1):

                # can't increment further
                if( i == 0 and index[i] == len(course_tables[i])-1 ):
                    return False

                # reached max for current index
                elif( index[i] == len(course_tables[i])-1 ):
                    index[i] = 0

                # increment and return result
                else:
                    index[i] += 1
                    return index
        #
        # add all possible timetables to list
        #
        possible = []
        while( index != False ):
            temp = []

            for i in range(len(index)):
                temp += course_tables[i][ index[i] ]

            possible.append( temp[:] )
            index = next(index)

        #
        # return only valid timetables
        #
        for p in range(len(possible)):
            possible[p] = sorted(possible[p], key=lambda x: x[0])

        valid_tables = []
        for p in possible:
            for i in range(len(p)-1):
                if p[i][0] == p[i+1][0]:
                    break # duplicate period found
            valid_tables.append(p)

        return valid_tables

# end
