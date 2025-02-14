#This file is for the purpose of generating a random number of champions of each class for the appropriate distribution of a single continent
#In the 1.0 build, the order of the classes is fixed, and it can't be rearranged or have new classes added in
#This is the first change desired in future iterations

import random
import math

#------------------------------------------------------------------------

def find_class(class_list, rand_list, r):
    for i in range(len(rand_list)):
        if (r <= rand_list[i]):
            class_list[i] += 1
            return class_list

#------------------------------------------------------------------------

loop = 1

while loop == 1:
    answer = str(input("Read from File? (R) or Write own list? (W)\n"))
    if answer == "R" or answer == "W":
        break
    print("Answer not recognized. ")

if answer == "W":
    length = int(input("How long is the class list?\n"))
    while length < 1:
        length = int(input("You must input at least 1 class.\n"))

    print("List classes in order of least to most common")

    randlist = [0] * length
    classes = [0] * length

    classlist = ["blank"] * length

    for i in range(length):
        classlist[i] = str(input("..."))
else:
    length = 23
    randlist = [0] * length
    classes = [0] * length

    classlist = ["Monk", "Psychic", "Inventor", "Gunslinger", "Cleric", "Oracle",
                 "Champion", "Druid", "Kineticist", "Barbarian", "Ranger", "Swashbuckler",
                 "Witch", "Fighter", "Rogue", "Thaumaturge", "Sorcerer", "Summoner",
                 "Investigator", "Bard", "Alchemist", "Magus", "Wizard"]

randlist[0] = 3 ** (length - 1)

for i in range(1, length):
    randlist[i] = int(randlist[i-1] * 4/3)

for i in range(1, length):
    randlist[i] = randlist[i] + randlist[i-1]

print(randlist)
#print(randlist[length-1]+1)

x = int(input("Number of iterations"))

for i in range(x):
    r = random.randrange(1,randlist[length-1]+1)

    classes = find_class(classes, randlist, r)
    

for n in range(len(classes)-1, -1, -1):
    print(classlist[n],": ",classes[n], sep = "")
