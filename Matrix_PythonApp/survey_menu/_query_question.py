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
        level_1 = parts[1]
        level_2 = parts[2]
        level_3 = parts[3]
        tiername = parts[4]
        catID = parts[5]
        category = parts[6] if len(parts) > 6 else ''  # Handling cases where title might be missing
        question1 = parts[7] if len(parts) > 7 else ''  # Handling cases where question1 might be missing
        question2 = parts[8] if len(parts) > 8 else ''  # Handling cases where question2 might be missing
        question3 = parts[9] if len(parts) > 9 else ''  # Handling cases where question3 might be missing
        question = parts[10]
        type = parts[11]
        if_trueortext = parts[12]
        advice_iftrueortext = parts[13]
        if_false = parts[14]
        advice_iffalse = parts[15]
        did_you_know = parts[16]
        weblinks = parts[17]
        
        # Create a list of the variables
        row_dict = {
            "id": Qid,                              # Question ID
            "lvl1": level_1,                        # IDxx0000
            "lvl2": level_2,                        # ID00xx00
            "lvl3": level_3,                        # ID0000xx
            "tier": tiername,                       # Tier Name of one of the ten tiers
            "catID": catID,                         # Category ID (IN, PD, ST, etc.)
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
        data_dict[Qid] = row_dict
    
    #AARON'S SUGGESTION: This is how it would work:
    # print(data_dict["IN020100"])

# SCRIPT BEGINS HERE



