import mod_questionQuery #imports variables from separate Python script
from mod_questionQuery import * 

import os

# os.chdir('/Users/jcmgmt/Documents/GitHub/jcmgmt/PythonSurveyFromScratch')

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

startingQuestion = f"{listOfCategories[0]}000000"
# print(startingQuestion)
currentquestion = startingQuestion      # "XX[X]000000"
catcurrentname = str(currentquestion[:-6])     # XX[X]...
qlevel = int(currentquestion[-6:])      # ...010101

# To update 'currentquestion', we can use the 'nonlocal' keyword in Python
# Or pass 'currentquestion' as an argument if we're in a nested function
isQ = dict_questions[catcurrentname][1][currentquestion]["qlevel"]
nextTQ = f"{catcurrentname}{(str(qlevel + 1).zfill(6))}"
nextSQ = f"{catcurrentname}{(str(qlevel + 100).zfill(6))}"
nextPQ = f"{catcurrentname}{(str(qlevel + 10000).zfill(6))}"

def ifpq():
    if nextPQ in dict_questions[catcurrentname][1].keys():
        currentquestion = nextPQ
    else:
        search_item = catcurrentname
        for index, name in enumerate(listOfCategories):
            if index + 1 < len(listOfCategories):
                currentquestion = f"{listOfCategories[index + 1]}000000"
            else:
                print("Whelp")
            break

def ifsq():
    if nextSQ in dict_questions[catcurrentname][1].keys():
        currentquestion = nextSQ
    else:
        ifpq()

def iftq():
    if nextTQ in dict_questions[catcurrentname][1].keys():
        currentquestion = nextTQ
    elif nextSQ in dict_questions[catcurrentname][1].keys():
        ifsq()
    else:
        ifpq()
def YesAnswer():
    if isQ == "Title":
        ifpq()
        print(currentquestion)
        pass
    elif isQ == "Primary":
        ifsq()
        print(currentquestion)
        pass
    elif isQ == "Secondary":
        iftq()
        print(currentquestion)
        pass
    elif isQ == "Tertiary":
        iftq()
        print(currentquestion)
        pass
    else:
        print("Invalid Option")
        print(currentquestion)
        pass

def NoAnswer():
    if isQ == "Primary":
        ifpq()
    elif isQ == "Secondary":
        ifpq()
    elif isQ == "Tertiary":
        ifsq()
    else:
        print("Invalid Option")

def searchNextQ():
    currentquestion 
    if currentquestion in dict_questions[catcurrentname][1].keys():
        currentquestion = dict_questions[catcurrentname][1].keys()
        print("True")
    else:
        print("Does Not Exist")
        print(currentquestion)

# ------------------------------
#
def goToNextPQ():
    currentquestion = f"{catcurrentname}{(str(qlevel + 10000).zfill(6))}"
#
# ------------------------------

# --------------------------------
def questionInterface():
    clear_screen()
    skipTitle()
    print(ascii_art)                        # Print the ASCII art
    print(f"Question: {dict_questions[catcurrentname][1][currentquestion]["q"]}") #Display the current question
    #TESTING SPACE#
    print(isQ)
    # print(dict_questions[catcurrentname][1].keys())
    print(dict_questions[catcurrentname][1][currentquestion]["q"]) #Display the current question
    # print(dict_questions["PPT"][1]["PPT010000"]["type"]) #Display a test question
    # print(dict_questions["PPT"][1]["PPT010000"]["qlevel"]) #Display a test question

    if dict_questions[catcurrentname][1][currentquestion]["type"] == "Boolean":
        print("[1] Yes")
        print("[2] No")
        print("[Exit] Exit")
    elif dict_questions[catcurrentname][1][currentquestion]["type"] == "String":
        print("Type 'Yes', 'No', or enter your answer")
        print("[Exit] Exit")
    else:
        print("Error")
          
def skipTitle():
    # So that it doesn't get stuck on keys with "Title" as the qlevel, 
    # +10000 to the qlevel so that it goes to the first question of the section.
    # Use a while loop to skip over the "Title" questions.
    while dict_questions[catcurrentname][1][currentquestion]["qlevel"] == "Title":
        goToNextPQ()  # Call the function to update 'currentquestion'
        continue
    else:
        pass

while True:
    questionInterface()

    try:
        option = input("Enter your option")
    
        if option == 0:
            break
        # Maybe we can do a WhileLoop for if input == "1"
        elif option == "1":
            if dict_questions[catcurrentname][1][currentquestion]["type"] == "Boolean" or dict_questions[catcurrentname][1][currentquestion]["type"] == "String":
                YesAnswer()
            else:
                print("Error occurred at answer selection")


            # currentquestion = f"{catcurrentname}{(str(qlevel + plvl).zfill(6))}" 
                #print(f"{catcurrentnamee}{(str(qlevel + plvl).zfill(6))}")
            continue
        elif option == "2":
            currentquestion = f"{catcurrentname}{qlevel}"
            print(currentquestion) 

        else:
            print(f"You entered: {option}")

    except ValueError:
        print("Please provide a valid input.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program. Take care!")


# print("ME")
# print(f"{listOfCategories[2]}000000")
#def testLoop():
#    search_item = catcurrentname
#    for index, name in enumerate(listOfCategories):
#        if index + 1 < len(listOfCategories):
#            print(index,name)
#            print(f"{listOfCategories[index + 1]}000000")
#        else:
#            print("Whelp")
# testLoop()