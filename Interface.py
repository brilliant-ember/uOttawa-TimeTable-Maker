from tkinter import *



class MainWindow:
	def __init__(self, master):
		frame = Frame(master)
		frame.grid()
		
		self.label1 = Label(master, text = "Please input the semster and course codes", bg="black", fg="yellow",width=60)
		self.label1.grid(row = 0, columnspan = 100)

		self.sem=Label(master, text="Write F for the Fall, W for the Winter, or S for the Summer/Spring semesters ")
		self.sem.grid(row = 1, pady = 15)
		self.semEntry = Entry(master)
		self.semEntry.grid(row = 1, column = 1, pady = 15)
		self.labelc1 = Label(master, text ="Course 1")
		self.labelc1.grid(row = 2, pady = 15) 
		self.entry1 = Entry(master)
		self.entry1.grid(row = 2, column = 1, pady = 15, padx = 15)

		self.labelc2 = Label(master, text ="Course 2")
		self.labelc2.grid(row = 3) 
		self.entry2 = Entry(master)
		self.entry2.grid(row = 3, column = 1,  padx = 15)

		self.labelc3 = Label(master, text ="Course 3")
		self.labelc3.grid(row = 4, pady = 15) 
		self.entry3 = Entry(master)
		self.entry3.grid(row = 4, column = 1,  padx = 15, pady = 15)

		self.labelc4 = Label(master, text ="Course 4")
		self.labelc4.grid(row = 5) 
		self.entry4 = Entry(master)
		self.entry4.grid(row = 5, column = 1,  padx = 15)

		self.labelc5 = Label(master, text ="Course 5")
		self.labelc5.grid(row = 6, pady = 15) 
		self.entry5 = Entry(master)
		self.entry5.grid(row = 6, column = 1,  padx = 15, pady = 15)

		self.labelc6 = Label(master, text ="Course 6")
		self.labelc6.grid(row = 7) 
		self.entry6 = Entry(master)
		self.entry6.grid(row = 7, column = 1,  padx = 15)

		self.labelc7 = Label(master, text ="Course 7")
		self.labelc7.grid(row = 8, pady = 15) 
		self.entry7 = Entry(master)
		self.entry7.grid(row = 8, column = 1,  padx = 15, pady = 15)

		self.v = IntVar()
		self.v.set(1)
		Radiobutton(master, text = "Style 1", variable = self.v, value = 1).grid(row=9)
		Radiobutton(master, text = "Style 2", variable = self.v, value = 2).grid(row=9,column=1)
		Radiobutton(master, text = "Dark style", variable = self.v, value = 3).grid(row=10)
		Radiobutton(master, text = "Blue style", variable = self.v, value = 4).grid(row=10,column=1)

		helpB = Button(master, text="help", command=self.helpF, width=15).grid(row=11,column=1 ,padx=5,pady=15)
		submitB = Button(master, text="Submit!", fg="red", command=self.submit, width=15,  font = ("Vendera", 20, "bold italic")).grid(row=11 ,padx=5,pady=15)
	def helpF(self):
		pass
		# L = [self.entry1]
		# for i in range(len (L)):
		# 	if len(L[i]) !=7:
		# 		print('YAY')



	def submit(self):
		# if self.v.get==1:
		# 	selected = x
		pass

	def popError(self):
		popup=Tk()
		popup.title("Tragic Error") 
		if True:
			pass
		label = Label(popup, text=msg, font = ("Vendera", 10))
		label.pack(fill = "x", pady = 10)
		popup.mainloop()


root = Tk()
root.title("Lovely Schedule Maker")
MainWindow(root)
root.mainloop()