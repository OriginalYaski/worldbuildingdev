#This file is intended as the general GUI/primary operator of each of the sub-files in this project

import tkinter as tk

class PageOne(tk.Frame):
    
    #Placeholder submit command. Prints submitted list to the IDLE shell currently
    def submit(self, controller):
        for i in range(len(varList)):
            if varList[i].get() == 1:
                print(classList[i], end="\n")

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

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global classList, varList, updateVar, c, r
        c = r = pointer = 0
        #Create the window
        #root = tk.Tk()
        #root.title("Select Classes")
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
        with open("default values.txt") as f:
            defaultlist = f.read().splitlines()
            classList = defaultlist[0].split(", ")
        '''classList = ["Alchemist", "Animist", "Barbarian", "Bard", "Champion",
                     "Cleric", "Commander", "Druid", "Exemplar", "Fighter",
                     "Guardian", "Gunslinger", "Inventor", "Investigator", "Kineticist",
                     "Magus", "Monk", "Oracle", "Psychic", "Ranger",
                     "Rogue", "Sorcerer", "Summoner", "Swashbuckler", "Thaumaturge",
                     "Witch", "Wizard"]'''
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
