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


# To update the current question based on question levels
def update_question_levels():
    global currentquestion, qlevel
    nextTQ = f"{catcurrentname}{(str(qlevel + 1).zfill(6))}"
    nextSQ = f"{catcurrentname}{(str(qlevel + 100).zfill(6))}"
    nextPQ = f"{catcurrentname}{(str(qlevel + 10000).zfill(6))}"
    return nextTQ, nextSQ, nextPQ


# Navigate to the next Primary Question
def ifpq():
    global currentquestion, qlevel
    nextPQ = update_question_levels()[2]
    if nextPQ in dict_questions[catcurrentname][1]:
        currentquestion = nextPQ
        qlevel = int(currentquestion[-6:])  # Update qlevel after updating question
    else:
        search_item = catcurrentname
        for index, name in enumerate(listOfCategories):
            if index + 1 < len(listOfCategories):
                currentquestion = f"{listOfCategories[index + 1]}000000"
                qlevel = 0  # Reset qlevel when moving to the next category
            else:
                print("No more categories.")
                break


# Navigate to the next Secondary Question
def ifsq():
    global currentquestion, qlevel
    nextSQ = update_question_levels()[1]
    if nextSQ in dict_questions[catcurrentname][1]:
        currentquestion = nextSQ
        qlevel = int(currentquestion[-6:])  # Update qlevel after updating question
    else:
        ifpq()


# Navigate to the next Tertiary Question
def iftq():
    global currentquestion, qlevel
    nextTQ = update_question_levels()[0]
    if nextTQ in dict_questions[catcurrentname][1]:
        currentquestion = nextTQ
        qlevel = int(currentquestion[-6:])  # Update qlevel after updating question
    else:
        ifsq()


# Handle 'Yes' Answer
def YesAnswer():
    global currentquestion, isQ
    isQ = dict_questions[catcurrentname][1][currentquestion]["qlevel"]
    if isQ == "Title":
        ifpq()
    elif isQ == "Primary":
        ifsq()
    elif isQ == "Secondary":
        iftq()
    elif isQ == "Tertiary":
        iftq()
    else:
        print("Invalid Option")


# Handle 'No' Answer
def NoAnswer():
    global currentquestion
    ifpq()


# Interface for displaying the question
def questionInterface():
    clear_screen()
    skipTitle()  # Skip title questions if necessary
    print(ascii_art)
    print(f"Question: {dict_questions[catcurrentname][1][currentquestion]['q']}")
    print(f"Type: {dict_questions[catcurrentname][1][currentquestion]['type']}")
    print("[1] Yes")
    print("[2] No")
    print("[Exit] Exit")


# Skip Title Questions
def skipTitle():
    global currentquestion
    while dict_questions[catcurrentname][1][currentquestion]["qlevel"] == "Title":
        ifpq()


# Main Loop
while True:
    questionInterface()
    
    try:
        option = input("Enter your option: ")

        if option.lower() == "exit":
            break

        elif option == "1":  # Handle Yes Answer
            YesAnswer()

        elif option == "2":  # Handle No Answer
            NoAnswer()

        else:
            print(f"You entered: {option}")

    except ValueError:
        print("Please provide a valid input.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program!")
