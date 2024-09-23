import mod_questionQuery  # imports variables from separate Python script
from mod_questionQuery import * 

import os
import math

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

########################### ASCII Header Art ###########################

ascii_art = r"""
  __  __           _         _____                           __  __       _        _      
 |  \/  |         (_)       / ____|                         |  \/  |     | |      (_)     
 | \  / |_   _ ___ _  ___  | |     __ _ _ __ ___  ___ _ __  | \  / | __ _| |_ _ __ ___  __
 | |\/| | | | / __| |/ __| | |    / _` | '__/ _ \/ _ \ '__| | |\/| |/ _` | __| '__| \ \/ /
 | |  | | |_| \__ \ | (__  | |___| (_| | | |  __/  __/ |    | |  | | (_| | |_| |  | |>  < 
 |_|  |_|\__,_|___/_|\___|  \_____\__,_|_|  \___|\___|_|    |_|  |_|\__,_|\__|_|  |_/_/\_\
 -----------------------------------------------------------------------------------------
"""

# Starting question
startingQuestion = f"{listOfCategories[0]}000000"
currentquestion = startingQuestion      # "XX[X]000000"
catcurrentname = str(currentquestion[:-6])     # XX[X]...
qlevel = int(currentquestion[-6:])      # ...010101

def questionInterface():
    clear_screen()
    print(ascii_art)                        # Print the ASCII art
    print(f"Question: {dict_questions[catcurrentname][1][currentquestion]['q']}")  # Display the current question

    # Handle question type and present options
    if dict_questions[catcurrentname][1][currentquestion]["type"] == "Boolean":
        print("[1] Yes")
        print("[2] No")
        print("[Exit] Exit")
    elif dict_questions[catcurrentname][1][currentquestion]["type"] == "String":
        print("Type 'Yes', 'No', or enter your answer")
        print("[Exit] Exit")
    else:
        print("Error")

# Main loop
while True:
    catcurrentname = currentquestion[:-6]  # XX[X]...
    qlevel = int(currentquestion[-6:])     # ...010101

    # Set up the next question levels
    nextTQ = f"{catcurrentname}{str(qlevel + 1).zfill(6)}"
    nextSQ = f"{catcurrentname}{str(math.floor((qlevel + 100) / 100) * 100).zfill(6)}"
    nextPQ = f"{catcurrentname}{str(math.floor((qlevel + 10000) / 10000) * 10000).zfill(6)}"
    nextcat = f"{listOfCategories[(listOfCategories.index(catcurrentname)) + 1]}000000"

    # Handling "Title" level questions
    while dict_questions[catcurrentname][1][currentquestion]["qlevel"] == "Title":
        currentquestion = nextPQ  # Move to the next primary question

    # Display the current question interface
    questionInterface()

    try:
        option = input("Enter your option: ")

        if option.lower() == "exit":
            break

        elif option == "1":  # Handle Yes Answer

            if dict_questions[catcurrentname][1][currentquestion]["qlevel"] == "Title":
                if nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")
                    break

            elif dict_questions[catcurrentname][1][currentquestion]["qlevel"] == "Primary":
                # Check for secondary and primary level questions
                if nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")
                    break

        elif option == "2":  # Handle No Answer
            if nextPQ in dict_questions[catcurrentname][1]:
                currentquestion = nextPQ
            elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                currentquestion = nextcat
            else:
                print("You've reached the end of the survey!")
                break

    except ValueError:
        print("Please provide a valid input.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program!")
