from http.server import BaseHTTPRequestHandler, HTTPServer
import json # convert json to string

from urllib.parse import urlencode, quote_plus, unquote
# example
# payload = {'courseURL':'https://web30.uottawa.ca/v3/SITS/timetable/Course.aspx?id=018039&term=2175&session=A'}
# result = urlencode(payload, quote_via=quote_plus)
# urllib.parse.unquote('id%3D184ff84d27c3613d&quality=medium')

from classfiles.CourseBuilder import CourseBuilder
from classfiles.TableBuilder import TableBuilder
from classfiles.ViewBuilder import ViewBuilder

#
# SET Variables
#
HOST = "localhost"
PORT = 8000

#
# Define class to handle server requests
#
class Handle_RH(BaseHTTPRequestHandler):
    def do_GET(self):

        #
        # prepare response headers
        #
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        #
        # get course page url from parameters
        #
        url = None
        if self.path.find("?") != -1:
            params = self.path.split("?")[1]
            paramName, urlEncoded = params.split("=")
            url = unquote(urlEncoded)

        if url != None:

            #
            # get the course data as a JSON object
            #
            course = CourseBuilder(url, "selenium") # TODO - change to urlopen in production
            data = course.getJSON()

            #
            # send response as JSON object
            #
            self.wfile.write(bytes( json.dumps(data) , "utf-8"))

        else:
            res = "No url parameters found. 'courseURL' should be the only parameter"
            self.wfile.write(bytes(res, "utf-8"))

#
# Start server listining on HOST and PORT
#
myServer = HTTPServer((HOST, PORT), Handle_RH)
print("http://" + HOST + ":" + str(PORT) + "/")
myServer.serve_forever()
