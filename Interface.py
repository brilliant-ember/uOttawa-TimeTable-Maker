from tkinter import *
class MainWindow:
	def __init__(self, master):
		frame = Frame(master)
		frame.grid()

		self.label1 = Label(master, text="Please input the course codes", bg="black", fg="yellow")
		self.label1.grid(row =0)

		self.labelc1 = Label(master, text="Course 1")
		self.labelc1.grid(row=0)
		self.entry1 = Entry(master)
		self.entry1.grid(row=1,column=1)
		self.labelc1.grid(row=1)
		self.b1 = Button(frame, text="Add",command=self.func)



	def added(self):
		pass
	def func(self):
		pass
root = Tk()
MainWindow(root)
root.mainloop()