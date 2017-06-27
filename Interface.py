from tkinter import *
import webbrowser
import Activator as Av
from selenium.common.exceptions import TimeoutException
import multiprocessing as M


if __name__=="__main__":
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
			Buy = Button(master, text="Buy the developer a coffee!", command=self.Coffee, fg="red",bg="white", font = ("Vendera", 20, "bold italic")).grid(row=12 ,padx=15,pady=15)

			submitB = Button(master, text="Submit!", command=self.submit,  font = ("Vendera", 20, "bold italic")).grid(row=11 ,padx=5,pady=15)
		def helpF(self):
			pass
			# L = [self.entry1]
			# for i in range(len (L)):
			# 	if len(L[i]) !=7:
			# 		print('YAY')

		def submit(self):

			Acti = True
			def AF():
				Acti = False
			data = [self.semEntry.get().lower(), self.entry1.get().replace(" ","").lower(), self.entry2.get().replace(" ","").lower(), self.entry3.get().replace(" ","").lower(), self.entry4.get().replace(" ","").lower(), self.entry5.get().replace(" ","").lower(), self.entry6.get().replace(" ","").lower(), self.entry7.get().replace(" ","").lower() ]
			if len(data[0]) != 1:
				self.popError("Make sure the semester entry is one charecter either F, W, or S")
				Acti = False
			for i in range(1, len(data)):
				courseE = data[i]
				if len(courseE) > 0  and len(courseE) != 7:
					self.popError("Course "+str(i)+" input is not right")
					Acti = False
			while Acti:
				try:
					popup = Toplevel()
					popup.title("Message")
					popup.lift() 
					label = Label(popup, text="In progress, please wait. the time is takes could vary depending the internet speed. Avarge time is 1 minute per course", font = ("Vendera", 10, "bold"))
					label.pack(fill = "x", pady = 10, padx=7)
					bb = Button(popup, text="Stop?", command = AF)
					bb.pack(side=BOTTOM, pady=7)
					

					if __name__=="__main__":
						m1 = M.Process(target=Av.mainMethod, args=(data, self.v.get()))
						m1.start()
						m1.join()
						Acti = False

					#Av.mainMethod(data, self.v.get())
				except TimeoutException:
					popup = Tk()
					popup.title("Guess What?! i got an error ;) ") 
					label =Label(popup, text="I couldn't find "+course+", I can't connect, check your internet connection ", font = ("Vendera", 10, "bold"))
					label.pack(fill = "x", pady = 10, padx=7)
					b = Button(popup, text="Destroy?", command = popup.destroy)
					b.pack(side=BOTTOM, pady=7)

					popup.mainloop()
					Acti = False



		def popError(self, msg):
			popup = Toplevel()
			popup.title("Tragic Error") 
			label = Label(popup, text=msg+", click on the help button for a beautiful tutorial", font = ("Vendera", 10, "bold"))
			label.pack(fill = "x", pady = 10, padx=7)
			b = Button(popup, text="Destroy?", command = popup.destroy)
			b.pack(side=BOTTOM, pady=7)
			popup.lift()


		def Coffee(self):
			webbrowser.open_new("paypal.me/ThanksShukranMerci/5")

		def style(self):
			pass
			# if self.v.get==1:
			# 	selected = x



	root = Tk()
	root.title("Lovely Schedule Maker")
	MainWindow(root)
	root.mainloop()