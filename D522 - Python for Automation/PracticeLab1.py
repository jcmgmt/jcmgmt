"""

16.1 Practice Lab 1
An outdated design file has stored red, blue, and green (RGB) color values as separate integer values within a list. Combine all three color values into a single string value properly formatted as an RGB color.

Complete the Python function format_rgb. The function should accept a list of integers representing separate RGB values, combine the RGB values into a single string value properly formatted as an RGB color, and return the formatted RGB color. A formatted RGB color does not contain space characters between values.

Only the format_rgb function will be graded for this assessment. The function should work for any list of integers passed to format_rgb beyond the examples provided.

Example: If the stored RGB values are

[255, 165, 13]
the expected return is

rgb(255,165,13)
Example: If the stored RGB values are

[0, 0, 0]
the expected return is

rgb(0,0,0)

"""

def format_rgb(rgb):
    r, g, b = rgb
    return f"rgb({r},{g},{b})"
    return rgb


# You may alter the code below to test your solution or print help documentation.
# Only the format_rgb function will be graded for this assessment.

#rgb_sample = [255, 165, 13]
#print(format_rgb(rgb_sample))
# help(help)

"""

Practice Lab 2: Combining Date Components
A list contains separate integer values representing the year, month, and day of a date. Combine all three values into a single string formatted as a date in the format YYYY-MM-DD.

Complete the Python function format_date. The function should accept a list of integers representing separate year, month, and day values, combine them into a single string formatted as YYYY-MM-DD, and return the formatted date string. Ensure that the month and day are always displayed with two digits.

Example: If the stored date values are

python
Copy code
[2024, 9, 23]
the expected return is

yaml
Copy code
2024-09-23
If the stored date values are

python
Copy code
[1999, 1, 1]
the expected return is

yaml
Copy code
1999-01-01

"""

def format_date(entereddate):
    year, month, date = entereddate
    return f"{year}-{month}-{date}"

entereddate = [2023, 9, 23]
print(format_date(entereddate))

"""

Practice Lab 3: Formatting Time Values
A list contains separate integer values representing hours, minutes, and seconds of a time. Combine all three values into a single string formatted as a time in the format HH:MM:SS.

Complete the Python function format_time. The function should accept a list of integers representing separate hours, minutes, and seconds, combine them into a single string formatted as HH:MM:SS, and return the formatted time string. Ensure that hours, minutes, and seconds are always displayed with two digits.

Example: If the stored time values are

python
Copy code
[9, 5, 33]
the expected return is

makefile
Copy code
09:05:33
If the stored time values are

python
Copy code
[14, 0, 0]
the expected return is

makefile
Copy code
14:00:00

"""

def format_time(inputs):
    hr, min, sec = inputs
    return f"{hr:02d}:{min:02d}:{sec:02d}"

inputs = [6, 2, 30]
print(format_time(inputs))