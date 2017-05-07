# Python Classes

# Running the demo
Run the command: python3 example.py

# class descriptions
Three python classes are contained in the classfiles directory:

1. CourseBuilder
This class takes a list of urls, or a list of files and returns rows or a json object of data which describes a course

2. TableBuilder
This class takes a json object from CourseBuilder and converts it to a list of all valid possible timttables

3. ViewBuilder
This class takes a list of all valid possible timetables and renders them to the console in a graphical manner

# Server

1. Run command: python3 server.py
2. The sever is now running at http://localhost:8000/
3. Visit this url for a demo request: localhost:8000/?courseURL=https%3A%2F%2Fweb30.uottawa.ca%2Fv3%2FSITS%2Ftimetable%2FCourse.aspx%3Fid%3D018039%26term%3D2175%26session%3DA   
