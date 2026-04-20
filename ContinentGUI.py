#This file is intended as the general GUI/primary operator of each of the sub-files in this project

import tkinter as tk

def submit():
    for i in range(len(varList)):
        if varList[i].get() == 1:
            print(classList[i], end="\n")

    root.destroy()

r = c = pointer = 0

root = tk.Tk()
root.title("Select Classes")

listFrame = tk.Frame(root)
bottomFrame = tk.Frame(root)

listFrame.pack(side="top")
bottomFrame.pack(side="bottom")

entryFrame = tk.Frame(bottomFrame)
submitFrame = tk.Frame(bottomFrame)

entryFrame.pack(side="left")
submitFrame.pack(side="right")

classList = ["Alchemist", "Animist", "Barbarian", "Bard", "Champion",
             "Cleric", "Commander", "Druid", "Exemplar", "Fighter",
             "Guardian", "Gunslinger", "Inventor", "Investigator", "Kineticist",
             "Magus", "Monk", "Oracle", "Psychic", "Ranger",
             "Rogue", "Sorcerer", "Summoner", "Swashbuckler", "Thaumaturge",
             "Witch", "Wizard"]

varList = [tk.IntVar() for _ in range(27)]


for name in classList:
    tk.Checkbutton(listFrame, text=name, variable=varList[pointer]).grid(row=r, column=c)
    c += 1
    pointer += 1
    if c > 4:
        r += 1
        c = 0

updateVar = tk.StringVar()

def update_list():
    global c, r
    classList.append(updateVar.get())
    varList.append(tk.IntVar())

    tk.Checkbutton(listFrame, text=classList[-1], variable=varList[-1]).grid(row=r, column=c)
    c += 1
    if c > 4:
        r += 1
        c = 0

    updateVar.set("")

newLabel = tk.Label(entryFrame, text="Add another class to the list").pack(side="top")
newClass = tk.Entry(entryFrame, textvariable = updateVar)
newClass.pack(side="left")
classButton = tk.Button(entryFrame, text="Add", command=update_list).pack(side="left")
submitButton = tk.Button(submitFrame, text="Submit", command=submit).pack(side="bottom")

root.mainloop()
