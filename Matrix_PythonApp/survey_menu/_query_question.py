import os

# Initialize an empty list to store lists of delimiters
data_dict = {}

# Open the text file in read mode
with open('Questions.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Split the line into components using tab as the delimiter
        parts = line.strip().split('\t')
        
        # Assign each part to a separate variable
        Qid = parts[0]
        level_1 = int(parts[1])
        level_2 = int(parts[2])
        level_3 = int(parts[3])
        tiername = parts[4]
        catID = parts[5]
        catname = parts[6]
        category = parts[7] if len(parts) > 7 else ''  # Handling cases where title might be missing
        question1 = parts[8] if len(parts) > 8 else ''  # Handling cases where question1 might be missing
        question2 = parts[9] if len(parts) > 9 else ''  # Handling cases where question2 might be missing
        question3 = parts[10] if len(parts) > 10 else ''  # Handling cases where question3 might be missing
        question = parts[11]
        type = parts[12]
        if_trueortext = parts[13]
        advice_iftrueortext = parts[14]
        if_false = parts[15]
        advice_iffalse = parts[16]
        did_you_know = parts[17]
        weblinks = parts[18]
        
        # Create a list of the variables
        row_dict = {
            "id": Qid,                              # Question ID
            "lvl1": level_1,                        # IDxx0000
            "lvl2": level_2,                        # ID00xx00
            "lvl3": level_3,                        # ID0000xx
            "tier": tiername,                       # Tier Name of one of the ten tiers
            "catID": catID,                         # Category ID (IN, PD, ST, etc.)
            "cat": category,                        # Title 
            "catname": catname,                     # Category Name
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
        data_dict[Qid] = row_dict
    
    #AARON'S SUGGESTION: This is how it would work:
    # print(data_dict["IN020100"]["lvl2"] + 2)

""" SCRIPTS THAT ARE NOT YET WORKING

# Creates a sorted list of unique catIDs from data_dict
ordered_catIDs = sorted(set(row["catID"] for row in data_dict.values()))

# Current Question formula
currentquestion = data_dict.get[{catID}+{level_1}])

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
    
# Branch Logic scripts for Yes/No answers

def find_next_question(catID, lvl1, lvl2, lvl3):
    # Define possible next questions within the same category
    next_tq = f"{catID}{str(lvl1).zfill(2)}{str(lvl2).zfill(2)}{str(lvl3 + 1).zfill(2)}"
    next_sq = f"{catID}{str(lvl1).zfill(2)}{str(lvl2 + 1).zfill(2)}{str(lvl3).zfill(2)}"
    next_pq = f"{catID}{str(lvl1 + 1).zfill(2)}{str(lvl2).zfill(2)}{str(lvl3).zfill(2)}"
    
    # Check for the next tertiary question
    if next_tq in data_dict:
        return next_tq
    # Check for the next secondary question
    elif next_sq in data_dict:
        return next_sq
    # Check for the next primary question
    elif next_pq in data_dict:
        return next_pq
    else:
        # If no more questions in the current category, move to the next category
        current_index = ordered_catIDs.index(catID)
        if current_index < len(ordered_catIDs) - 1:
            # Get the first question of the next category
            next_catID = ordered_catIDs[current_index + 1]
            first_question = next(cat for cat in data_dict if data_dict[cat]["catID"] == next_catID)
            return first_question
        else:
            return None  # No more questions available

# Example usage:
# current_question = find_next_question("IN", 2, 1, 1)
# if current_question:
#     print(data_dict[current_question]["q"])
# else:
#     print("No more questions available.")


# END FIRST SECTION"""

""" #START SECOND SECTION
next_tq = f"{catID}+{level_1}+{level_2}+{level_3 + 1}"
next_sq = ({catID}+{level_1}+{level_2 + 1}+{level_3})
next_pq = ({catID}+{level_1 + 1}+{level_2}+{level_3})

if_pq = 
    if next_pq in data_dict
        currentquestion = next_pq
    else: #GO TO THE NEXT catID

if_sq = 
    if next_sq in data_dict
        currentquestion = next_sq
    else: if_pq

if_tq =
    if next_tq in data_dict
        currentquestion = next_tq
    else: if_sq
# END SECOND SECTION"""