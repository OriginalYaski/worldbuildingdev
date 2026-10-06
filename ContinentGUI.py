#Top level GUI caller for the project

import tkinter as tk
from openpyxl import Workbook
from openpyxl import load_workbook
from DemographicsGUI import PageOne
from ClasslistGUI import PageThree

LARGE_FONT= ("Verdana", 12)

class MainWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        global campaign, wb, ws
        campaign = ""
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("TTRPG population generator")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        '''if cont == PageThree:
            cont.setup(self.frames[cont], self)'''

        frame = self.frames[cont]
        frame.tkraise()

    def save(self):
        self.wb.save(self.campaign + '.xlsx')

    def finish(self):
        self.save()
        self.wb.close()

        root.destroy()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #root.title("New campaign")
        #Create the frames for the window
        titleFrame = tk.Frame(self)
        enterFrame = tk.Frame(self)
        #Place the frames within the window
        titleFrame.pack(side="top")
        enterFrame.pack(side="bottom")

        updateVar = tk.StringVar()

        title = tk.Label(titleFrame, text="Welcome to your new campaign! Please, give it a name.", font=LARGE_FONT).pack(side="top", pady=10, padx=10)
        newCampaign = tk.Entry(enterFrame, textvariable = updateVar)
        newCampaign.pack(side="left")
        submitButton = tk.Button(enterFrame, text="Submit", command=lambda: self.submit(updateVar.get(), controller)).pack(side="right")

    def submit(self, title, controller):
        controller.campaign = title
        controller.wb = Workbook()
        controller.ws = controller.wb.create_sheet('Big sheet 1')

        controller.show_frame(PageOne)

'''with open("default values.txt") as f:
    defaultlist = f.read().splitlines()
    classList = defaultlist[0].split(", ")
    pop = int(defaultlist[1])
    ratio = int(defaultlist[2])'''

'''#Create the window
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
'''
root = MainWindow()
root.mainloop()


