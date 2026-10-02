#Top level GUI caller for the project

import tkinter as tk
from openpyxl import Workbook
from openpyxl import load_workbook
from ClasslistGUI import Window1

def submit():
    campaign = updateVar.get()
    wb = Workbook()
    ws = wb.create_sheet('Big sheet 1')
    wb.save(campaign + '.xlsx')
    wb.close()
    root.destroy()

    window = Window1()
    window.run(campaign)

with open("default values.txt") as f:
    defaultlist = f.read().splitlines()
    classList = defaultlist[0].split(", ")
    '''pop = int(defaultlist[1])
    ratio = int(defaultlist[2])'''

#Create the window
root = tk.Tk()
root.title("New campaign")
#Create the frames for the window
titleFrame = tk.Frame(root)
enterFrame = tk.Frame(root)
#Place the frames within the window
titleFrame.pack(side="top")
enterFrame.pack(side="bottom")

updateVar = tk.StringVar()

title = tk.Label(titleFrame, text="Welcome to your new campaign! Please, give it a name.").pack(side="top")
newCampaign = tk.Entry(enterFrame, textvariable = updateVar)
newCampaign.pack(side="left")
submitButton = tk.Button(enterFrame, text="Submit", command=submit).pack(side="right")

root.mainloop()


