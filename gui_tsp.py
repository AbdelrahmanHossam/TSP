# ! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tsartsaris Sotiris"
__copyright__ = "Copyright 2014, The TSP Project"
__credits__ = ["Tsartsaris Sotiris"]
__license__ = "APACHE 2.0"
__version__ = "1.0.1"
__maintainer__ = "Tsartsaris Sotiris"
__email__ = "info@tsartsaris.gr"
__status__ = "Development"

from Tkinter import *
import tkFileDialog
import ttk

root = Tk()
root.title("TSP Solver")
root.geometry("1024x768")


def openfile():
    filename = tkFileDialog.askopenfilename()
    produce_final(filename)

# entry_1 = Entry(root)
# entry_2 = Entry(root)

# entry_1.grid(row = 0, column = 0)
# entry_2.grid(row = 1, column = 1)

# def printName(event):
#     print "Hello Sam"

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side = BOTTOM)
# theLabel = ttk.Label(root, text = 'test again test')
# theLabel.grid(row = 0, column = 1, sticky = W)
# c = Checkbutton(root, text = "keep me in man")
# c.grid(columnspan = 2)

button1 = ttk.Button(root, text = 'test', padding = 5, command = openFile)
# button1.bind("<Button-1>", printName)
# button2 = ttk.Button(topFrame, text = 'test')
# button3 = Button(root, text = 'test')
# button4 = ttk.Button(bottomFrame, text = 'test')

button1.grid(row = 0, column = 1, sticky = W)
# button2.pack(side = LEFT)
# button3.pack(fill = X)
# button4.pack(side = LEFT)


root.mainloop()