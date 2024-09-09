import _query_question  #imports variables from separate Python script
from _query_question import * 

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

########################### VARIABLE FOR header_space ###########################
# Just a variable to add space in the CLI display

header_space = r""""""

########################### FUNCTION FOR "get_qlevel" ############################
# Function used to determine the currently visible question ('currentquestion')'s level by checking the selected questoion's dictonary keys "q1", "q2", and "q3" 
# (Result displays whether it's a "Primary", "Secondary", or "Tertiary" level question)

def get_qlevel(currentquestion):
    # Retrieve question levels from currentquestion
    q1 = currentquestion.get('q1', '')
    q2 = currentquestion.get('q2', '')
    q3 = currentquestion.get('q3', '')

    # Determine the question level based on the presence of q1, q2, and q3
    if q1 == "":
        if q2 == "":
            if q3 == "":
                return "Error: All question levels are empty"
            else:
                return "Tertiary"
        else:
            return "Secondary"
    else:
        return "Primary"

########################### FUNCTION FOR YES/NO or ENTER TEXT ############################
# This function determines whether or not to display "Yes/No" as answer options, or to display "Enter Text" instead.

def yesno_entertext(currentquestion):
    # Retrieve the type from currentquestion
    question_type = currentquestion.get("type", "")

    if question_type == "Boolean":
        print("[1] Yes")
        print("[2] No")
        try:
            option = int(input("Enter your option (1 for Yes, 2 for No): "))
            if option == 1:
                print("You selected: Yes")
            elif option == 2:
                print("You selected: No")
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif question_type == "String":
        option = input("Enter your input: ")
        print(f"You entered: {option}")

    else:
        print("Error: Unsupported question type")

########################### ASCII Header Art ###########################
# ASCII art for the survey's header

ascii_art = r"""
  __  __           _         _____                           __  __       _        _      
 |  \/  |         (_)       / ____|                         |  \/  |     | |      (_)     
 | \  / |_   _ ___ _  ___  | |     __ _ _ __ ___  ___ _ __  | \  / | __ _| |_ _ __ ___  __
 | |\/| | | | / __| |/ __| | |    / _` | '__/ _ \/ _ \ '__| | |\/| |/ _` | __| '__| \ \/ /
 | |  | | |_| \__ \ | (__  | |___| (_| | | |  __/  __/ |    | |  | | (_| | |_| |  | |>  < 
 |_|  |_|\__,_|___/_|\___|  \_____\__,_|_|  \___|\___|_|    |_|  |_|\__,_|\__|_|  |_/_/\_\
 -----------------------------------------------------------------------------------------
"""
########################### SURVEY INTERFACE DISPLAY ###########################
# The following code is used to design the CLI interface

def questionInterface():
    clear_screen()
    print(ascii_art)            # Print the ASCII art
    print(f"Current Question Level: {isq}")  # Display the current question level
    print(f"Question: {currentquestion.get('q', '')}")  # Display the current question
    print(header_space)         # Display header space
    yesno_entertext(currentquestion)  # Call the function to handle the question type
    print("[0] Exit")
    print(header_space)
    print("(INSERT 'Did You Know' key from the 'did_know' dictionary entry for currentquestion variable)")
    print(header_space)
    print("(INSERT 'Links' key from the 'links' dictionary entry for currentquestion variable)")

# Main program loop
while True:
    questionInterface()
    
    try:
        option = int(input("Enter your option: "))
        
        if option == 0:
            break
        elif option == 1:
            # Print "adv_true" value from dictionary entry for currentquestion
            # perform "if_true_text" value provided from dictionary entry for currentquestion. This should go to the next pQ, sQ, or tQ.
            #
        elif option == "TEXT":
            # Print "adv_true" value from dictionary entry for currentquestion
            # perform "if_true_text" value provided from dictionary entry for currentquestion. This should go to the next pQ, sQ, or tQ.
        elif option == 2:
            # Print "adv_false" value from dictionary entry for currentquestion
            # perform "if_false_text" value provided from dictionary entry for currentquestion. This should go to the next pQ, sQ, or tQ.
        else:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")
    
    except ValueError:
        print("Please provide a valid input.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program. Take care!")