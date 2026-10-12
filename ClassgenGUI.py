#This file is for the purpose of generating a random number of individuals of each class for the appropriate distribution of a single continent

import tkinter as tk
from openpyxl import Workbook
from Universal_GUI_styling import *
import random
import math

class PageFour(tk.Frame):
        
#------------------------------------------------------------------------

    def cleanup(self, controller, reset_buttons):
        controller.geometry("600x444")
        controller.update()
        if reset_buttons:
            self.nametowidget("backButton").destroy()
            self.nametowidget("submitButton").destroy()
        
#------------------------------------------------------------------------

    def submit(self, controller):
        global list_length
        self.cleanup(controller, False)
        if controller.ws['D37'].value == 2:
            for i in range(list_length):
                controller.ws.cell(row = 22, column = i+6).value = int(pop_list[i].get())
        controller.finish()
        
#------------------------------------------------------------------------

    def back(self, controller):
        self.cleanup(controller, True)
        controller.show_frame(3)
        
#------------------------------------------------------------------------
        
    def backup(self, controller):
        #When backing up, just reset the window dimensions
        if ((list_length * 18) + 8) > 444:
            controller.geometry("600x" + str((list_length * 18) + 8))
            controller.update()
        
#------------------------------------------------------------------------
            
    #Finds what class the given individual maps to, and updates the running tally of how many members there are of that class
    def find_class(self, class_list, rand_list, r):
        for i in range(len(rand_list)-1, -1, -1):
            if (r <= rand_list[i]):
                class_list[i] += 1
                return class_list

#------------------------------------------------------------------------

    #Perform an update to all the values of the class population distribution
    def update_distribution(self, controller):
        
        #Set up a list
        rand_list = [0] * list_length
        classes = [0] * list_length

        #First, scale out to the maximum, to ensure each cell will hold an integer at the end.
        rand_list[-1] = int(denomenator.get()) ** (list_length - 1)

        #Then, set the "size" of each section, relative to the rest
        for i in range(list_length-2, -1, -1):
            rand_list[i] = int(rand_list[i+1] * int(numerator.get())/int(denomenator.get()))

        #Then, add the sections together to get the full span.
        for i in range(list_length-2, -1, -1):
            rand_list[i] = rand_list[i] + rand_list[i+1]

        #Generate all the PCs by class, randomly
        for i in range(int(controller.ws['B1'].value)):
            r = random.randrange(1,rand_list[0]+1)

            classes = self.find_class(classes, rand_list, r)

        for i in range(list_length):
            pop_list[i].set(classes[i])
        
        controller.ws['D37'].value = 2
        
#------------------------------------------------------------------------

    def update_list(self, controller):

        global list_length
        #Get the length of the list of classes
        list_length = int(controller.ws['A6'].value)

        #If the class_list is longer than the incoming value, then we need to clean up some excess space
        if len(class_list) > list_length:
            for i in range(list_length, len(class_list)):
                class_list.pop()
                pop_list.pop()
                display_list.pop()
        #If the class_list is shorter than the incoming value, create extra space to store it
        elif len(class_list) < list_length:
            for i in range(list_length-len(class_list)):
                class_list.append("")
                pop_list.append(tk.StringVar())
                display_list.append(tk.Label(self, textvariable=pop_list[i]
                                             ).place(y=4+i*18,x=4))
                
        #Set all the class names to the correct values
        for i in range(list_length):
            class_list[i] = controller.ws.cell(row=21, column=i+6).value

        #As we updated the list, reset/update the class distribution as well
        self.update_distribution(controller)
        
#------------------------------------------------------------------------        

    #This function checks if there have been any modifications to the variables set so far when arriving from Page Three 
    def startup(self, controller):

        global list_length
        
        #If the class list has been changed, perform a full reset
        if controller.ws['C37'].value == 2:
            self.update_list(controller)
            #Mark that the new values have been received
            controller.ws['B37'].value = 1
            controller.ws['C37'].value = 1

        #If only the population was updated, then only update that without resetting the classes
        elif controller.ws['B37'].value == 2:
            self.update_distribution(controller)
            #Mark that the new values have been received
            controller.ws['B37'].value = 1

        #Scale the height of the window to fit the fields we intend to populate it with
        if ((list_length * 18) + 8) > 444:
            controller.geometry("600x" + str((list_length * 18) + 8))
            controller.update()

        #Create and place the forward and back buttons
        back_button = tk.Button(self, name="backButton", text='Back', command=lambda: self.back(controller)).place(
            x=300, y=controller.winfo_height()-35)
        submit_button = tk.Button(self, name="submitButton",  text="Submit", command=lambda: self.submit(controller)).place(
            x=540, y=controller.winfo_height()-35)
        
#------------------------------------------------------------------------

    def __init__(self, parent, controller, defaults):
        tk.Frame.__init__(self, parent)

        #Create the variables that we will use later but don't set them
        #Most of these depend on the values of other pages, so we can't set them yet
        global pop_list, class_list, display_list, numerator, denomenator
        list_length = 0
        pop_list = []
        class_list = []
        display_list = []

        #Set up and load the default values for this page
        numerator = tk.StringVar()
        numerator.set(defaults[6])
        denomenator = tk.StringVar()
        denomenator.set(defaults[7])
