from collections import OrderedDict

# Initialize a combined dictionary to store the final structure
combined_dict = {}

# Open the text file in read mode
with open('Questions.txt', 'r') as file:
    for line in file:
        parts = line.strip().split('\t')
        
        # Assign each part to a variable (default values for missing parts)
        Qid = parts[0] if len(parts) > 0 else ''
        level_1 = int(parts[1]) if len(parts) > 1 else 0
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
        
        # Create a dictionary for the question details
        row_dict = {
            "id": Qid,
            "lvl1": level_1,
            "lvl2": level_2,
            "lvl3": level_3,
            "tier": tiername,
            "catID": catID,
            "catname": catname,
            "cat": category,
            "q1": question1,
            "q2": question2,
            "q3": question3,
            "q": question,
            "type": type,
            "if_true_text": if_trueortext,
            "adv_true": advice_iftrueortext,
            "if_false": if_false,
            "adv_false": advice_iffalse,
            "did_know": did_you_know,
            "links": weblinks
        }

        # Add catID and catname to the combined dictionary
        if catID:
            if catID not in combined_dict:
                combined_dict[catID] = (catname, {})  # Initialize with category name and empty dictionary
            
            # Add the question data to the appropriate catID
            combined_dict[catID][1][Qid] = row_dict


print(combined_dict)
