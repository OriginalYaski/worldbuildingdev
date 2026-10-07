#This window is for the purpose of setting up the available classes in this setting

import tkinter as tk
from openpyxl.styles import Border, Side
from openpyxl import Workbook
from Universal_GUI_styling import *
from ClassgenGUI import PageFour

class PageThree(tk.Frame):
    
    #Placeholder submit command. Prints submitted list to the IDLE shell currently
    def submit(self, controller):

        x = 0
        for i in range(len(varList)):
            if varList[i].get() == 1:
                x += 1
                controller.ws.cell(row = 21, column = x+5, value = classList[i])
                

        #Store the size of the class matrix and label it
        lengthtitle = controller.ws['A5']
        c_length = controller.ws['A6']

        lengthtitle.value = "Number of classes"
        c_length.value = x

        lengthtitle.border = TOP_CELL
        c_length.border = BOTTOM_CELL

        #controller.save()

        controller.finish()


    #When the button is pressed, update the displayed and stored lists
    def update_list(self, frame):
        global r, c
        classList.append(updateVar.get())
        varList.append(tk.IntVar())

        tk.Checkbutton(frame, text=classList[-1], variable=varList[-1]).grid(row=r, column=c)
        c += 1
        if c > 4:
            r += 1
            c = 0

        updateVar.set("")

    def select_all(self):
        for num in varList:
            num.set(1)

    def select_none(self):
        for num in varList:
            num.set(0)

    def __init__(self, parent, controller, defaults):
        tk.Frame.__init__(self, parent)
        global classList, varList, updateVar, c, r
        c = r = pointer = 0
        
        #Create the frames for the window
        listFrame = tk.Frame(self)
        bottomFrame = tk.Frame(self)
        #Place the frames within the window
        listFrame.pack(side="top")
        bottomFrame.pack(side="bottom")
        #Create more frames to place within the bottom frame
        entryFrame = tk.Frame(bottomFrame)
        submitFrame = tk.Frame(bottomFrame)
        selectFrame = tk.Frame(submitFrame)
        #Place the frames within the bottom frame
        entryFrame.pack(side="left")
        submitFrame.pack(side="right")
        selectFrame.pack(side="left")
        #Set up the class list
        classList = defaults[0].split(", ")
        #Create list to hold values of checkbuttons
        varList = [tk.IntVar() for _ in range(len(classList))]

        #Set up the list of classes for display
        for name in classList:
            tk.Checkbutton(listFrame, text=name, variable=varList[pointer]).grid(row=r, column=c)
            c += 1
            pointer += 1
            if c > 4:
                r += 1
                c = 0
                
        #The variable where the new class name is stored
        updateVar = tk.StringVar()

        #Create and display the elements to add a new class to the list, and to submit the final list
        newLabel = tk.Label(entryFrame, text="Add another class to the list").pack(side="top")
        newClass = tk.Entry(entryFrame, textvariable = updateVar)
        newClass.pack(side="left")
        classButton = tk.Button(entryFrame, text="Add", command=lambda: self.update_list(listFrame)).pack(side="left")
        submitButton = tk.Button(submitFrame, text="Submit", command=lambda: self.submit(controller)).pack(side="right")
        allButton = tk.Button(selectFrame, text="Select All", command=self.select_all).pack(side="top")
        noneButton = tk.Button(selectFrame, text="Select None", command=self.select_none).pack(side="bottom", padx=20)
