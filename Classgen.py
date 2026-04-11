#This file is for the purpose of generating a random number of individuals of each class for the appropriate distribution of a single continent

from openpyxl.styles import Border, Side
from openpyxl import Workbook
import random
import math

thin = Side(border_style="thin", color="00000000")
topcell = Border(top=thin, left=thin, right=thin)
bottomcell = Border(left=thin, right=thin, bottom=thin)
leftcell = Border(top=thin, left=thin, bottom=thin)
rightcell = Border(top=thin, right=thin, bottom=thin)

#------------------------------------------------------------------------
#Finds what class the given individual maps to, and updates the running tally of how many members there are of that class
def find_class(class_list, rand_list, r):
    for i in range(len(rand_list)-1, -1, -1):
        if (r <= rand_list[i]):
            class_list[i] += 1
            return class_list

#------------------------------------------------------------------------
#Begin method
loop = 1

while loop == 1:
    #In future, will allow user to read from a text file.
    #Not actually implemented yet.
    #For the moment, inputting R loads the default configuration.
    answer = str(input("Read from File? (R) or Write own list? (W)\n"))
    if answer == "R" or answer == "W":
        break
    print("Answer not recognized. ")

if answer == "W":
    length = int(input("How long is the class list?\n"))
    while length < 1:
        length = int(input("You must input at least 1 class.\n"))

    print("List classes in order of most to least common")

    randlist = [0] * length
    classes = [0] * length

    classlist = ["blank"] * length

    for i in range(length):
        classlist[i] = str(input("..."))
else:
    length = 25
    randlist = [0] * length
    classes = [0] * length

    classlist = ["Wizard", "Magus", "Alchemist", "Bard", "Investigator",
                 "Summoner", "Sorcerer", "Thaumaturge", "Rogue", "Fighter", "Witch",
                 "Swashbuckler", "Ranger", "Barbarian", "Kineticist", "Druid", "Champion",
                 "Oracle", "Animist", "Cleric", "Gunslinger", "Inventor", "Psychic",
                 "Monk", "Exemplar"]

#Generate the Workbook and the first sheet we will be working with
wb = Workbook()
ws = wb.create_sheet('Big sheet 1')

#This segment creates the class distribution
#Currently, the scaling of each class relative to the rest is fixed


#If you multiply 1 by 5/3, you get a fraction. If you multiply 2 by 5/3, you get a fraction. If you multiply 3 by 5/3, you get an integer.
#As long as the denominator is a factor of the number you are multiplying by, you will get an integer.
#As we are going to be multiplying by the ratio multiple times, our starting number must be a factor of the denominator raised to (the length of the list - 1)

#First, scale out to the maximum, to ensure each cell will hold an integer at the end.
L = length - 1
randlist[L] = 3 ** (L)

#Then, set the "size" of each section, relative to the rest
for i in range(L-1, -1, -1):
    randlist[i] = int(randlist[i+1] * 4/3)

#Then, add the sections together to get the full span.
for i in range(L-1, -1, -1):
    randlist[i] = randlist[i] + randlist[i+1]

#Used for calibration/confirmation of proper randlist setup (Optional)
#print(randlist)
#print(randlist[length-1]+1)



answer = str(input("Use default setup?"))
if answer == "Y":
    x = 5120000
    y = 640000000
#This needs to be fleshed out
else:
    x = int(input("Number of iterations"))
    #Need to give controls on ratio of adults to exalted, etc., but I'm hardcoding for now
    y = 640000000


#Store the size of the class matrix and label it
lengthtitle = ws['A1']
c_length = ws['A2']

lengthtitle.value = "Number of classes"
c_length.value = length

lengthtitle.border = topcell
c_length.border = bottomcell



#Store the total PCs, total Adults, and total NPCs (respectively)
pcs = ws.cell(row = 1, column = length + 5, value = x)
ads = ws.cell(row = 2, column = length + 5, value = y)
npcs = ws.cell(row = 3, column = length + 5, value = y-x)

pcs.border = ads.border = npcs.border = leftcell

#Label the above values (respectively)
pcs = ws.cell(row = 1, column = length + 6, value = "Total PCs")
ads = ws.cell(row = 2, column = length + 6, value = "Total Adults")
npcs = ws.cell(row = 3, column = length + 6, value = "Total NPCs")

pcs.border = ads.border = npcs.border = rightcell


#Generate all the PCs by class, randomly
for i in range(x):
    r = random.randrange(1,randlist[0]+1)

    classes = find_class(classes, randlist, r)
    
#Print and store all the PCs by class
for n in range(len(classes)):
    ws.cell(row = 21, column = n+2, value = classlist[n])
    ws.cell(row = 22, column = n+2, value = classes[n])
    print(classlist[n],": ",classes[n], sep = "")

bookname = str(input("Enter file name to save classlist to: "))
wb.save(bookname + '.xlsx')
wb.close()
