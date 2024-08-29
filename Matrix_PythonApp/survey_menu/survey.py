import _query_question  #imports variables from separate Python script

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
header_space = r"""
"""

def questionInterface():
    clear_screen()
    print(ascii_art)  # Print the ASCII art
    print(header_space)
    print("[1] Survey")
    print("[2] People and Careers")
    print("[3] Tools in the Business")
    print("[0] Exit")


# Main program loop
while True:
    questionInterface()
    
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 0:
        break
    elif option == 1:
        surveyMenu()
    elif option == 2:
        peopleAndCareersMenu()
    elif option == 3:
        toolsInBusinessMenu()
    else:
        print("Invalid option. Please try again.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program. Take care!")
