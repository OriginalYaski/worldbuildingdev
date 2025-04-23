import sys
import Classgen
import ClassBuildUp
import ContinentClassSetup

operation = input(str("Start from generating class spread? (No levels) :"))

if operation == "Cancel":
    print("Okay, see you around!")
    sys.exit(0)

filename = ""

if operation == "Y":
    filename = Classgen.main()

    if filename == "Cancel":
        print("Okay, see you around!")
        sys.exit(0)

    operation2 = input(str("Continue to PC level generation? :"))

else:
    filename = input(str("Okay, what file would you like to load? :"))

    if filename == "Cancel":
        print("Okay, see you around!")
        sys.exit(0)

    operation2 = input(str("Would you like to generate PC-level spread? :"))



if operation2 == "Y":
    status = ClassBuildUp.main(filename)

    if status == "Cancel":
        print("Okay, see you around!")
        sys.exit(0)

    operation3 = input(str("Continue to adding NPC levels? :"))

elif operation2 == "Cancel":
    print("Okay, see you around!")
    sys.exit()

#If they DID generate a new PC class spread but NOT a level spread, then we cannot continue
elif operation == "Y":
    print("End of operation. See you later!")
    sys.exit(0)

else:
    operation3 = input(str("Seems like you're far along. Would you like to generate NPC levels? :"))



if operation3 == "Y":
    ContinentClassSetup.main(filename)


print("That's all there is for now. Check again later!")
