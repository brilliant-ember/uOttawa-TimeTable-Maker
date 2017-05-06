import math

class ViewBuilder:
    def __init__(self, valid_tables):
        self.valid_tables = valid_tables

    def showTables(self):
        #
        # timeslot states (hollow or filled square)
        #
        empty = "\u25A1"
        full = "\u25A0"

        #
        # format list into 9x5 table
        #
        def format_table(lst):
            table = [ [empty]*5 for x in range(9) ]

            for i in lst:
                day = math.floor( (i[0]-1)/9 )
                period = ((i[0] - 1) % 9)
                table[period][day] = [full, i[1]]

            return table

        #
        # draw table to terminal
        #
        def draw_table(table):
            # precondition: table is a 9x5 matrix with unicode strings
            for row in table:
                for cell in row:
                    print(cell[0], end="")
                print("")

        #
        # returns True for given table when
        # table should be rendered
        #
        def condition(table):

            # Example condition requiring there to be class
            # on tues and wed from 7 - 10pm
            one = table[7][1][0] == full and table[7][2][0] == full and table[8][1][0] == full and table[8][2][0] == full

            return True # condition always true, so all timetables will be rendered

        #
        # draw timetables
        #
        count = 0
        for v in self.valid_tables:
            vf = format_table(v)
            if condition(vf):
                print("")
                count += 1
                draw_table(vf)
                print("")
        print("Rendered " + str(count) + " tables")
        print("Considered LEC, LAB, DGD, and TUT for each course")
