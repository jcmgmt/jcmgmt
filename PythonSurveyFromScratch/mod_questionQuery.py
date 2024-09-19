from collections import OrderedDict

# Initialize a combined dictionary to store the final structure
dict_questions = {}

# Initialize a list to store unique catIDs in the order they appear
listOfCategories_list = []

# Open the text file in read mode
with open('Questions.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        
        # Assign each part to a variable (default values for missing parts)
        Qid = parts[0] if len(parts) > 0 else ''
        qlevel = parts[1] if len(parts) > 1 else ''
        tiername = parts[2] if len(parts) > 2 else ''
        catID = parts[3] if len(parts) > 3 else ''
        catname = parts[4] if len(parts) > 4 else ''
        category = parts[5] if len(parts) > 5 else ''
        question1 = parts[6] if len(parts) > 6 else ''
        question2 = parts[7] if len(parts) > 7 else ''
        question3 = parts[8] if len(parts) > 8 else ''
        question = parts[9] if len(parts) > 9 else ''
        q_type = parts[10] if len(parts) > 10 else ''
        if_trueortext = parts[11] if len(parts) > 11 else ''
        advice_iftrueortext = parts[12] if len(parts) > 12 else ''
        if_false = parts[13] if len(parts) > 13 else ''
        advice_iffalse = parts[14] if len(parts) > 14 else ''
        did_you_know = parts[15] if len(parts) > 15 else ''
        weblinks = parts[16] if len(parts) > 16 else ''
        
        # Create a dictionary for the question details
        row_dict = {
            "id": Qid,
            "qlevel": qlevel,
            "tier": tiername,
            "catID": catID,
            "catname": catname,
            "cat": category,
            "q1": question1,
            "q2": question2,
            "q3": question3,
            "q": question,
            "type": q_type,
            "if_true_text": if_trueortext,
            "adv_true": advice_iftrueortext,
            "if_false": if_false,
            "adv_false": advice_iffalse,
            "did_know": did_you_know,
            "links": weblinks
        }

        # Add catID and catname to the combined dictionary
        if catID:
            if catID not in dict_questions:
                dict_questions[catID] = (catname, {})  # Initialize with category name and empty dictionary
                # Add the catID to the list if it's not already present
                if catID not in listOfCategories_list:
                    listOfCategories_list.append(catID)
            
            # Add the question data to the appropriate catID
            dict_questions[catID][1][Qid] = row_dict

# Convert the list of catIDs to a tuple
listOfCategories = tuple(listOfCategories_list)

# Output the final tuple
# print(listOfCategories)  # Example output: ('IN', 'ED', 'ML')

# You can now access the catIDs using the index, e.g.
# print(listOfCategories[0])  # 'IN'
# print(listOfCategories[1])  # 'ED'

# --------------------------------

# print(dict_questions["IN"][1].keys()) # searches nested dictionaries for all keys: INXXXXXX
# print(dict_questions["IN"][1].values()) # searches nested dictionaries for all values: 'tier', 'cat', etc.
# print(dict_questions[listOfCategories[0]][1].keys())


"""def check():
    # Check if "PPT000000" is in the dictionary under the first category in listOfCategories
    if "PPT00000" in dict_questions[listOfCategories[0]][1].keys():
        return "True"
    else:
        return "False"

# Call the check function and assign the result
result = check()

# Print the result
print(result)
"""