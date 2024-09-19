#1. Nested Decicions: The Adventure Game

#Task 1: Code Correction
#Task 2: Setting the Scene
#Task 2: Default Path

#Notes about assignment for instructor:
#I see that the pass statement is unnessary but I wanted a statement to be left if the input was invalid

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
        print("Check your typing, invalid entry.")
elif place == "cave":
    action = input("Would you like to (light a torch) or (proceed in the dark)?")
    if action =="light a torch":
        print("You find a hidden treasure! Lighting a torch was worth it after all, wasn't it?")
    elif action == "proceed in the dark":
        print("In the absence of light, it is you who must light up the darkness. Follow your heart, you have chosen intuition as your light.")
    else:
        pass
        print("Check your typing, invalid entry.")