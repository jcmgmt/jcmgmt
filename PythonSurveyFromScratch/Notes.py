import mod_questionQuery #imports variables from separate Python script
from mod_questionQuery import * 

import mod_surveyloop #imports variables from separate Python script
from mod_surveyloop import startingQuestion

import os

isQ = dict_questions[catname][1][currentquestion]["qlevel"]
nextTQ = f"{catname}{(str(qlevel + 1).zfill(6))}"
nextSQ = f"{catname}{(str(qlevel + 100).zfill(6))}"
nextPQ = f"{catname}{(str(qlevel + 10000).zfill(6))}"

def ifpq():
    if nextPQ in dict_questions[catname][1].keys():
        currentquestion = nextPQ
    else:
        search_item = catname
        for index, name in enumerate(listOfCategories):
            if name == search_item:
        # Check if the next index exists to avoid an out-of-range error
                if index + 1 < len(listOfCategories):
            # Update currentquestion based on the next category in the list
                    currentquestion = f"{listOfCategories[index + 1]}000000"
                else:
                    print("Reached the end of the list. No more categories.")
        break

def ifsq():
    if nextSQ in dict_questions[catname][1].keys():
        currentquestion = nextSQ
    else:
        ifpq()

def iftq():
    if nextTQ in dict_questions[catname][1].keys():
        currentquestion = nextTQ
    elif nextSQ in dict_questions[catname][1].keys():
        ifsq()
    else:
        ifpq()

def YesAnswer():
        if isQ == "Title":
            ifpq()
            print(currentquestion)
        elif isQ == "Primary":
            ifsq()
            print(currentquestion)
        elif isQ == "Secondary":
            iftq()
            print(currentquestion)
        elif isQ == "Tertiary":
            iftq()
            print(currentquestion)
        else:
            print("Invalid Option")
            print(currentquestion)

def NoAnswer():
    if isQ == "Primary":
        ifpq()
    elif isQ == "Secondary":
        ifpq()
    elif isQ == "Tertiary":
        ifsq()
    else:
        print("Invalid Option")

while dict_questions[catcurrentname][1][currentquestion]["qlevel"] == "Title":
    goToNextPQ()  # Call the function to update 'currentquestion'
    continue
else:
    pass


print("ME")