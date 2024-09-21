import mod_questionQuery #imports variables from separate Python script
from mod_questionQuery import * 

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

########################### VARIABLE FOR header_space ###########################
# Just a variable to add space in the CLI display

header_space = r""""""

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
# -------------------------------- Getting the first item on the list

def startingQuestionid():
    return f"{listOfCategories[0]}000000"

startingQuestion = startingQuestionid()

# print(startingQuestion)

# --------------------------------

def surveyloop():
    clear_screen()
    print(ascii_art)                        # Print the ASCII art
    currentquestion = startingQuestion      # "XX[X]000000"

    catname = str(currentquestion[:-6])     # XX[X]...
    qlevel = int(currentquestion[-6:])      # ...010101
    tlvl = 1
    slvl = 100
    plvl = 10000

    # To update 'currentquestion', we can use the 'nonlocal' keyword in Python
    # Or pass 'currentquestion' as an argument if we're in a nested function
    def goToSQ():
        nonlocal currentquestion
        currentquestion = f"{catname}{(str(qlevel + slvl).zfill(6))}"

    def goToTQ():
        nonlocal currentquestion
        currentquestion = f"{catname}{(str(qlevel + tlvl).zfill(6))}"

    def goToNexttQ():
        nonlocal currentquestion
        currentquestion = f"{catname}{(str(qlevel + tlvl).zfill(6))}"

    def goToNextPQ():
        nonlocal currentquestion
        currentquestion = f"{catname}{(str(qlevel + plvl).zfill(6))}"

    def searchNextQ():
        nonlocal currentquestion 
        if currentquestion in dict_questions[catname][1].keys():
            currentquestion = dict_questions[catname][1].keys()
            print("True")
        else:
            print("Does Not Exist")
            print(currentquestion)

    # ------------------------------
    #

    #
    # ------------------------------

    # So that it doesn't get stuck on "Title" entries that have no questions, 
    # +10000 to the qlevel so that it goes to the first question of the section.
    # Use a while loop to skip over the "Title" questions.
    while dict_questions[catname][1][currentquestion]["qlevel"] == "Title":
        goToNextPQ()  # Call the function to update 'currentquestion'
        continue
    else:
        pass


    # print(dict_questions[catname][1].keys())
    print(dict_questions[catname][1][currentquestion]["q"]) #Display the current question
    # print(dict_questions["PPT"][1]["PPT010000"]["type"]) #Display a test question
    # print(dict_questions["PPT"][1]["PPT010000"]["qlevel"]) #Display a test question

    print(header_space)         # Display header space

    if dict_questions[catname][1][currentquestion]["type"] == "Boolean":
        print("[1] Yes")
        print("[2] No")
        print("[Exit] Exit")
    elif dict_questions[catname][1][currentquestion]["type"] == "String":
        print("Type your response")
        print("[Exit] Exit")
    else:
        print("Error")


    print(header_space)         # Display header space
"""
    while True:
        user_input = input("Input: ")
    
        if user_input == "exit":
            print("Exiting the loop.")
            break

        # Maybe we can do a WhileLoop for if input == "1"
        elif user_input == "1":
            if dict_questions[catname][1][currentquestion]["type"] == "Boolean" and dict_questions[catname][1][currentquestion]["qlevel"] == "Primary":
                goToSQ()
                searchNextQ()
            elif dict_questions[catname][1][currentquestion]["type"] == "Boolean" and dict_questions[catname][1][currentquestion]["qlevel"] == "Secondary":
                goToTQ()
                searchNextQ()


            # currentquestion = f"{catname}{(str(qlevel + plvl).zfill(6))}" 
                #print(f"{catnamee}{(str(qlevel + plvl).zfill(6))}")
            continue
        elif user_input == "2":
            currentquestion = f"{catname}{qlevel}"
            print(currentquestion) 

        else:
            print(f"You entered a custom string: {user_input}")

surveyloop()

"""
