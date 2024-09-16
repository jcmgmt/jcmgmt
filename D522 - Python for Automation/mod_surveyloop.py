def surveyloop():
    currentSurveyQuestion = 0  # Initialize num outside the loop to retain its value across iterations
    
    while True:
        user_input = input("Enter '1', '2', 'text', a custom string, or 'exit' to quit: ").lower()
    
        if user_input == "exit":
            print("Exiting the loop.")
            break
        elif user_input == "1":
            currentSurveyQuestion += 1
            print(f"Current num: {currentSurveyQuestion}")
        elif user_input == "2":
            currentSurveyQuestion += 2
            print(f"Current num: {currentSurveyQuestion}")
        else:
            print(f"You entered a custom string: {user_input}")

surveyloop()

"""
fav_numbers = {'id': 0, 'name': "zero"}
for name, number in fav_numbers.items():
 print(name + ' loves ' + str(number))
"""