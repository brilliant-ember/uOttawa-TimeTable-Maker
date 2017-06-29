The Initial script parses the website and organizes the data in table per course basis
The Schecdule combines tables and outputs the tables
#This only works with the version present in 2017 of the university's website, if at somepoint the website patterns and general design is changed, the program may not work
## if u get index out of bound error in SecNum method(param2), then check your internet connection because that means that u have an empty listt,and having an empty
list means that u didnt fetch any data form the site. Check ur internet connection and try again
Module Inital:
	takes a course URL and produces a course obj which has a variable reptrsenting all possible tables of the course.
	it countains a bunch of goodies including

	Class time:
		represents a time slot of half an hour, and it has a set of built in methods like fill and is empty

	Class table:
		represents a week table 


Module Inteface:
	responsible for the GUI made with Tkinter

Module Activator:
	Takes care of communicating the GUI input with the Schedule Module

Module Schedule:
	Takes the Tables and Makes a HTML tables using the tableHtml Module


Module tableHtml:
	takes input from Schedule Module and makes HTML tables