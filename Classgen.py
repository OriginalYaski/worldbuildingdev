#This file is for the purpose of generating a random number of champions of each class for the appropriate distribution of a single continent
#In the 1.0 build, the order of the classes is fixed, and it can't be rearranged or have new classes added in
#This is the first change desired in future iterations

import random
import math

loop = 1

while loop == 1:
    answer = str(input("Read from File? (R) or Write own list? (W)\n"))
    if answer == "R" or answer == "W":
        break
    print("Answer not recognized. ")

if answer == "W":
    length = int(input("How long is the class list?\n"))

    print("List classes in order of least to most common")

    classes = [0] * length

    classlist = ["blank"] * length

    for i in range(length):
        classlist[i] = str(input("..."))
else:
    classes = [0] * 23

    classlist = ["Monk", "Psychic", "Inventor", "Gunslinger", "Cleric", "Oracle",
                 "Champion", "Druid", "Kineticist", "Barbarian", "Ranger", "Swashbuckler",
                 "Witch", "Fighter", "Rogue", "Thaumaturge", "Sorcerer", "Summoner",
                 "Investigator", "Bard", "Alchemist", "Magus", "Wizard"]

x = int(input("Number of iterations"))

for i in range(x):
    r = random.randrange(1,70274600998838)

    if (r <= 31381059609):
        classes[0] += 1
    elif (r <= 73222472421):
        classes[1] += 1
    elif (r <= 129011022837):
        classes[2] += 1
    elif (r <= 203395756725):
        classes[3] += 1
    elif (r <= 302575401909):
        classes[4] += 1
    elif (r <= 434814928821):
        classes[5] += 1
    elif (r <= 611134298037):
        classes[6] += 1
    elif (r <= 846226790325):
        classes[7] += 1
    elif (r <= 1159683446709):
        classes[8] += 1
    elif (r <= 1577625655221):
        classes[9] += 1
    elif (r <= 2134881933237):
        classes[10] += 1
    elif (r <= 2877890303925):
        classes[11] += 1
    elif (r <= 3868568131509):
        classes[12] += 1
    elif (r <= 5189471901621):
        classes[13] += 1
    elif (r <= 6950676928437):
        classes[14] += 1
    elif (r <= 9298950297525):
        classes[15] += 1
    elif (r <= 12429981456309):
        classes[16] += 1
    elif (r <= 16604689668021):
        classes[17] += 1
    elif (r <= 22170967283637):
        classes[18] += 1
    elif (r <= 29592670771125):
        classes[19] += 1
    elif (r <= 39488275421109):
        classes[20] += 1
    elif (r <= 52682414954421):
        classes[21] += 1
    else:
        classes[22] += 1

for n in range(22, -1, -1):
    print(classlist[n],": ",classes[n], sep = "")
