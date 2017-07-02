

import cx_Freeze
import sys
import os

os.environ['TCL_LIBRARY'] = "D:\\Programs\Python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "D:\\Programs\Python\\tcl\\tk8.6"
includes = ["Activator.py","Initial.py","Schedule.py","tableHtml.py","tcl86t.dll", "tk86t.dll"]
base = None

if sys.platform == "win32":
	base = "Win32GUI"

executables = [cx_Freeze.Executable("Interface.py")]

cx_Freeze.setup(
	name = "Uottawa Table Maker",
	version = "0.1",
	description = "I will show you all course combinations",
	executables = executables,
	options = {'build_exe': {'include_files':includes,"packages": ["selenium"]}},
	
	)