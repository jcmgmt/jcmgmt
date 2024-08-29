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
        category = parts[4]
        catID = parts[5]
        title = parts[6] if len(parts) > 6 else ''  # Handling cases where title might be missing
        question1 = parts[7] if len(parts) > 7 else ''  # Handling cases where question1 might be missing
        question2 = parts[8] if len(parts) > 8 else ''  # Handling cases where question2 might be missing
        question3 = parts[9] if len(parts) > 9 else ''  # Handling cases where question3 might be missing
        
        # Create a list of the variables
        row_dict = {
            "id": Qid,
            "lvl1": level_1,
            "lvl2": level_2, 
            "lvl3": level_3,
            "category": category,
            "catID": catID,
            "title": title,
            "q1": question1,
            "q2": question2,
            "q3": question3
        }
                
        # Append the list to the data_list
        data_dict[Qid] = row_dict
    
    #AARON'S SUGGESTION: This is how it would work:
    print(data_dict["IN010000"]["category"])

# Now, data_list contains lists of the seven variables for each row
# You can access the variables for a specific row like this:
#print(data_list[0])  # Output: ['IN000000', '00', '00', '00', 'Pre-Production', 'IN', 'In-Take Initial Questions', '']
#print(data_list[6])  # Output: ['IN010000', '01', '00', '00', 'Pre-Production', 'IN', '', 'Can you tell me about your background and experience as an artist?']

#You can access specific variables within a row using their index in the list. For example, data_list[0][1] would give you 00 for the first row's level_1 value.
#print(data_list[0][6])