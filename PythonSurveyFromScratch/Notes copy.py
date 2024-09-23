import mod_questionQuery #imports variables from separate Python script
from mod_questionQuery import * 

import mod_surveyloop #imports variables from separate Python script
from mod_surveyloop import *

import os

# os.chdir('/Users/jcmgmt/Documents/GitHub/jcmgmt/PythonSurveyFromScratch')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

ascii_art = r"""
  __  __           _         _____                           __  __       _        _      
 |  \/  |         (_)       / ____|                         |  \/  |     | |      (_)     
 | \  / |_   _ ___ _  ___  | |     __ _ _ __ ___  ___ _ __  | \  / | __ _| |_ _ __ ___  __
 | |\/| | | | / __| |/ __| | |    / _` | '__/ _ \/ _ \ '__| | |\/| |/ _` | __| '__| \ \/ /
 | |  | | |_| \__ \ | (__  | |___| (_| | | |  __/  __/ |    | |  | | (_| | |_| |  | |>  < 
 |_|  |_|\__,_|___/_|\___|  \_____\__,_|_|  \___|\___|_|    |_|  |_|\__,_|\__|_|  |_/_/\_\
 -----------------------------------------------------------------------------------------
"""

# Assuming mod_questionQuery contains listOfCategories and dict_questions
# from mod_questionQuery import listOfCategories, dict_questions

startingQuestion = f"{listOfCategories[0]}000000"

currentquestion = startingQuestion  # Initialize question id
catcurrentname = currentquestion[:-6]  # Category name
qlevel = int(currentquestion[-6:])  # Question level (integer)



# Main Loop
while True:
    questionInterface()
    
    try:
        option = input("Enter your option: ")

        if option.lower() == "exit":
            break

        elif option == "1":  
            YesAnswer()

        elif option == "2":  
            NoAnswer()

        else:
            print(f"You entered: {option}")

    except ValueError:
        print("Please provide a valid input.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program!")
