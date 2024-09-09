import os

from collections import OrderedDict

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
print(question_dict["ED000000"]["catname"])  # Access the catname for a specific question ID
print(cat_dict)  # Print the unique catID-catname pairs in order

catID_list = list(cat_dict.keys())[1]
print(catID_list)

# SCRIPTS THAT ARE NOT YET WORKING

### Current Question formula
# Initialize the starting point for currentquestion using the first catID
first_catID = list(cat_dict.keys())[0]  # Get the first catID from cat_dict

# Initialize level variables
level_1 = 0
level_2 = 0
level_3 = 0

# Construct the initial currentquestion (e.g., "IN000000")
currentquestion = f"{first_catID}{level_1:02}{level_2:02}{level_3:02}"

# Function to generate next_tq, next_sq, and next_pq
def generate_next_question_ids(catID, level_1, level_2, level_3):
    next_tq = f"{catID}{level_1:02}{level_2:02}{level_3 + 1:02}"
    next_sq = f"{catID}{level_1:02}{level_2 + 1:02}{level_3:02}"
    next_pq = f"{catID}{level_1 + 1:02}{level_2:02}{level_3:02}"
    return next_tq, next_sq, next_pq

# Now generate the next_tq, next_sq, next_pq based on current values
next_tq, next_sq, next_pq = generate_next_question_ids(first_catID, level_1, level_2, level_3)

# Example of how to check and update currentquestion based on the existence of next questions in question_dict
if next_tq in question_dict:
    currentquestion = next_tq
elif next_sq in question_dict:
    currentquestion = next_sq
elif next_pq in question_dict:
    currentquestion = next_pq
else:
    # If none are found, go to the next catID
    next_catID = get_next_catID(first_catID)  # Function to get the next catID
    if next_catID:
        currentquestion = f"{next_catID}000000"  # Reset to the first level of the new catID
    else:
        currentquestion = None  # No more questions left

# Example usage:
# current_question = find_next_question("IN", 2, 1, 1)
# if current_question:
#     print(question_dict[current_question]["q"])
# else:
#     print("No more questions available.")


# Get Question Level (Question 1, Question 2, or Question 3)(Primary, Secondary, Teriary levels)
def get_qlevel(question1, question2, question3):
    if question1 == "":
        if question2 == "":
            if question3 == "":
                print("Next Section!")
                return None  # or return a specific value if needed
            else:
                return "Tertiary"
        else:
            return "Secondary"
    else:
        return "Primary"
    
### Branch Logic scripts for Yes/No answers

### BRANCH LOGIC FOR YES/NO QUESTIONS

# Generate the next tq, sq, and pq question IDs
next_tq = f"{catID}{level_1:02}{level_2:02}{level_3 + 1:02}"
next_sq = f"{catID}{level_1:02}{level_2 + 1:02}{level_3:02}"
next_pq = f"{catID}{level_1 + 1:02}{level_2:02}{level_3:02}"

# Helper function to find the next catID in cat_dict
def get_next_catID(current_catID):
    cat_keys = list(cat_dict.keys())  # Get list of catIDs
    if current_catID in cat_keys:
        current_index = cat_keys.index(current_catID)
        if current_index + 1 < len(cat_keys):  # Check if there's a next catID
            return cat_keys[current_index + 1]
    return None  # No next catID, return None

# if_pq block
if next_pq in question_dict:
    currentquestion = next_pq
else:
    next_catID = get_next_catID(catID)  # Get the next catID if available
    if next_catID:
        # Generate the first pq for the next catID
        currentquestion = f"{next_catID}01{0:02}{0:02}"
    else:
        currentquestion = None  # No more questions available

# if_sq block
if next_sq in question_dict:
    currentquestion = next_sq
else:
    # Fallback to if_pq if next_sq doesn't exist
    if next_pq in question_dict:
        currentquestion = next_pq
    else:
        next_catID = get_next_catID(catID)  # Get the next catID if available
        if next_catID:
            currentquestion = f"{next_catID}01{0:02}{0:02}"
        else:
            currentquestion = None  # No more questions available

# if_tq block
if next_tq in question_dict:
    currentquestion = next_tq
else:
    # Fallback to if_sq if next_tq doesn't exist
    if next_sq in question_dict:
        currentquestion = next_sq
    else:
        if next_pq in question_dict:
            currentquestion = next_pq
        else:
            next_catID = get_next_catID(catID)  # Get the next catID if available
            if next_catID:
                currentquestion = f"{next_catID}01{0:02}{0:02}"
            else:
                currentquestion = None  # No more questions available

"""
### JUSTIN'S BRANCH LOGIC NOTES
next_tq = f"{catID}+{level_1}+{level_2}+{level_3 + 1}"
next_sq = ({catID}+{level_1}+{level_2 + 1}+{level_3})
next_pq = ({catID}+{level_1 + 1}+{level_2}+{level_3})

if_pq = 
    if next_pq in question_dict
        currentquestion = next_pq
    else: # catID_list[0 + 1]

if_sq = 
    if next_sq in question_dict
        currentquestion = next_sq
    else: if_pq

if_tq =
    if next_tq in question_dict
        currentquestion = next_tq
    else: if_sq
"""
# END SECOND SECTION"""