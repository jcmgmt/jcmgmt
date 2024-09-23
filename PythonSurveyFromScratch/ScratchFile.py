import math
startingQuestion = f"{listOfCategories[0]}000000"
currentquestion = startingQuestion          # "XX[X]000000"

while True:
    global qlevel, catcurrentname, qlevel, nextTQ, nextSQ, nextPQ
    
    catcurrentname = currentquestion[:-6]   # XX[X]...
    qlevel = int(currentquestion[-6:])      # ...010101

    while dict_questions[catname][1][currentquestion]["qlevel"] == "Title":
        currentquestion = nextPQ
    else:
        pass

    nextTQ = f"{catcurrentname}{str(qlevel + 1).zfill(6)}"
    nextSQ = f"{catcurrentname}{str(math.floor((qlevel + 100) / 100) * 100).zfill(6)}"
    nextPQ = f"{catcurrentname}{str(math.floor((qlevel + 10000) / 10000) * 10000).zfill(6)}"
    nextcat = f"{listOfCategories[(listOfCategories.index(catcurrentname)) + 1]}000000"

    questionInterface()

    try:
        option = input("Enter your option: ")

        if option.lower() == "exit":
            break

        elif option == "1":  # Handle Yes Answer

            if qlevel == "Title":
                if nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Primary":
                if nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Secondary":
                if nextTQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextTQ                
                elif nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Tertiary":
                if nextTQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextTQ                
                elif nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")


        elif option == "2":  # Handle No Answer

            if qlevel == "Title":
                if listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Primary":
                if nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Secondary":
                if nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Tertiary":
                if nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

        else:

            if qlevel == "Title":
                if nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Primary":
                if nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Secondary":
                if nextTQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextTQ                
                elif nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

            elif qlevel == "Tertiary":
                if nextTQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextTQ                
                elif nextSQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextSQ
                elif nextPQ in dict_questions[catcurrentname][1]:
                    currentquestion = nextPQ
                elif listOfCategories.index(catcurrentname) + 1 < len(listOfCategories):
                    currentquestion = nextcat
                else:
                    print("You've reached the end of the survey!")

    except ValueError:
        print("Please provide a valid input.")
        input("Press Enter to continue...")

clear_screen()
print("Thanks for using this program!")