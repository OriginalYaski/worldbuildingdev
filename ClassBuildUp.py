#Step one of getting the baseline level distribution (without extra NPC levels)

import random
from openpyxl import Workbook
from openpyxl import load_workbook

#for the progress display
CURRENT_PERCENT = 0

#------------------------------------------------------------------------

#method to setup the PC and total per-level values
def total_lists(sheet, total, col, falloff, scale):
    #Account for potential upper remainders
    tracker = total

    #Create output list
    output = [0,]*20

    for i in range(0, 19):
        #Get value for the level
        val = round(total/(falloff**(i/scale))-total/(falloff**((i+1)/scale)))

        #Write value to cell
        ws.cell(row = 20 - i, column = col, value = val)

        #Add value to list
        output[i] = val

        print(val)

        #Increment tracker
        tracker -= val

    #We aren't going to epic levels, so keep all the rest
    ws.cell(row = 1, column = col, value = tracker)
    output[19] = tracker
    print(tracker)

    return output

#------------------------------------------------------------------------

#todo make it accept variable user input
wb = load_workbook('The new organizer.xlsx')

ws = wb['Big sheet 1']

#Get the enpoint of the list
global mark
mark = ws['A1'].value + 1

#get the list of class priority
PC_class_list = [ws.cell(row = 21, column = i).value for i in range(2,mark+1)]

#Get the totals
PC_total = ws.cell(row = 1, column = mark + 4).value
Adult_total = ws.cell(row = 2, column = mark + 4).value

#Setup the PC and total level distributions
PC_lvl_list = total_lists(ws, PC_total, mark+1, 169, 5)
Total_lvl_list = total_lists(ws, Adult_total, mark+2, 169, 5)

#generate the class distribution array
level_array = {}
level_key = 1

#PC_tracker = [ws.cell(row = i, column = 24).value for i in range(1,21)]
#total_tracker = [ws.cell(row = i, column = 25).value for i in range(1,21)]

#total_demographics = dict_make(ws['AA3'].value, ws, PC_class_list)

#to do, make it output automatically to either an excel sheet or a txt file
#for x in total_demographics.keys():
#    print(total_demographics[x])

wb.save('The new organizer.xlsx')
wb.close()
