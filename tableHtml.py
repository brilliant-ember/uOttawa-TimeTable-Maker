time=['8.0', '8.3', '9.0', '9.3', '10.0', '10.3', '11.0', '11.3', '12.0', '12.3', '13.0', '13.3', '14.0', '14.3', '15.0', '15.3', '16.0', '16.3', '17.0', '17.3', '18.0', '18.3', '19.0', '19.3', '20.0', '20.3', '21.0', '21.3', '22.0']
course_color=["#eafffd","#c8e5fd","#e3c8fd","#fdc8f3","#faf1ae","#97e33f","#3fe3ca"]
scheme1=["snow","#f4f1d1","snow","#f5eb67","#f4e9e9","#effad2","snow","#ad9981","#ad9981"]
scheme2=["#ffffff","#e5e7f8","snow","#cfd0cc","grey","#e3b7ed","#f4e9e9","#e5e7f8","snow"]
schemeBlue=["snow","#859ddd","","#859ddd"]
schemeBlack=[]
schemePink=[]

def HTML_lister(tbl):
	'''Exports a list oflists with all the divs and css data is this format:[[][divTagStr, dayOfTheWeek, startTime, numberOfSlots, Css class key made of 'session CourseCode DayandTimeOfsession' ][]]'''
	divList = []
	for day in tbl:
		session = []#each day starts with a new session
		dayOftheWeek=day[0]
		for i in range(1, len(day)):
			slot = day[i]

			if slot != None:
				if len(session) == 0:
					slotStr = time[i-1]
					session.append(slotStr)
					sessionName = slot[-11:]
					session.append(sessionName)
					session.append(slot[:-11])
					session.append("30Min")
				elif slot[-3:] != session[1][-3:]:#div creation here, then empty the session list
					divEx= ['''<div class="session  '''+ dayOftheWeek+slotStr.replace(".","Z")+''' " '''+'''
	        		<h3>'''+
	        		session[1]+" "+session[2]+ " "+session[0].replace(".",":")+"0"+'''
	        		</h3>
	    			</div>
	    			''', dayOftheWeek,session[0],session.count("30Min")," "+"."+dayOftheWeek+slotStr.replace(".","Z")]
					divList.append(divEx)
					session= []

					slotStr = time[i-1]
					session.append(slotStr)
					sessionName = slot[-11:]
					session.append(sessionName)
					session.append(slot[:-11])
					session.append("30Min")
				else:
					session.append("30Min")
			elif slot == None and len(session) != 0:

				divEx= ['''<div class="session  '''+ dayOftheWeek+slotStr.replace(".","Z")+''' " '''+'''
	        		<h3>'''+
	        		session[1]+" "+session[2]+ " "+session[0].replace(".",":")+"0"+'''
	        		</h3>
	    			</div>
	    			''', dayOftheWeek,session[0],session.count("30Min")," "+"."+dayOftheWeek+slotStr.replace(".","Z")]
				divList.append(divEx)
				session = []

		if len(session) != 0:
			divEx= ['''<div class="session  '''+ dayOftheWeek+slotStr.replace(".","Z")+''' " '''+'''
    		<h3>'''+
    		session[1]+" "+session[2]+ " "+session[0].replace(".",":")+"0"+'''
    		</h3>
			</div>
			''', dayOftheWeek,session[0],session.count("30Min")," "+"."+dayOftheWeek+slotStr.replace(".","Z")]
			divList.append(divEx)
			

	return divList

def coordinate(day, StartTime, number_of_slots):
	'''takes day and StartTime and returns the X and Y coordinates as well the hight of the the div in the format of a list of numbers [x, y, hight]'''
	w = ['Mon','Tue','Wed','Thu','Fri','Say','Sun']
	yList = [55, 90, 125, 160, 195, 230, 265, 300, 335, 370, 405, 440, 475, 510, 545, 580, 615, 650, 685, 720, 755, 790, 825, 860, 895, 930, 965, 1000, 1035]
	x = w.index(day)
	x = (x*163) + 66
	y = time.index(StartTime)
	y = yList[y]
	h =  number_of_slots - 2
	h = 0.3+(0.6*h)
	return [str(x), str(y), str(h)]

if True:
	selected = scheme1
def UseThis(tbl):
	htmlCss = '''
	<html>
	    <head>
	        <style>
	table{
	    background-color: '''+selected[0]+''';
	    width: 1000;    
	}
	#day{
	    background-color: '''+ selected[1]+''';
	    border-bottom: 10px double '''+selected[2]+''';   
	}
	.tile{
	    width:1000;
	    margin:  15px;
	 
	    border: 3px solid #cfd0cc;
	    border-bottom:3px double '''+ selected[3]+'''
	}
	td{
	    border-radius: 3px;    
	    text-align: center;
	    width: 150px;
	    border: 3px solid '''+ selected[4]+''';
	    margin: 2px;
	    padding: 4px;
	    background-color: ''' +selected[5]+''';
	    
	}
	.time{
	     background-color: '''+ selected[6]+''';
	     border-right: 10px double '''+ selected[7]+''';
	     width: 15px;
	     
	    
	}
	#sat{
	    width:10px;
	    background-color: #ad9981;
	    width: 10px;
	    
	}
	#sun{
	    width:10px;
	        background-color: #ad9981;

	}
	.session{
	    
	    border-radius: 10px;    
	    width: 144;
	    position: absolute;
	    border: 5px solid green;
	    font-family: Century Gothic, sans-serif;
	    text-align: center;
	}'''


	htmlTbl=	'''	</style>
	    
	        <title>
	            I'm a cute table <3
	        </title>
	    </head>
	        
	    <body>
	        <div class="tile">
	        <table>
	            <thead>
	                <tr>
	                      <th class="time">Times</th>
	                        <th id="day">Monday</th>
	                        <th id="day">Tuesday</th>
	                        <th id="day">Wednessday</th>
	                        <th id="day">Thursday</th>
	                        <th id="day">Friday</th>
	                        <th id="day">Saterday</th>
	                        <th id="day">Sunday</th>
	                </tr>
	            </thead>
	        <tbody>
	            <tr>
	                
	                <td class= "time">8:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
	                
	            </tr>
	            <tr>
	                
	                <td class= "time">8:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
	                
	            </tr>
	            
	            <tr>
	    <td class= "time">9:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">9:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">10:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">10:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">11:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">11:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">12:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">12:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">13:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">13:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">14:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">14:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">15:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">15:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">16:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">16:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">17:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">17:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">18:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">18:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">19:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">19:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">20:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">20:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">21:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">21:30</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>
		<tr>
		    <td class= "time">22:00</td><td></td><td></td><td></td><td></td><td></td><td id="sat"></td><td id="sun"></td>
		</tr>

		      
	'''

	htmlEnd = "</html>"

	divList = HTML_lister(tbl)

	color = []
	for div in divList:
		#[x, y, hight]
		#[divTagStr, dayOfTheWeek, startTime, numberOfSlots, Css class key made of 'session CourseCode DayandTimeOfsession' ]
		forTbl = "  " + div[0]
		
		postion = coordinate(div[1], div[2], div[3])
		if len(color) == 0 or div[4][0:16] not in color:
			color.append(div[4][0:16])

		forCss = div[4]+"""{ """+ "line-height: """+postion[2]+"""; 
					background-color: """ + course_color[color.index(div[4][0:16])] + """; 
					top: """ + postion[1] + """; 
					margin-left: """ + postion[0] + """; } \n"""

		htmlTbl = htmlTbl + forTbl 
		htmlCss += forCss

	html = htmlCss + htmlTbl + htmlEnd

	f = open("Hello.html", "w")
	f.write(html)



tbl=[['Mon', None, None, None, None, None, None, None, 'LEC MRT 218 MAT2322 B00', 'LEC MRT 218 MAT2322 B00', 'LEC MRT 218 MAT2322 B00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], ['Tue', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], ['Wed', None, None, None, None, None, None, None, 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', None, None, None, 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', None, None, None, None, None, None, None, None, None, None], ['Thu', None, None, None, None, None, None, None, None, None, None, 'LEC MRT 218 MAT2322 B00', 'LEC MRT 218 MAT2322 B00', 'LEC MRT 218 MAT2322 B00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', 'LEC LPR 155 ELG2138 A00', None, None, None, None, None, None, None, None, None, None, None, None, None], ['Fri', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
UseThis(tbl)


