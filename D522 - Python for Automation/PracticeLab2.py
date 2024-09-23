"""

16.2 Practice Lab 2
Complete the Python function minutes_to_hours. The function should accept an integer representing the execution time of a process in minutes, convert the value from minutes to hours, and return a float representing the execution time in hours. There are 60 minutes in an hour. The function should utilize float division and not integer division.

Only the minutes_to_hours function will be graded for this assessment. The function should work for any integer passed to minutes_to_hours beyond the examples provided.

Example: If the argument representing 60 minutes is

60
the expected return is

1.0
Example: If the argument representing 30 minutes is

30
the expected return is

0.5

"""


def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

# You may alter the code below to test your solution or print help documentation.
# Only the minutes_to_hours function will be graded for this assessment.

# mins = 60
# print(minutes_to_hours(mins))
# help(help)