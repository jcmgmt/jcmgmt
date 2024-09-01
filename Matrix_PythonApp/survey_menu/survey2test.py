"""
TRY WORKING THIS SCRIPT WHEN YOU CAN. SEE IF THIS WORKS FOR YOU.

"""
import _query_question  #imports variables from separate Python script
from _query_question import * 

#Reference List:
            # "id"              # Question ID
            # "lvl1"            # IDxx0000
            # "lvl2"            # ID00xx00
            # "lvl3"            # ID0000xx
            # "tier"            # Tier Name of one of the ten tiers
            # "catID"           # Category ID (IN, PD, ST, etc.)
            # "cat"             # Title 
            # "q1"              # Primary Question (pQ)
            # "q2"              # Secondary Question (sQ)
            # "q3"              # Tertiary Question (tQ)
            # "q"               # What is the question being asked?
            # "type"            # Boolean or string? 
            # "if_true_text"    # What to do when value is true
            # "adv_true"        # Text provided upon response when the value is true or string is provided
            # "if_false"        # What to do when value is false
            # "adv_false"       # Text provided upon response when the value is false
            # "did_know"        # Text provided during question prompt for reader's awareness
            # "links"           # Text provided to share links

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define the ASCII art as a string
ascii_art = r"""
  __  __           _         _____                           __  __       _        _      
 |  \/  |         (_)       / ____|                         |  \/  |     | |      (_)     
 | \  / |_   _ ___ _  ___  | |     __ _ _ __ ___  ___ _ __  | \  / | __ _| |_ _ __ ___  __
 | |\/| | | | / __| |/ __| | |    / _` | '__/ _ \/ _ \ '__| | |\/| |/ _` | __| '__| \ \/ /
 | |  | | |_| \__ \ | (__  | |___| (_| | | |  __/  __/ |    | |  | | (_| | |_| |  | |>  < 
 |_|  |_|\__,_|___/_|\___|  \_____\__,_|_|  \___|\___|_|    |_|  |_|\__,_|\__|_|  |_/_/\_\
 -----------------------------------------------------------------------------------------
"""

# Variable for header space
header_space = r""""""
def questionInterface(current_question_key):
    clear_screen()
    print(ascii_art)  # Print the ASCII art
    
    # Get the current question data
    question_data = data_dict[current_question_key]
    
    # Print the question
    print(f"Question: {question_data['q']}")
    print(header_space)
    
    # Check the type of question and display options accordingly
    if question_data["type"] == "String":
        print("[1] Type your answer")
        print("[2] Skip for now")
    else:
        print("[1] Yes")
        print("[2] No")
    
    print("[0] Exit")
    print(header_space)

# Main program loop
current_question_key = "IN020100"  # Start with the first question

while True:
    questionInterface(current_question_key)
    
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please provide a valid input.")
        continue

    if option == 0:
        break
    elif option == 1:
        # Handle the "Yes" or "Type your answer" case
        if data_dict[current_question_key]["type"] == "String":
            answer = input("Type your answer: ")
            print(f"Your answer: {answer}")
            # You can add logic to save or process the answer here
        else:
            print("if_true")
            # Implement logic for navigating to the next question
            current_question_key = determine_next_question(data_dict[current_question_key])
    elif option == 2:
        # Handle the "No" or "Skip for now" case
        if data_dict[current_question_key]["type"] == "String":
            print("Skipped.")
        else:
            print("if_false")
            # Implement logic for navigating to the next question
            current_question_key = determine_alternate_question(data_dict[current_question_key])
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program. Take care!")
