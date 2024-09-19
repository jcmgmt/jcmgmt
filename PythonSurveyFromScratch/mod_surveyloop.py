import mod_questionQuery #imports variables from separate Python script
from mod_questionQuery import * 

def surveyloop():
    currentquestion = startingQuestion

    catnamee = str(startingQuestion[:-6])
    qlevel = int(startingQuestion[-6:])
    tlvl = 1
    slvl = 100
    plvl = 10000

    print(dict_questions[catnamee][1].keys())
    
    while True:
        user_input = input("Enter '1', '2', 'text', a custom string, or 'exit' to quit: ").lower()
    
        if user_input == "exit":
            print("Exiting the loop.")
            break

        elif user_input == "1": #If the answer is True
            # Then if the question is primary level:
            # IF THEN
                #if the question is secondary level:
                #IF THEN
                    #if the question is tertiary level:
                    #IF THEN
            currentquestion = f"{catnamee}{(str(qlevel + plvl).zfill(6))}" 
            if currentquestion in dict_questions[catnamee][1].keys():
                currentquestion = dict_questions[catnamee][1].keys()
                print("True")
            else:
                print("Does Not Exist")
                #print(f"{catnamee}{(str(qlevel + plvl).zfill(6))}")

        elif user_input == "2":
            currentquestion = f"{catnamee}{qlevel}"
            print(currentquestion) 

        else:
            print(f"You entered a custom string: {user_input}")

surveyloop()
