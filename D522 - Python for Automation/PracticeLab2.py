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


def minutes_to_hours(mins):
    hours = mins / 60
    return hours

# You may alter the code below to test your solution or print help documentation.
# Only the minutes_to_hours function will be graded for this assessment.

mins = 120
print(minutes_to_hours(mins))
# help(help)

"""

Practice Lab 3: Seconds to Minutes Conversion
Complete the Python function seconds_to_minutes. The function should accept an integer representing the duration of a process in seconds, convert the value from seconds to minutes, and return a float representing the duration in minutes. There are 60 seconds in a minute. The function should utilize float division and not integer division.

Example: If the argument representing 120 seconds is

python
Copy code
120
the expected return is

Copy code
2.0
If the argument representing 45 seconds is

python
Copy code
45
the expected return is

Copy code
0.75


"""

def seconds_to_minutes(processinsec):
    sectomin = float(processinsec) / 60.0
    return sectomin

sectomin = 80
print(seconds_to_minutes(sectomin))

"""

Practice Lab 4: Hours to Days Conversion
Complete the Python function hours_to_days. The function should accept an integer representing a duration in hours, convert the value from hours to days, and return a float representing the duration in days. There are 24 hours in a day. The function should utilize float division and not integer division.

Example: If the argument representing 48 hours is

python
Copy code
48
the expected return is

Copy code
2.0
If the argument representing 36 hours is

python
Copy code
36
the expected return is

Copy code
1.5

"""

def hours_to_days(duration):
    hrtoday = float(duration) / 24.0
    return hrtoday

duration = 678
print(hours_to_days(duration))