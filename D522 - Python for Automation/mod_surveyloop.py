def surveyloop():
    num = 0  # Initialize num outside the loop to retain its value across iterations
    
    while True:
        user_input = input("Enter '1', '2', 'text', a custom string, or 'exit' to quit: ").lower()
    
        if user_input == "exit":
            print("Exiting the loop.")
            break
        elif user_input == "1":
            num += 1
            print(f"Current num: {num}")
        elif user_input == "2":
            num += 2
            print(f"Current num: {num}")
        else:
            print(f"You entered a custom string: {user_input}")

surveyloop()
