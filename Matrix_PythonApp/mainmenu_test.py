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
"""

def mainMenu():
    clear_screen()
    print(ascii_art)  # Print the ASCII art
    print("[1] Survey")
    print("[2] People and Careers")
    print("[3] Tools in the Business")
    print("[0] Exit")

def surveyMenu():
    while True:
        clear_screen()
        print(ascii_art)  # Print the ASCII art
        print("[1] Start at beginning of survey")
        print("[2] Start at a specific section")
        print("[3] Search for questions using a keyword")
        print("[0] Return to main menu")
        
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 0:
            break
        elif option == 1:
            print("(Launches Survey from beginning)")
            input("Press Enter to continue...")
        elif option == 2:
            print("(Displays a menu of the Section Headers as selectable options to start survey at.)")
            input("Press Enter to continue...")
        elif option == 3:
            print("(Haven't figured this part out yet. Create a python dictionary that contains keywords from the Google Sheet? Should I even have this as an option?)")
            input("Press Enter to continue...")
        else:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")

def peopleAndCareersMenu():
    while True:
        clear_screen()
        print(ascii_art)  # Print the ASCII art
        print("[1] Navigate by Category")
        print("[2] Search by Keyword")
        print("[0] Return to main menu")
        
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 0:
            break
        elif option == 1:
            print("(Displays a menu of the Section Headers as selectable options from the 'People and Careers' document)")
            input("Press Enter to continue...")
        elif option == 2:
            print("(Haven't figured this part out yet. Collect keywords from 'People and Careers' document & somehow add them as variables tied to each career line?)")
            input("Press Enter to continue...")
        else:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")

def toolsInBusinessMenu():
    while True:
        clear_screen()
        print(ascii_art)  # Print the ASCII art
        print("[1] Navigate by Category")
        print("[2] Search by Keyword")
        print("[0] Return to main menu")
        
        try:
            option = int(input("Enter your option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 0:
            break
        elif option == 1:
            print("(Displays a menu of the Section Headers as selectable options from the 'Tools in the Business' document)")
            input("Press Enter to continue...")
        elif option == 2:
            print("(Haven't figured this part out yet. Collect keywords from 'Tools in the Business' document & somehow add them as variables tied to each career line?)")
            input("Press Enter to continue...")
        else:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")

def option3():
    print("Option 3 has been called.")

# Main program loop
while True:
    mainMenu()
    
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
