"""

16.8 Practice Lab 8
Complete the python function named write_dict_to_csv that appends predefined data to an existing file config.csv using the CSV library.

Note:

There should be a newline after the last row of data per CSV library defaults.
Only the file output will be graded for this assessment, standard output will be ignored.
Print to check your work; what you print to stdout does not affect the assessment
Here is an example of the usage:

write_dict_to_csv('config.csv')
Here is an example of what the config.csv should look like when written:

device_name,ip_address
Router1,192.168.1.1
Router2,192.168.1.2

"""

import csv

def write_dict_to_csv(filename):
    # Data to be written to the CSV file
    fieldnames = ['device_name', 'ip_address']

    data = [
        {'device_name': 'Router1', 'ip_address': '192.168.1.1'},
        {'device_name': 'Router2', 'ip_address': '192.168.1.2'}
    ]

    # Write the data to the CSV file.
    # Write your code here.
    
    # Print to check your work; what you print to stdout does not affect the assessment.
    # print('\n'.join([','.join(fieldnames)] + [','.join(str(d[field]) for field in fieldnames) for d in data]))
   

# You may alter the code below to test your solution or print help documentation.
# Only the write_dict_to_csv functions file output will be graded for this assessment.
# help(help)
    
# The assessment requires the below driver code in order for Zybooks to check file ouput.
# Do not edit code below this line.
write_dict_to_csv('config.csv')