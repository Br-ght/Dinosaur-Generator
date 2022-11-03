import random
import json

#stores the open version of the json that contains the dinosaurs/descriptions as f
f = open('dinosaurs.json')
#loads the json as the variable data which makes data a dictionary (this also enables me to access the json objects)
data = json.load(f)
#modeSwitch will determine whether or not the the matches (if found) will print a random match or print dinosaur that matches the user input
modeSwitch = int(input("Please choose how you'd like your results outputted: \n[1.] Random matches \t[2.] All matches \n"))
#put it in the while loop so it'll run unless interrupted by keyboard
while True:
    #create an empty dictionary to store all matching values for the random choice option. This will store the names as keys and descriptions as values.
    found = dict()
    #get the user input. The lsit will be checked to find anything that starts with whatever the user input is
    user_dino = input("\nEnter a dinosaur or letter: ").lower()
    #if the userinput isn't alphabetical then it will tell you it's not valid (line 31)
    if (user_dino.isalpha()):
        for x in range(0, len(data)-1):
            #selecting each name object and description object from the json 
            current_name = data[x]['Name']
            current_desc = data[x]['Description']
            #check if the selected name object starts with the user input
            if (current_name.lower().startswith(user_dino)):
                #add any matching values to the dictionary
                found.update({current_name : current_desc})
                #if the mode is switched to all matches then it'll print when a match is found until the loop stops
                if (modeSwitch == 2):
                    print(f'\n{current_name} - {current_desc}')
        #if nothing is added to found and it remains empty that means no matches were found in the json (so the dinosaur probably doesn't exist)
        if (not bool(found)):
            print("Sorry that doesn't exit")
        #if found isn't empty and the mode is on random then it'll select a random match and print it with its description
        elif (bool(found) and modeSwitch == 1):
            selected_dino = random.choice(list(found.keys()))
            print(f'\n{selected_dino} - {found[selected_dino]}')
    #see line 15
    else:
        print("\nThat is not a valid character.")

