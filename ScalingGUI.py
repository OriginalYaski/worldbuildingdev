#This window is for the purpose of setting up how many individuals there are of each character level in this setting

import tkinter as tk
import random
from openpyxl import Workbook
from Universal_GUI_styling import *
from ClasslistGUI import PageThree


class PageTwo(tk.Frame):

#------------------------------------------------------------------------

    #This function saves the generated values to the appropriate spot in the excel file and moves to the next page
    def submit(self, controller):

        #Setup the PC and total level distributions
        #The total_lists method has been set up to accept variable scaling, but this method isn't set up for that just yet
        PC_lvl_list = self.total_lists(controller.ws, PC_total,
                                       4, int(scalar.get()), int(frequency.get()))
        Total_lvl_list = self.total_lists(controller.ws, Adult_total,
                                          3, int(scalar.get()), int(frequency.get()))

        controller.ws['C21'].value = "Adults per level"
        controller.ws['C21'].border = BOTTOM_CELL
        controller.ws.column_dimensions['C'].width = 15
        
        controller.ws['D21'].value = "PCs per level"
        controller.ws['D21'].border = BOTTOM_CELL
        controller.ws.column_dimensions['D'].width = 13

        # Apply style
        for i, rowOfCellObjects in enumerate(controller.ws['C2':'D20']):
            for n, cellObj in enumerate(rowOfCellObjects):
                cellObj.border = COLUMN
        controller.ws['C1'].border = TOP_CELL
        controller.ws['D1'].border = TOP_CELL
        
        
        controller.save()
        controller.show_frame(PageThree)

#------------------------------------------------------------------------

    #method to setup the PC and total per-level values
    def total_lists(self, sheet, total, col, falloff, scale):
        #The function used to generate the per-level values technically extends up to level infinity
        #This helps take all those people that should exist at levels 21+ and rounds them into the level 20 values
        tracker = total

        #Create output list
        output = [0,]*20

        for i in range(0, 19):
            #Get value for the level
            val = round(total/(falloff**(i/scale))-total/(falloff**((i+1)/scale)))

            #Write value to cell
            sheet.cell(row = 20 - i, column = col, value = val)

            #Add value to list
            output[i] = val

            #print(val)

            #Increment tracker
            tracker -= val

        #We aren't going to epic levels, so keep all the rest
        sheet.cell(row = 1, column = col, value = tracker)
        output[19] = tracker
        #print(tracker)

        return output

#------------------------------------------------------------------------

    def startup(self, controller):

        global PC_total, Adult_total

        #Get the totals
        PC_total = int(controller.ws.cell(row = 1, column = 2).value)
        Adult_total = int(controller.ws.cell(row = 3, column = 2).value)
        
#------------------------------------------------------------------------

    def __init__(self, parent, controller, defaults):
        tk.Frame.__init__(self, parent)

        global scalar, frequency

        PC_total = 1
        Adult_total = 1
        
        scalar = tk.StringVar()
        scalar.set(defaults[4])
        frequency = tk.StringVar()
        frequency.set(defaults[5])

        submitButton = tk.Button(self, text="Submit",
                                 command=lambda: self.submit(controller)).pack(side="bottom")
        
