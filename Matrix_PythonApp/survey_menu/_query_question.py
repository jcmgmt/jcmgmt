import os
from collections import OrderedDict

########################### CREATE DICTIONARIES FROM QUESTION TEXT DOCUMENT ###########################

# Initialize an empty list to store lists of delimiters
question_dict = {}

# Initialize an empty ordered dictionary for cat_dict to store unique catID-catname pairs
cat_dict = OrderedDict()

# Open the text file in read mode
with open('Questions.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Split the line into components using tab as the delimiter
        parts = line.strip().split('\t')
        
        # Assign each part to a separate variable
        Qid = parts[0] if len(parts) > 0 else ''
        level_1 = int(parts[1]) if len(parts) > 1 else 0  # Default to 0 if missing
        level_2 = int(parts[2]) if len(parts) > 2 else 0
        level_3 = int(parts[3]) if len(parts) > 3 else 0
        tiername = parts[4] if len(parts) > 4 else ''
        catID = parts[5] if len(parts) > 5 else ''
        catname = parts[6] if len(parts) > 6 else ''
        category = parts[7] if len(parts) > 7 else ''
        question1 = parts[8] if len(parts) > 8 else ''
        question2 = parts[9] if len(parts) > 9 else ''
        question3 = parts[10] if len(parts) > 10 else ''
        question = parts[11] if len(parts) > 11 else ''
        type = parts[12] if len(parts) > 12 else ''
        if_trueortext = parts[13] if len(parts) > 13 else ''
        advice_iftrueortext = parts[14] if len(parts) > 14 else ''
        if_false = parts[15] if len(parts) > 15 else ''
        advice_iffalse = parts[16] if len(parts) > 16 else ''
        did_you_know = parts[17] if len(parts) > 17 else ''
        weblinks = parts[18] if len(parts) > 18 else ''

        # Add catID and catname to cat_dict if they are not empty and unique
        if catID and catname and catID not in cat_dict:
            cat_dict[catID] = catname

        # Create a list of the variables
        row_dict = {
            "id": Qid,                              # Question ID
            "lvl1": level_1,                        # IDxx0000
            "lvl2": level_2,                        # ID00xx00
            "lvl3": level_3,                        # ID0000xx
            "tier": tiername,                       # Tier Name of one of the ten tiers
            "catID": catID,                         # Category ID (IN, PD, ST, etc.)
            "catname": catname,                     # Category name (added)
            "cat": category,                        # Title
            "q1": question1,                        # Primary Question (pQ)
            "q2": question2,                        # Secondary Question (sQ)
            "q3": question3,                        # Tertiary Question (tQ)
            "q": question,                          # What is the question being asked?
            "type": type,                           # Boolean or string?
            "if_true_text": if_trueortext,          # What to do when value is true
            "adv_true": advice_iftrueortext,        # Text provided upon response when the value is true or string is provided
            "if_false": if_false,                   # What to do when value is false
            "adv_false": advice_iffalse,            # Text provided upon response when the value is false
            "did_know": did_you_know,               # Text provided during question prompt for reader's awareness
            "links": weblinks                       # Text provided to share links
        }

        # Append the list to the data_list
        question_dict[Qid] = row_dict

# Example: Accessing values from question_dict and cat_dict
print(question_dict.get("ED000000", {}).get("catname", "Not found"))  # Access the catname for a specific question ID
print(cat_dict)  # Print the unique catID-catname pairs in order

########################### SELECTS THE FIRST QUESTION TO START THE SURVEY ###########################
# This configures the variable "currentquestion" to start with the first line item & disctionary key in the question_dict dictionary. 
# Essentially, this should start with "IN000000". Once the survey begins, the resulting "Yes/No" questions will guide the survey moving forward.

# Initialize the starting point for currentquestion using the first line item & dictionary key in the question_dict dictionary
first_catID = list(cat_dict.keys())[0]  # Get the first catID from cat_dict

# Initialize level variables
level_1 = 0
level_2 = 0
level_3 = 0

# Construct the initial qID (e.g., "IN000000")
initial_qID = f"{first_catID}{level_1:02}{level_2:02}{level_3:02}"

# Retrieve the question text for the initial qID
currentquestion = question_dict.get(initial_qID, {}).get('q', 'No question found')

########################### FUNCTION TO GENERATE NEXT QUESTION IDs ###########################

def generate_next_question_ids(catID, level_1, level_2, level_3):
    next_tq = f"{catID}{level_1:02}{level_2:02}{level_3 + 1:02}"
    next_sq = f"{catID}{level_1:02}{level_2 + 1:02}{level_3:02}"
    next_pq = f"{catID}{level_1 + 1:02}{level_2:02}{level_3:02}"
    return next_tq, next_sq, next_pq

# Generate the next_tq, next_sq, next_pq based on current values
next_tq, next_sq, next_pq = generate_next_question_ids(first_catID, level_1, level_2, level_3)

########################### FUNCTION TO GET NEXT CATID ###########################

def get_next_catID(current_catID):
    cat_keys = list(cat_dict.keys())  # Get list of catIDs
    if current_catID in cat_keys:
        current_index = cat_keys.index(current_catID)
        if current_index + 1 < len(cat_keys):  # Check if there's a next catID
            return cat_keys[current_index + 1]
    return None  # No next catID, return None

########################### BRANCH LOGIC FOR QUESTION NAVIGATION ###########################
# This is used when an answer is selected  in the survey.
# Essentially, it checks what level the "currentquestion" value is, performs math to 
# update the "currentquestion" variable, and then searches the dictionary with the newly updated value.

# Update currentquestion based on the existence of next questions in question_dict
if next_tq in question_dict:
    currentquestion = question_dict[next_tq].get('q', 'No question found')
elif next_sq in question_dict:
    currentquestion = question_dict[next_sq].get('q', 'No question found')
elif next_pq in question_dict:
    currentquestion = question_dict[next_pq].get('q', 'No question found')
else:
    # If none are found, go to the next catID
    next_catID = get_next_catID(first_catID)  # Function to get the next catID
    if next_catID:
        currentquestion = question_dict.get(f"{next_catID}000000", {}).get('q', 'No question found')  # Reset to the first level of the new catID
    else:
        currentquestion = 'No more questions available'

########################### VARIABLE FOR "isq" ###########################
# This variable simply displays the result from the 'get_qlevel' function.
# It should display the "Primary", "Secondary", or "Tertiary" text.

def get_qlevel(currentquestion):
    q1 = currentquestion.get('q1', '')
    q2 = currentquestion.get('q2', '')
    q3 = currentquestion.get('q3', '')

    if q1 == "":
        if q2 == "":
            if q3 == "":
                return "Error: All question levels are empty"
            else:
                return "Tertiary"
        else:
            return "Secondary"
    else:
        return "Primary"

isq = get_qlevel(question_dict.get(initial_qID, {}))  # This should be set to "Primary", "Secondary", or "Tertiary"
# option = 1     # This is the user's response option

# Define variables for the actions
ifsq = "Perform action for Primary question"
iftq = "Perform action for Secondary or Tertiary question"

# Configure actions based on isq and option
option = 1  # Example user response
if isq == "Primary" and option == 1:
    result = ifsq
elif isq in ["Secondary", "Tertiary"] and option == 1:
    result = iftq
else:
    result = "No action taken or invalid input"

# Output the result for debugging or further processing
print(result)
