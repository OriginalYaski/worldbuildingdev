#This file is for the purpose of generating a random number of individuals of each class for the appropriate distribution of a single continent
#The code for draggable listboxes was sources from: https://www.plus2net.com/python/tkinter-drag-and-drop.php

import tkinter as tk
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from Universal_GUI_styling import *
import random, math, pathlib, os


class PageFour(tk.Frame):
        
#------------------------------------------------------------------------
    
    def start_drag(self, event):
        listbox=event.widget

        index=listbox.nearest(
            event.y
        )

        box=listbox.bbox(
            index
        )

        if box is None:
            listbox.dragged_index=None
            return

        top=box[1]
        height=box[3]

        if not (
            top <= event.y <= top + height
        ):
            listbox.dragged_index=None
            return

        listbox.dragged_index=index
            
#------------------------------------------------------------------------
        
    def on_drop(self, event):
        
        listbox=event.widget
        source=listbox.dragged_index

        if source is None:
            return

        target=listbox.nearest(
            event.y
        )

        item=listbox.get(
            source
        )

        listbox.delete(
            source
        )

        if source < target:
            target -= 1

        listbox.insert(
            target,
            item
        )

        listbox.selection_clear(
            0,
            'end'
        )

        listbox.selection_set(
            target
        )

        listbox.dragged_index=None
    
#------------------------------------------------------------------------

#On leaving this page, reset the window to its default dimensions and make sure that the window updates this fact
    def cleanup(self, controller):
        controller.geometry("600x444")
        controller.update()
        
#------------------------------------------------------------------------

    def submit(self, controller):
        global list_length
        self.cleanup(controller)
        if controller.ws['D37'].value == 2:
            l = 0
            for i in range(list_length):
                controller.ws.cell(row = 21, column = i+6).value = listbox.get(i)
                controller.ws.cell(row = 22, column = i+6).value = int(pop_list[i].get())
                if len(controller.ws.cell(row = 21, column = i+6).value) > l:
                    l = len(controller.ws.cell(row = 21, column = i+6).value)
                if len(str(controller.ws.cell(row = 22, column = i+6).value)) > l:
                    l = len(str(controller.ws.cell(row = 22, column = i+6).value))

            for i in range(6, list_length+6):
                controller.ws.column_dimensions[get_column_letter(i)].width = l+1
        controller.finish()
        
#------------------------------------------------------------------------

    def back(self, controller):
        #When backing up OUT OF this window, just reset the window dimensions for the previous page and leave
        self.cleanup(controller)
        controller.show_frame(3)
        
#------------------------------------------------------------------------
        
    def backup(self, controller):
        #When backing up INTO this window, just reset the window dimensions to the larger dimensions of this page
        if ((list_length * 16) + 8) > 444:
            controller.geometry("600x" + str((list_length * 16) + 8))
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

    def reroll(self, controller):
        self.update_distribution(controller)
        
#------------------------------------------------------------------------

    def increment(self, pos, target):
        if pos:
            pop_list[target].set(str(int(pop_list[target].get()) + 1))
        else:
            pop_list[target].set(str(int(pop_list[target].get()) - 1))
        
#------------------------------------------------------------------------

    def update_list(self, controller):

        global list_length, marker
        #Get the length of the list of classes
        list_length = int(controller.ws['A6'].value)

        #If the class_list is longer than the incoming value, then we need to clean up some excess space
        if len(class_list) > list_length:
            for i in range(list_length, len(class_list)):
                class_list.pop()
                #display_list.pop()
                self.nametowidget("label" + str(i)).destroy()
                self.nametowidget("up" + str(i)).destroy()
                self.nametowidget("down" + str(i)).destroy()
                pop_list.pop()
                #print(str(len(display_list)))
                
        #If the class_list is shorter than the incoming value, create extra space to store it
        elif len(class_list) < list_length:
            for i in range(len(class_list), list_length):
                class_list.append("")
                pop_list.append(tk.StringVar())
                tk.Label(self, textvariable=pop_list[-1],
                         font=DEFAULT_FONT,
                         name="label" + str(i), width=8,
                         relief="solid", borderwidth=1)
                self.nametowidget("label" + str(i)).place(y=5+i*21,x=166)
                tk.Button(self, name="up" + str(i), image=plus, highlightthickness = 0,
                          width=14, height=7, bd=2, relief="groove",
                          command=lambda x=i: self.increment(True, x)).place(
                              y=6+i*21, x=226)
                tk.Button(self, name="down" + str(i), image=minus, highlightthickness = 0,
                          height=7, width=14, bd=2, relief="groove",
                          command=lambda x=i: self.increment(False, x)).place(
                              y=16+i*21, x=226)
                #canvas.create_line(0, 3+(i+1)*16, 55, 3+(i+1)*16)
                
        #Set all the class names to the correct values
        for i in range(list_length):
            class_list[i] = controller.ws.cell(row=21, column=i+6).value


        #As we updated the list, reset/update the class distribution as well
        self.update_distribution(controller)
        
#------------------------------------------------------------------------

    def load_in(self, controller):
        #Just in case we are loading an already running campaign of this name, check to see if there are any classes that should be added, and check the selected classes
        return
        
#------------------------------------------------------------------------        

    #This function checks if there have been any modifications to the variables set so far when arriving from Page Three 
    def startup(self, controller):

        global list_length, listbox
        new_buttons = False
        
        #If the class list has been changed, perform a full reset
        if controller.ws['C37'].value == 2:
            #If this is not our first time visiting this page, we need to reset certain objects
            if controller.ws['D37'].value != 0:
                self.nametowidget("backButton").destroy()
                self.nametowidget("submitButton").destroy()
                self.nametowidget("class_display").destroy()
                #canvas.delete("all")
            
            self.update_list(controller)
            #Mark that the new values have been received
            controller.ws['B37'].value = 1
            controller.ws['C37'].value = 1

            new_buttons = True

        #If only the population was updated, then only update that without resetting the classes
        elif controller.ws['B37'].value == 2:
            self.update_distribution(controller)
            #Mark that the new values have been received
            controller.ws['B37'].value = 1

        #Scale the height of the window to fit the fields we intend to populate it with
        if ((list_length * 21) + 8) > 444:
            controller.geometry("600x" + str((list_length * 21) + 8))
            controller.update()

        #Sometimes we need to create new elements. But not all the time. We don't want to reset the entire page everytime someone hits the back button
        if new_buttons:
            #Create and place the forward and back buttons
            back_button = tk.Button(self, name="backButton", text='Back', command=lambda: self.back(controller)).place(
                x=250, y=controller.winfo_height()-35)
            submit_button = tk.Button(self, name="submitButton",  text="Submit", command=lambda: self.submit(controller)).place(
                x=540, y=controller.winfo_height()-35)

            #Create and place the listbox
            listbox = tk.Listbox(self, name="class_display",
                                 font = ("Segoe UI", 11), height=list_length)

            listbox.place(x=2, y=3)

            for i in range(list_length):
                listbox.insert('end', class_list[i])

            listbox.dragged_index=None

            listbox.bind('<ButtonPress-1>', self.start_drag)

            listbox.bind('<ButtonRelease-1>', self.on_drop)

        
#------------------------------------------------------------------------

    def __init__(self, parent, controller, defaults):
        global plus, minus, pop_list, class_list, numerator, denomenator
        tk.Frame.__init__(self, parent)
        up_file = "up.png"
        down_file = "down.png"
        current_dir = pathlib.Path(__file__).parent.resolve()
        up_path = os.path.join(current_dir, up_file)
        down_path = os.path.join(current_dir, down_file)
        plus = tk.PhotoImage(file=up_path)
        minus = tk.PhotoImage(file=down_path)

        #Create the variables that we will use later but don't set them
        #Most of these depend on the values of other pages, so we can't set them yet 
        list_length = 0
        pop_list = []
        class_list = []

        #Set up and load the default values for this page
        #We haven't set this to be modifiable yet, but we are storing it as the correct variable in preparation
        numerator = tk.StringVar()
        numerator.set(defaults[6])
        denomenator = tk.StringVar()
        denomenator.set(defaults[7])
        explanation = tk.Message(self, name="explanation",
                                 font=DEFAULT_FONT, width=330,
                                 text='It is not guaranteed that all classes are created equal. At least, not in the eyes of your Campaign\'s residents they might not be. '
                                 'When your NPCs are choosing what class they would like to put their effort into, not every choice may be as tempting as the last. '
                                 'Is this a wild setting with an above average number of barbarians? Is wizardry considered the height of power, and so your setting is filled to the gills with them? '
                                 'Is divinity rare in this setting, and thus clerics and champions are rare? '
                                 'This page is to help design a naturalistic spread of classes due to the personal preferences of your Campaign\'s residents.').place(
                                     x=250, y=100)
