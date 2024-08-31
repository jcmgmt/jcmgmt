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
    print(data_dict["IN020100"]["lvl2"] + 2)

# SCRIPT BEGINS HERE
"""
def goto_sQ(Qid):
    # Increment lvl2 by 1
    lvl1 = int(data_dict[Qid]["lvl1"])
    lvl2 = int(data_dict[Qid]["lvl2"]) + 1
    lvl3 = int(data_dict[Qid]["lvl3"])
    
    # Concatenate catID + lvl1 + lvl2 + lvl3 to form the new ID
    new_id_lvl2 = f"{data_dict[Qid]['catID']}{lvl1:02}{lvl2:02}{lvl3:02}"
    
    # Open the text file and search for the line that matches the new concatenated ID
    with open('Questions.txt', 'r') as file:
        for line in file:
            if line.startswith(new_id_lvl2):
                # Split the line to get the parts
                parts = line.strip().split('\t')
                
                # Extract and print the question (q) value
                question = parts[10]  # Assuming the 11th part is the question
                print(question)
                break
        else:
            # If no match is found with lvl2 incremented, increment lvl1 and reset lvl2 and lvl3
            lvl1 += 1
            lvl2 = 0
            lvl3 = 0
            new_id_lvl1 = f"{data_dict[Qid]['catID']}{lvl1:02}{lvl2:02}{lvl3:02}"
            
            # Re-open the file and search again for the new ID with incremented lvl1
            with open('Questions.txt', 'r') as file:
                for line in file:
                    if line.startswith(new_id_lvl1):
                        parts = line.strip().split('\t')
                        question = parts[10]
                        print(question)
                        break
                else:
                    print(f"No question found for ID: {new_id_lvl1}")

def goto_tQ():

def next_pQ():
    
def next_sQ():

def next_pQ():
    
"""

