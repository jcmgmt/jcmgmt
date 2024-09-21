isQ = dict_questions[catname][1][currentquestion]["qlevel"]

nextTQ = f"{catname}{(str(qlevel + 1).zfill(6))}"

nextSQ = f"{catname}{(str(qlevel + 100).zfill(6))}"

nextPQ = f"{catname}{(str(qlevel + 10000).zfill(6))}"

def ifpq():
    if nextPQ in dict_questions[catname][1].keys():
        currentquestion = nextPQ
    else:
        search_item = catname
        for index, name in listOfCategories:
            if name == search_item:
                currentquestion = f"{listOfCategories[index + 1]}000000"


def ifsq():
    if nextSQ in dict_questions[catname][1].keys():
        currentquestion = nextSQ
    else:
        ifpq()


def iftq():
    if nextTQ in dict_questions[catname][1].keys():
        currentquestion = nextTQ
    else:
        ifsq()



def YesAnswer():
    if isq == "Primary" and user_input == "1":
        ifsq()
    elif isq == "Secondary" and user_input == "1":
        iftq()
    elif isq == "Tertiary" and user_input == "1":
        iftq()
    else:
        print("Invalid Option")