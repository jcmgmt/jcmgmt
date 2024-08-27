## 22AUG24: Survey somewhat works, it just provides additional prompts of "(yes/no)" questions. 
# It can sortof navigate through the logical question branches dependent on the yes/no answers.

# Initialize an empty list to store dictionaries
data_list = []

# Open the text file in read mode
with open('Questions.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Split the line into components using tab as the delimiter
        parts = line.strip().split('\t')
        
        # Create a dictionary for each line in the file
        line_dict = {
            'Qid': parts[0],
            'level_1': parts[1],
            'level_2': parts[2],
            'level_3': parts[3],
            'category': parts[4],
            'catID': parts[5],
            'title': parts[6] if len(parts) > 6 else '',  # Handle cases where title might be missing
            'question1': parts[7] if len(parts) > 7 else '',  # Handle cases where question1 might be missing
            'question2': parts[8] if len(parts) > 8 else '',  # Handle cases where question2 might be missing
            'question3': parts[9] if len(parts) > 9 else ''  # Handle cases where question3 might be missing
        }
        
        # Append the dictionary to the data_list
        data_list.append(line_dict)

# Function to ask a question and branch based on the answer
def ask_question(question):
    if question is not None:  # Ensure the question exists
        answer = input(question + " (yes/no or type 'exit' to leave): ").strip().lower()
        if answer == 'exit':
            print("Exiting the survey. Thank you!")
            exit()  # Exit the survey
        if answer in ['yes', 'no']:
            return answer == 'yes'
    return None  # Indicate the question was skipped or not applicable


# Function to run the interactive survey
def run_survey(data_list):
    i = 0
    while i < len(data_list):
        # Get the current question dictionary
        question_dict = data_list[i]
        
        # Ask question1
        if ask_question(question_dict['question1']):
            # If answered yes, go to question2
            if question_dict['question2'] and ask_question(question_dict['question2']):
                # If answered yes, go to question3
                if question_dict['question3']:
                    ask_question(question_dict['question3'])
            # After answering question2 or question3, move to the next question1
        # Move to the next question1
        i += 1

# Run the survey
run_survey(data_list)
